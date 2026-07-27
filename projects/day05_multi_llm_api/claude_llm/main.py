import os
from openai import OpenAI
from config import ANTHROPIC_API_KEY, ANTHROPIC_BASE_URL, ANTHROPIC_MODEL

# Notes: Install below package
# npm install -g @anthropic-ai/claude-code

api_key = ANTHROPIC_API_KEY or os.getenv("ANTHROPIC_API_KEY")
base_url = ANTHROPIC_BASE_URL or os.getenv("ANTHROPIC_BASE_URL")
model = ANTHROPIC_MODEL or os.getenv("ANTHROPIC_MODEL") or "gemini-2.0-flash"

if not api_key or not base_url:
    raise RuntimeError("ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL must be set")

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

try:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": "Write a Python function to reverse a string."}
        ],
    )
    print(response.choices[0].message.content)
except Exception as exc:
    print(f"Request failed: {exc}")
    raise SystemExit(1)