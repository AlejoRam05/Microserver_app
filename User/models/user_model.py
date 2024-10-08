"""Definimos la entidad USER"""

from pydantic import BaseModel, EmailStr
from datetime import datetime

#BaseModel nos ayuda a crear nuestro modelo

class UserMain(BaseModel):
    "Valores/Data que debe ingresar el usuario, valores que espera la Clase User"
    id: int
    name: str 
    username: str 
    email: EmailStr 
    hashed_password: str 
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None
    
# name: str | None = None  "| None = None -> nos permite obviar ese parametro"
async def user_client(usuarios: UserMain) -> UserMain:
    return usuarios

    
