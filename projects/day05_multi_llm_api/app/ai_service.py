from provider import OllamaProvider

provider = OllamaProvider()

def ask_ai(prompt: str) -> str:
    provider.generate(prompt=prompt)
