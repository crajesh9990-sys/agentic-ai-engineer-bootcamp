from fastapi import APIRouter

from ai_service import ask_ai
from models import AIRequest, AIResponse

router = APIRouter()

@router.post("/ask")
def ask(request: AIRequest) -> AIResponse:
    print(f"Received prompt(routes): {request}, {request.prompt}")
    response = ask_ai(request.prompt)
    return AIResponse(response=response)

@router.get("/health")
def health_check():
    return {"status": "Up and running"}

@router.post("/summarize")
def summarize(request: AIRequest) -> AIResponse:
    prompt = f"""
    Summarize this text in five bullets.

    {request.prompt}
    """
    response = ask_ai(prompt)
    return AIResponse(response=response)

@router.post("/interview")
def interview(request: AIRequest) -> AIResponse:
    prompt = f"""
    Generate one AI interview question about

    {request.prompt}

    Return

    Question

    Ideal Answer

    Common Mistakes
    """
    response = ask_ai(prompt)
    return AIResponse(response=response)

@router.post("/python")
def python_code(request: AIRequest) -> AIResponse:
    prompt = f"""
    Generate production-quality Python code.

    {request.prompt}
    """
    response = ask_ai(prompt)
    return AIResponse(response=response)