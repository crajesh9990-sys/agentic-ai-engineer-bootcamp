import logging
import ollama

from config import settings

logger = logging.getLogger(__name__)


class LLMService:

    def __init__(self):
        self.model = settings.LLM_MODEL

    def _extract_content(self, response) -> str:
        if isinstance(response, dict):
            message = response.get("message") or {}
            if isinstance(message, dict):
                return message.get("content", "")
        if hasattr(response, "message"):
            message = getattr(response, "message")
            if hasattr(message, "content"):
                return message.content
        return ""

    def chat(self, messages) -> str:
        try:
            response = ollama.chat(
                model=self.model,
                messages=messages,
                options={
                    "temperature": 0.2
                },
            )
            return self._extract_content(response)
        except Exception:
            logger.exception("LLM request failed")
            raise

    def stream_chat(self, messages):
        try:
            return ollama.chat(
                model=self.model,
                messages=messages,
                stream=True,
                options={
                    "temperature": 0.2
                },
            )
        except Exception:
            logger.exception("Streaming request failed")
            raise


llm_service = LLMService()
