from fastapi import FastAPI
from src.model.connection import Connection


app = FastAPI()
connection = Connection()


@app.get("/")
async def root():
    connection
    return {"message": "Hello World"}