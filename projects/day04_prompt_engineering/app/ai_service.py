import requests
from openai import OpenAI

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"

OPENAI_API_KEY = "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"

from openai import OpenAI
import os

client = OpenAI(
    api_key=OPENAI_API_KEY
)

def ask_ai_openai(prompt: str):
    response = client.responses.create(
        model="gpt-5-nano",
        input="Write a Python function to reverse a string."
    )
    return response.output_text

def ask_ai(prompt: str):
    print(f"Received prompt(ai_service): {prompt}")
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    print(f"Received response(ai_service): {response.json()['response']}")
    return response.json()["response"]
