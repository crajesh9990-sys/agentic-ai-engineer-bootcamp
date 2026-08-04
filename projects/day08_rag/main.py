from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import router
from load_documents import load_documents

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_documents()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)

