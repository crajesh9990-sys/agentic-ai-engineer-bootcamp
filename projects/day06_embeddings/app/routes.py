from fastapi import APIRouter

from cosine_similarity import find_consine_similarity
from document_store import document_store
from embedding_service import get_embeddings
from models import SearchRequest


router = APIRouter()


@router.post("/search")
def search(searchRequest: SearchRequest):
    documents = document_store.get_documents()

    if not documents:
        return {"query": searchRequest.query, "best_match": None, "score": None}

    req_embedding = get_embeddings(searchRequest.query)
    best_document = None
    best_score = -1.0

    for doc in documents:
        score = find_consine_similarity(req_embedding, doc.embedding)
        if score > best_score:
            best_score = score
            best_document = doc

    return {
        "query": searchRequest.query,
        "best_match": best_document.title if best_document else None,
        "score": round(float(best_score), 4) if best_document else None,
    }

# def getFiles():
#     documents = _load_documents()
#     print(documents)


# getFiles()