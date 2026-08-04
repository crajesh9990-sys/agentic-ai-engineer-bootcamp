import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from llm_service import LLMService
from prompt_builder import PromptBuilder


class FakeMessage:
    def __init__(self, content):
        self.content = content


class FakeResponse:
    def __init__(self, content):
        self.message = FakeMessage(content)


def test_prompt_builder_returns_messages_with_content():
    messages = PromptBuilder.build_prompt(
        history=[{"role": "user", "content": "Earlier question"}],
        documents=["Relevant document"],
        question="Current question",
    )

    assert isinstance(messages, list)
    assert messages[0]["role"] == "system"
    assert "content" in messages[0]
    assert messages[-1]["content"] == "Current question"


def test_llm_service_extracts_content_from_response_object():
    service = LLMService()

    with patch("llm_service.ollama.chat", return_value=FakeResponse("hello from model")):
        answer = service.chat([{"role": "user", "content": "hi"}])

    assert answer == "hello from model"
