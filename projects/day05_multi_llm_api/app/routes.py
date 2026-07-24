from fastapi import APIRouter
from loguru import logger
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

try:
    from app.config import LLM_PROVIDER, MODEL
    from app.models import AIRequest, AIResponse, ProgrammingRequest, PersonaRequest
    from app.prompt_service import PromptService
    from app.providers.provider_factory import ProviderFactory
except ImportError:  # pragma: no cover - supports script-style execution
    from config import LLM_PROVIDER, MODEL
    from models import AIRequest, AIResponse, ProgrammingRequest, PersonaRequest
    from prompt_service import PromptService
    from providers.provider_factory import ProviderFactory

router = APIRouter()
service = PromptService()
# aiProvider = OllamaProvider()
aiProvider = ProviderFactory.get_provider()

@router.post("/explain")
def explain(request: AIRequest) -> AIResponse:
    logger.info("Request payload: {}", request.model_dump_json())
    prompt = service.explain_prompt(request.prompt)
    generated_text = aiProvider.generate(prompt)
    return AIResponse(response=generated_text)

@router.get("/provider")
def get_provider():
    return {"provider": LLM_PROVIDER, "model": MODEL}
