from fastapi import APIRouter, HTTPException
import logging

from models import ChatRequest
from embedding_service import embedding_service
from vector_store import vector_store
from prompt_builder import prompt_builder
from session_manager import session_manager
from llm_service import llm_service

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    session_id = request.session_id

    if not session_id:
        session_id = session_manager.create_session()

    if not session_manager.session_exists(session_id=session_id):
        session_id = session_manager.create_session()

    # session_manager.add_message(
    #     session_id,
    #     "user",
    #     request.question
    # )

    history = session_manager.get_history(session_id)
    logger.info("Chat history: %s", history)

    embedding = embedding_service.generate_embeddings(request.question)
    logger.info("Request embedding preview: %s", embedding[:5] if embedding else embedding)


    results = vector_store.search(embedding)

    documents = results["documents"][0]
    metadata = results["metadatas"][0]
    distances = results["distances"][0]

    messages = prompt_builder.build_prompt(
        history,
        documents,
        request.question
    )

    session_manager.add_message(session_id, "user", request.question)

    answer = llm_service.chat(messages)

    session_manager.add_message(session_id, "system", answer)

    retrieval = []

    for doc, meta, distance in zip(documents, metadata, distances):
        retrieval.append(
            {
                "title": meta["title"],
                "distance": round(distance, 4),
                "preview": doc[:120]
            }
        )

    return {
        "session_id": session_id,
        "answer": answer,
        "sources": [
            item["title"]
            for item in metadata
        ],
        "retrieval": retrieval
    }

@router.get("/session/{session_id}")
def get_session(session_id: str):
    if not session_manager.session_exists(session_id):
        raise HTTPException(
            status_code=404,
            detail="Session not found."
        )

    return {
        "session_id": session_id,
        "messages": session_manager.get_history(
            session_id
        )
    }

@router.delete("/session/{session_id}")
def clear_session(session_id: str):
    session_manager.clear_history(
        session_id
    )
    return {
        "message": "Conversation cleared."
    }
