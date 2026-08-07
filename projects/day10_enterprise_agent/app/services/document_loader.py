import json
import logging

from ..config import settings
from .embedding_service import embedding_service
from .vector_store import vector_store

logger = logging.getLogger(__name__)


class DocumentLoader:

    def load_documents(self):
        if vector_store.count() > 0:
            logger.info("Documents already indexed.")
            return

        logger.info("Loading company documents from %s", settings.DATA_PATH)

        with open(
            settings.DATA_PATH,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for item in data:
            ids.append(item["id"])
            documents.append(item["content"])
            embeddings.append(
                embedding_service.generate_embeddings(
                    item["content"]
                )
            )
            metadatas.append(
                {
                    "title": item["title"],
                    "department": item["department"],
                    "category": item["category"],
                    "author": item["author"],
                    "version": item["version"]
                }
            )

        vector_store.add_documents(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

        logger.info(
            "%s documents indexed successfully.",
            len(ids)
        )

document_loader = DocumentLoader()
