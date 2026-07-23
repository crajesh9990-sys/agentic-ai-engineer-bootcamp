from typing import Generator, Annotated
from fastapi import Depends, FastAPI

app = FastAPI()


def get_db() -> Generator:
    db = "DB_SESSION_CONNECTED"  # Simulate DB Connection
    try:
        yield db
    finally:
        print("Closing DB connection...")  # Executes after response is sent

@app.get("/data/")
async def read_data(db: Annotated[str, Depends(get_db)]):
    return {"db_status": db}