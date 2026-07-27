import json
from pathlib import Path
from document import Document
from embedding_service import get_embeddings

class DocumentStore():
    def __init__(self):
        self.documents: list[Document] = []

    def load_documents(self):
        DOCUMENTS_DIR = Path(__file__).resolve().parent / "data" / "documents.json"
        with open(DOCUMENTS_DIR, "r", encoding="utf-8") as file:
            docs = json.load(file)

        self.documents.clear()

        for doc in docs:
            document = Document(
                title=doc["title"],
                content=doc["content"],
                embedding=get_embeddings(doc["content"])
            )

            self.documents.append(document)

    def get_documents(self):
        return self.documents

document_store = DocumentStore()
