from fastapi import APIRouter
from models import AskRequest
from embedding_service import get_embeddings
from vector_store import vector_store
from prompt_builder import build_prompt
from llm_service import ask_llm

router = APIRouter()

@router.post("/ask")
def ask(request: AskRequest):
    embedding = get_embeddings(
        request.question
    )
    results = vector_store.search_docs(query_embeddings=embedding, top_k=3)

    print(results)

    docs = results["documents"][0]

    metadata = results["metadatas"][0]

    distances = results["distances"][0]

    prompt = build_prompt(
        request.question,
        docs
    )

    answer = ask_llm(
        prompt
    )

    retrieval = []
    for doc, metadata_item, distance in zip(docs, metadata, distances):
        retrieval.append(
            {
                "title": metadata_item["title"],
                "document": doc,
                "distance": distance
            }
        )

    return {
        "question": request.question,
        "answer": answer,
        "sources": [
            item["title"]
            for item in metadata
        ],
        "retrieval": retrieval,
    }