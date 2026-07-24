from dotenv import load_dotenv
import os

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER")
MODEL = os.getenv("MODEL")
OLLAMA_URL=os.getenv("OLLAMA_URL")
