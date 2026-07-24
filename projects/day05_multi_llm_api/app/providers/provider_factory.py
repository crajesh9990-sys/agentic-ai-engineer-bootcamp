import sys
from pathlib import Path
from typing import Type
from loguru import logger

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

try:
    from app.config import LLM_PROVIDER
    from app.providers.base import BaseProvider
    from app.providers.ollama_provider import OllamaProvider
    from app.providers.openai_provider import OpenAIProvider
except ImportError:  # pragma: no cover - supports script-style execution
    from config import LLM_PROVIDER
    from providers.base import BaseProvider
    from providers.ollama_provider import OllamaProvider
    from providers.openai_provider import OpenAIProvider


class ProviderFactory:

    _PROVIDERS: dict[str, type[BaseProvider]] = {
        "ollama": OllamaProvider,
        "openai": OpenAIProvider,
    }

    @staticmethod
    def get_provider() -> BaseProvider:
        provider_name = (LLM_PROVIDER or "ollama").lower()

        logger.info(f"Provider name: {provider_name}")

        provider_cls = ProviderFactory._PROVIDERS.get(provider_name)
        if not provider_cls:
            raise ValueError(f"Unsupported provider: {LLM_PROVIDER}")

        return provider_cls()
