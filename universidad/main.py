from fastapi import FastAPI
from src.model.connection import Connection
from src.schema.user_schema import UserSchema


app = FastAPI()
connection = Connection()
print(connection)


@app.get("/")
async def root():
    connection
    return {"message": "Hello World"}

@app.post("/api/insert")
def insert(user_data: UserSchema):
    data = user_data.model_dump()
    connection.write(data)
    