from contextlib import asynccontextmanager

from fastapi import FastAPI

from load_documents import load_documents
from routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_documents()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)