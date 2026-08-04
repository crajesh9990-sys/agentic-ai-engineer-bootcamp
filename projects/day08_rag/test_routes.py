import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import routes


class DummyRequest:
    def __init__(self, question: str):
        self.question = question


def test_ask_returns_sources_from_metadata(monkeypatch):
    monkeypatch.setattr(routes, "get_embeddings", lambda question: [0.1, 0.2])
    monkeypatch.setattr(
        routes.vector_store,
        "search_docs",
        lambda query_embeddings, top_k=3: {
            "documents": [["doc1", "doc2", "doc3"]],
            "metadatas": [[{"title": "Alpha"}, {"title": "Beta"}, {"title": "Gamma"}]],
            "distances": [[0.1, 0.2, 0.3]],
        },
    )
    monkeypatch.setattr(routes, "build_prompt", lambda question, docs: "prompt")
    monkeypatch.setattr(routes, "ask_llm", lambda prompt: "answer")

    response = routes.ask(DummyRequest("hello"))

    assert response["answer"] == "answer"
    assert response["sources"] == ["Alpha", "Beta", "Gamma"]
