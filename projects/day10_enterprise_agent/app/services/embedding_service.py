import logging
import ollama
from typing import List

from config import settings

logger = logging.getLogger(__name__)


class EmbeddingService:

    def __init__(self):
        self.model = settings.EMBEDDING_MODEL

    def _extract_embedding(self, response) -> List[float]:
        if isinstance(response, dict):
            if "embeddings" in response and response["embeddings"]:
                return response["embeddings"][0]
            if "embedding" in response and response["embedding"]:
                return response["embedding"]

        embeddings = getattr(response, "embeddings", None)
        if embeddings:
            return embeddings[0]

        embedding = getattr(response, "embedding", None)
        if embedding:
            return embedding

        raise ValueError("Unexpected embedding response format")

    def generate_embeddings(self, text: str) -> List[float]:
        try:
            response = ollama.embed(
                model=self.model,
                input=text
            )
            embedding = self._extract_embedding(response)
            logger.info(
                "Embeddings generated for input '%s' (preview: %s)",
                text[:80],
                embedding[:5]
            )
            return embedding
        except Exception:
            logger.exception("Embeddings generation failed")
            raise


embedding_service = EmbeddingService()
