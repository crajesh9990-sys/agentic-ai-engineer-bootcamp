import chromadb

client = chromadb.PersistentClient("./chromadb")

collection = client.get_or_create_collection(name="employee_docs")

class VectorStore:
    def search_docs(self, query_embeddings, top_k = 3):
        return collection.query(
            query_embeddings=query_embeddings,
            n_results = top_k
        )

vector_store = VectorStore()
