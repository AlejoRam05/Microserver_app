"""Definimos la entidad USER"""

from pydantic import BaseModel 

#BaseModel nos ayuda a crear nuestro modelo

class User(BaseModel):
    "Valores/Data que debe ingresar el usuario, valores que espera la Clase User"
    id = int 
    name: str 
    username: str 
    age: int 
    mail: str 
    password: str 
    
# name: str | None = None  "| None = None -> nos permite obviar ese parametro"

