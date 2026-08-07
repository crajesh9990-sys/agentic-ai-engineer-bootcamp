from pathlib import Path


class Settings:

    APP_NAME = "Enterprise AI Agent"

    APP_VERSION = "1.0.0"

    APP_DESCRIPTION = "Enterprise AI Agent"

    LLM_MODEL = "llama3.2"

    EMBEDDING_MODEL = "nomic-embed-text"

    COLLECTION_NAME = "employee_docs"

    CHROMA_PATH = "./chromadb"

    MEMORY_WINDOW = 10

    DATA_PATH = (
        Path(__file__).resolve().parents[1] / "data" / "documents.json"
    )


settings = Settings()