from fastapi import HTTPException
from typing import Dict, Any, Optional, List
import asyncio, httpx, time
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from search import search_movies
from models import Message, ChatRequest

class RateLimitExceeded(Exception):
    pass

class ChatServiceError(Exception):
    pass

class RateLimiter:
    def __init__(self, max_requests: int = 10, time_window: int = 1):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []

    async def acquire(self):
        now = time.time()
        self.requests = [req_time for req_time in self.requests 
                        if now - req_time < self.time_window]
        if len(self.requests) >= self.max_requests:
            raise RateLimitExceeded("Rate limit exceeded")
        self.requests.append(now)

rate_limiter = RateLimiter()

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(RateLimitExceeded)
)
async def call_llm_api(messages: List[Dict], params: Dict) -> Dict:
    await rate_limiter.acquire()
    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            response = await client.post(
                f"{settings.LLM_API_URL}/api/chat",
                json={
                    "model": "integra-LLM",
                    "messages": messages,
                    **params
                },
                headers={"Authorization": f"Bearer {settings.LLM_API_KEY}"}
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutError:
            raise ChatServiceError("Tiempo de respuesta excedido")
        except httpx.HTTPError as e:
            raise ChatServiceError(f"Error en la llamada al LLM: {str(e)}")

async def get_movie_response(request: ChatRequest) -> Dict[Any, Any]:
    try:
        user_query = request.messages[-1].content
        search_results = await search_movies(user_query)
        
        total_tokens = 0
        filtered_results = []
        for doc in search_results:
            tokens = len(doc.page_content.split())
            if total_tokens + tokens <= 1000:
                filtered_results.append(doc)
                total_tokens += tokens
            else:
                break
                
        context = "\n".join([r.page_content for r in filtered_results])
        
        messages = [
            {
                "role": "system",
                "content": (
                    "Eres un experto en películas. Usa el siguiente contexto "
                    "para responder preguntas sobre películas de manera detallada y precisa."
                )
            },
            {
                "role": "user", 
                "content": f"Contexto del guión:\n{context}\n\nPregunta: {user_query}"
            }
        ]
        
        params = {
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
            "num_ctx": request.num_ctx,
            "top_k": request.top_k
        }
        
        result = await call_llm_api(messages, params)
        
        result["context"] = {
            "fragments": [r.page_content for r in filtered_results],
            "metadata": {
                "total_tokens": total_tokens,
                "timestamp": datetime.now().isoformat()
            }
        }
        
        return result
    except Exception as e:
        raise ChatServiceError(f"Error en el servicio de chat: {str(e)}")
