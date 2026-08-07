import re
import ollama

from app.agent.planner import planner
from app.agent.tool_registry import tool_registry
from .tool_selector_llm import llm_tool_selector
from ..utils.prompt_loader import PromptLoader
from ..services.llm_service import llm_service



class EnterpriseAgent:

    def __init__(self):
        pass


    def process(
        self,
        question: str
    ):

        tool_name = llm_tool_selector.select(
            question
        )

        plan = planner.create_plan(
            question,
            tool_name
        )

        result = self.execute_plan(
            plan
        )

        return result

    def execute_plan(
        self,
        plan
    ):
        tool = plan.tool
        question = plan.question

        if tool == "calculator":
            return self.execute_calculator(
                question
            )

        if tool == "weather":
            return self.execute_weather(
                question
            )

        if tool == "datetime":
            return tool_registry.execute(
                "datetime"
            )

        return tool_registry.execute(
            "rag",
            question=question
        )

    def execute_weather(
        self,
        question
    ):

        cities = [
            "chennai",
            "bangalore",
            "hyderabad"
        ]

        city = "chennai"

        for c in cities:
            if c in question.lower():
                city = c
                break

        return tool_registry.execute(
            "weather",
            city=city
        )

    def execute_calculator(
        self,
        question
    ):

        numbers = re.findall(
            r"\d+",
            question
        )

        if len(numbers) < 2:
            return {
                "error":
                "Need two numbers."
            }

        a = float(numbers[0])
        b = float(numbers[1])


        operation_prompt = PromptLoader.load_prompt(
            "calculator_prompt.txt"
        )

        operation_prompt_content = operation_prompt.format(question=question)
        messages = [
            {
                "role": "user",
                "content": operation_prompt_content
            }
        ]
        operation = llm_service.chat(messages=messages)

        # if "*" in question or "mul" in question:
        #     operation = "multiply"
        # elif "/" in question or "div" in question:
        #     operation = "divide"
        # elif "-" in question or "sub" in question:
        #     operation = "subtract"
        # else:
        #     operation = "add"

        return tool_registry.execute(
            "calculator",
            operation=operation,
            a=a,
            b=b
        )

agent = EnterpriseAgent()
