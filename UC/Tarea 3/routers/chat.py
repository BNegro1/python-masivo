from fastapi import APIRouter, HTTPException, BackgroundTasks, status
from models import ChatRequest, ChatResponse
from services.chat_service import get_movie_response, ChatServiceError
from typing import Dict, Any
import asyncio

router = APIRouter()

@router.post("/chat", 
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    responses={
        500: {"description": "Error interno del servidor"},
        504: {"description": "Tiempo de espera agotado"},
        400: {"description": "Solicitud inválida"}
    }
)
async def chat_endpoint(
    request: ChatRequest,
    background_tasks: BackgroundTasks
):
    try:
        response = await get_movie_response(
            messages=request.messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        background_tasks.add_task(log_conversation, request, response)
        
        return ChatResponse(
            response=response["choices"][0]["message"]["content"],
            context_used=response["context"]["fragments"]
        )
        
    except ChatServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )

async def log_conversation(request: ChatRequest, response: Dict):
    
    pass