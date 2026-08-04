import ollama

MODEL = "llama3.2"

def ask_llm(prompt: str):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]