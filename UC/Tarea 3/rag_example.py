import httpx
from search import search_movies

async def get_movie_response(query: str):

    results = await search_movies(query)
    context = "\n".join([r.page_content for r in results])
    
    system_prompt = f"""
    Eres un asistente experto en películas. Responde usando el siguiente contexto de los guiones:
    ```
    {context}
    ```
    Proporciona respuestas detalladas y precisas basadas en el contexto proporcionado.
    """
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://tormenta.ing.puc.cl/api/chat",
            json={
                "model": "llama3.2",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                "temperature": 0.7,
                "max_tokens": 500
            }
        )
        return response.json()
