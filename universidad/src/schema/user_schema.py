from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    nombres: str 
    apellidos: str
    cedula: str
    email: str
    telefono: str