from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    nombre:str
    apellido:str 
    documento:int
    avatar:str
    email:str
    direccion:str 
    password:str 
