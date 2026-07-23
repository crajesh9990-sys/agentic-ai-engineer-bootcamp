import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"

def ask_ai(prompt: str):
    print(f"Received prompt(ai_service): {prompt}")
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    print(f"Received response(ai_service): {response.json()["response"]}")
    return response.json()["response"]
