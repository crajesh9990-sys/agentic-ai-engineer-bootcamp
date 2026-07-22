import requests

url = "http://localhost:11434/api/generate"
model = "llama3.2"

def ask_AI(prompt: str) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"An error occurred while generating the response. {e}"