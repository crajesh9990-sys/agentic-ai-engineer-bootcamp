from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Prompt Engineering API",
    version="1.0.0",
    description="An API for interacting with an AI model to generate responses based on prompts."
)

app.include_router(router)
