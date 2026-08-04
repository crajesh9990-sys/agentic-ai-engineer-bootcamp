from typing import List

SYSTEM_PROMPT = """
You are an Enterprise IT Support Assistant.

Rules:

1. Answer ONLY using the supplied context.

2. If the answer cannot be found,
say:

"I don't have enough information."

3. Be concise.

4. Be professional.

5. If appropriate,
mention the document source.
"""


class PromptBuilder:

    @staticmethod
    def build_prompt(
        history: List[dict],
        documents: List[str],
        question: str
    ) -> List[dict]:
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

        messages.extend(history)

        context = "\n\n".join(documents) if documents else "No relevant documents found."

        messages.append(
            {
                "role": "system",
                "content": f"""
context
--------------------
{context}
--------------------
""",
            }
        )

        messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        return messages


prompt_builder = PromptBuilder()
