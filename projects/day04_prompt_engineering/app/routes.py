from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from models import AIRequest, ProgrammingRequest, PersonaRequest
from prompt_builder import explain_prompt, summarize_prompt, interview_prompt, code_prompt, rewrite_prompt, architect_prompt, review_code_prompt, programming_language_prompt, persona_prompt
from ai_service import ask_ai

router = APIRouter()

@router.post("/explain", response_class=PlainTextResponse)
def explain(request: AIRequest) -> str:
    response = ask_ai(explain_prompt(request.prompt))
    return response

@router.post("/summarize", response_class=PlainTextResponse)
def summarize(request: AIRequest) -> str:
    response = ask_ai(summarize_prompt(request.prompt))
    return response

@router.post("/interview", response_class=PlainTextResponse)
def interview(request: AIRequest) -> str:
    response = ask_ai(interview_prompt(request.prompt))
    return response

@router.post("/code", response_class=PlainTextResponse)
def code(request: AIRequest) -> str:
    response = ask_ai(code_prompt(request.prompt))
    return response

@router.post("/rewrite", response_class=PlainTextResponse)
def rewrite(request: AIRequest) -> str:
    response = ask_ai(rewrite_prompt(request.prompt))
    return response

@router.post("/architect", response_class=PlainTextResponse)
def architect(request: AIRequest) -> str:
    response = ask_ai(architect_prompt(request.prompt))
    return response

@router.post("/code-review", response_class=PlainTextResponse)
def code_review(request: AIRequest) -> str:
    response = ask_ai(review_code_prompt(request.prompt))
    return response

@router.post("/generate-code", response_class=PlainTextResponse)
def code_generator(request: ProgrammingRequest) -> str:
    response = ask_ai(programming_language_prompt(request.language, request.task))
    return response

@router.post("/persona", response_class=PlainTextResponse)
def persona_generator(request: PersonaRequest) -> str:
    response = ask_ai(persona_prompt(request.role, request.question))
    return response
