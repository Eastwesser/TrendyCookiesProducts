from fastapi import FastAPI
from database.database import Base

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_in_transaction(Base.metadata.create_all)