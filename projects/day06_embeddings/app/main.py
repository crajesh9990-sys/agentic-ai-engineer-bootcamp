from contextlib import asynccontextmanager

from fastapi import FastAPI

from document_store import document_store
from routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    document_store.load_documents()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)
