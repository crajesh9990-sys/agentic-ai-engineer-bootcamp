import chromadb
import logging
from typing import List, Dict, Any

from config import settings

class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_PATH)

        self.collection = self.client.get_or_create_collection(name=settings.COLLECTION_NAME)

    def add_documents(
            self,
            ids: List[str],
            documents: List[str],
            embeddings: List[float],
            metadatas = List[dict]
    ):
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
            self,
            embeddings: List[float],
            top_k: int = 3
     ) -> Dict[str, Any]:
        return self.collection.query(query_embeddings=embeddings, n_results=top_k)

    def count(self):
        return self.collection.count()

    def delete_all(self):
        ids = self.collection.get()["ids"]
        if ids:
            return self.collection.delete(ids=ids)

vector_store = VectorStore()