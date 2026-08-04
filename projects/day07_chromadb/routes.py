from fastapi import APIRouter
from models import SearchRequest
from embedding_service import get_embeddings
from load_documents import collection
from vector_store import vector_store

router = APIRouter()

@router.post("/search")
def search_docs(request: SearchRequest):

    query_embeddings = get_embeddings(request.query)

    results = vector_store.search_docs(query_embeddings=query_embeddings, top_k=3)

    print(results)

    response = []

    documents = results["documents"][0]
    metadata = results["metadatas"][0]
    distances = results["distances"][0]

    for doc, meta, distance in zip(
        documents,
        metadata,
        distances
    ):
        response.append({
            "title": meta["title"],
            "content": doc,
            "distance": distance
        })

    return {
        "query": request.query,
        "results": response
    }