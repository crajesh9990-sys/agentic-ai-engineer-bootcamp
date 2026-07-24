import os
import sys
from pathlib import Path

from loguru import logger

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

try:
    from app.providers.base import BaseProvider
except ImportError:  # pragma: no cover - supports script-style execution
    from app.providers.base import BaseProvider


class OpenAIProvider(BaseProvider):
    def generate(self, prompt):
        raise NotImplementedError("OpenAI provider is not available")
