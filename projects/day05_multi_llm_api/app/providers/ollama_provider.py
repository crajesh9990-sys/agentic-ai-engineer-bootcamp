import os
import sys
from pathlib import Path

import requests
from loguru import logger

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

try:
    from app.providers.base import BaseProvider
except ImportError:  # pragma: no cover - supports script-style execution
    from app.providers.base import BaseProvider


class OllamaProvider(BaseProvider):
    def generate(self, prompt: str):
        payload = {
            "model": os.getenv("MODEL"),
            "prompt": prompt,
            "stream": False,
        }

        logger.info("Calling Ollama...")
        response = requests.post(os.getenv("OLLAMA_URL"), json=payload)
        response.raise_for_status()
        return response.json()["response"]
