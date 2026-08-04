from typing import List, Optional
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    session_id: Optional[str] = Field(default=None, description="Conversation session id")
    question: str = Field(
        ...,
        min_length=1,
        description="User question"
    )

class RetrievalResult(BaseModel):
    title: str
    distance: float
    preview: str

class ChatResponse(BaseModel):
    session_id: str
    answer: str
    sources: List[str]
    retrieval: List[RetrievalResult]

class SessionResponse(BaseModel):
    session_id: str
    messages: List[dict]

class Message(BaseModel):
    role: str
    content: str
