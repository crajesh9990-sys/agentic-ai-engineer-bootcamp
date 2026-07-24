import requests
from loguru import logger

try:
    from .config import LLM_PROVIDER, MODEL, OLLAMA_URL
except ImportError:  # pragma: no cover - supports script-style execution
    from config import LLM_PROVIDER, MODEL, OLLAMA_URL


class OllamaProvider:
    def generate(self, prompt):
        payload = {
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        }
        logger.info("Calling Ollama...")

        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        return response.json()["response"]
