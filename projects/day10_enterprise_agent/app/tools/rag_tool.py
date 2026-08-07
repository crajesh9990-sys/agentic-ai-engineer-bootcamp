from app.services.embedding_service import embedding_service
from app.services.vector_store import vector_store


class RagTool:
    name = "rag"
    description = "Answers questions using enterprise documents."

    def execute(
        self,
        question: str,
        top_k: int = 3
    ):
        embedding = embedding_service.generate_embeddings(
            question
        )

        results = vector_store.search(
            embedding,
            top_k
        )

        return {
            "tool": self.name,
            "results": results
        }

rag_tool = RagTool()
