from pydantic import BaseModel

class AIRequest(BaseModel):
    prompt: str

class AIResponse(BaseModel):
    response: str

class ProgrammingRequest(BaseModel):
    language: str
    task: str

class PersonaRequest(BaseModel):
    role: str
    question: str
