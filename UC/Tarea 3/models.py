from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from enum import Enum

class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class Message(BaseModel):
    role: MessageRole
    content: str
    timestamp: Optional[float] = None

class ChatRequest(BaseModel):
    messages: List[Message]
    temperature: float = Field(default=0.6, ge=0, le=1)
    max_tokens: int = Field(default=500, ge=1)
    num_ctx: int = Field(default=2048, ge=1)
    top_k: int = Field(default=18, ge=1)

class ChatResponse(BaseModel):
    response: str
    context_used: List[str] = []
    metadata: Dict[str, Any] = {}