from pathlib import Path
import json
from document import Document

from embedding_service import get_embeddings

DOCUMENTS_DIR = Path(__file__).resolve().parent / "data" / "documents.json"

DOCUMENTS: list[Document] = []


def loadDocuments():
    global DOCUMENTS

    with DOCUMENTS_DIR.open("r", encoding="utf-8") as file:
        documents = json.load(file)

    DOCUMENTS.clear()

    for doc in documents:
        DOCUMENTS.append(
            {
                "title": doc["title"],
                "content": doc["content"],
                "embedding": get_embeddings(doc["content"])
            }
        )

    return DOCUMENTS
