from fastapi import FastAPI, requests, responses
from src.model.connection import Connection
from src.schema.user_schema import UserSchema
from jinja2 import Template, Environment, FileSystemLoader


app = FastAPI()
connection = Connection()
file_loader = FileSystemLoader('src/templates')
env = Environment(loader=file_loader)

@app.get("/")
async def root():
    template = env.get_template('index.html')
    return responses.HTMLResponse(content=template.render())
   
@app.get("/estudiantes")
async def show_students():
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
        
    template = env.get_template('estudiantes.html')
    return responses.HTMLResponse(content=template.render(items=items))

@app.get("/estudiante")
async def estudiante():
    template = env.get_template('estudiante.html')
    return responses.HTMLResponse(content=template.render())

@app.get("/estudiante/id")
async def read_by_id(id: int):
    student = {}
    row = connection.read_by_id(id)
    if row:
        student['id'] = row[0]
        student['nombres'] = row[1]
        student['apellidos'] = row[2]
        student['cedula'] = row[3]
        student['email'] = row[4]
        student['telefono'] = row[5]
    template = env.get_template('estudiante.html')
    return responses.HTMLResponse(content=template.render(student=student))

@app.get("/elimina_estudiante")
async def elimina_estudiante():
    template = env.get_template('elimina_estudiante.html')
    return responses.HTMLResponse(content=template.render())

@app.post("/delete/id")
async def delete(id: int):
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
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)