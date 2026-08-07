"""
LLM Tool Selector
"""

from ..utils.prompt_loader import PromptLoader
from .tool_metadata import TOOLS
from ..services.llm_service import llm_service



class LLMToolSelector:

    def __init__(self):
        self.prompt = PromptLoader.load_prompt(
            "tool_selection_prompt.txt"
        )

    def select(self, question: str):
        tools = ""

        for tool in TOOLS:
            tools += (
                f"Name: {tool['name']}\n"
                f"Description: {tool['description']}\n"
            )

        prompt = self.prompt.format(
            question=question,
            tools=tools
        )

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = llm_service.chat(
            messages
        )

        return response.strip().lower()

llm_tool_selector = LLMToolSelector()

        