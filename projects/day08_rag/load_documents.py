import ollama
import json
from pathlib import Path

from vector_store import collection
from embedding_service import get_embeddings

def load_documents():
    print("Documents loading...")
    DOCS_DIRECTORY = Path(__file__).resolve().parent / "data" / "documents.json"

    with open(DOCS_DIRECTORY, "r", encoding="utf-8") as file:
        docs = json.load(file)

    for doc in docs:
        print("loading document ", doc["id"])
        embedding = get_embeddings(doc["content"])

        collection.add(
            ids=[doc["id"]],
            documents=[doc["content"]],
            embeddings=[embedding],
            metadatas=[
                {
                    "title": doc["title"]
                }
            ]
        )

    print("Documents loaded...", collection.count())
