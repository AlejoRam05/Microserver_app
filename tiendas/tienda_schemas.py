"""MODELO DE QUE DATOS ESTARIA ESPERANDO PARA PROCESAR """
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field
from typing import Optional

class TiendaBase(BaseModel):
    
    name: str
    direction: str 
    location: str
    mail: EmailStr
    sucursal: str



class TiendaDB(SQLModel, TiendaBase, table = True):
    
    id: Optional[int] = Field(default=None, primary_key=True)


