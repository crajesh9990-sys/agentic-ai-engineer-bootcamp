class ToolSelector:
    def select(self, question: str) -> str:
        question = question.lower()

        calculator_words = [
            "calculate",
            "add",
            "subtract",
            "multiply",
            "divide",
            "+",
            "-",
            "*",
            "/"
        ]

        datetime_words = [
            "data", "time", "today", "day"
        ]

        if any(word in question for word in calculator_words):
            return "calculator"
        elif any(word in question for word in datetime_words):
            return "datetime"
        elif "weather" in question:
            return "weather"
        else:
            return "rag"

tool_selector = ToolSelector()
