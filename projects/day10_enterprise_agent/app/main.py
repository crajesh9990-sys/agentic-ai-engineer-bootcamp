import logging
import sys
from pathlib import Path
from fastapi import FastAPI
from contextlib import asynccontextmanager

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import logging_config
from app.services.document_loader import document_loader
from app.routes import router
from app.config import settings
from app.agent import register_tools


logging_config.setup_logging()

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application started...")
    logger.info("Loading documents...")
    document_loader.load_documents()
    yield
    logger.info("Application shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    lifespan=lifespan
)

app.include_router(
    router,
    prefix="/api/v1"
)

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
