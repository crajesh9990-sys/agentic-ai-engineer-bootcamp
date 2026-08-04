import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

import logging_config
from config import settings
from document_loader import document_loader
from routes import router

logging_config.setup_logging()

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging_config.setup_logging()

    logger.info("Loading documents...")
    document_loader.load_documents()
    logger.info("Application started...")
    yield
    logger.info("Application shutting down...")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Conversational RAG Assistant",
    lifespan=lifespan
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "status": "Application is up and running"
    }
