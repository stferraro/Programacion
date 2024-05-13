from fastapi import FastAPI
from src.model.connection import Connection
from src.schema.user_schema import UserSchema


app = FastAPI()
connection = Connection()


@app.get("/")
async def root():
    items = []
    for row in connection.read_all():
        dictionary = {}
        dictionary['id'] = row[0]
        dictionary['nombres'] = row[1]
        dictionary['apellidos'] = row[2]
        dictionary['cedula'] = row[3]
        dictionary['email'] = row[4]
        dictionary['telefono'] = row[5]
        items.append(dictionary)
    return items

@app.get("/api/estudiante/{id}")
async def read_by_id(id: str):
    items = {}
    row = connection.read_by_id(id)
    if row:
        items['id'] = row[0]
        items['nombres'] = row[1]
        items['apellidos'] = row[2]
        items['cedula'] = row[3]
        items['email'] = row[4]
        items['telefono'] = row[5]
    return items

@app.delete("/api/delete/{id}")
async def delete(id: str):
    connection.delete(id)
    return {"message": "El registro se eliminó correctamente"}

 
@app.put("/api/update/{id}")
def update(id: str, user_data: UserSchema):
    data = user_data.model_dump()
    data['id'] = id
    connection.update(data)
 

@app.post("/api/insert")
def insert(user_data: UserSchema):
    data = user_data.model_dump()
    connection.write(data)
    