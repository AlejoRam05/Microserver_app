"""MODELO DE QUE DATOS ESTARIA ESPERANDO PARA PROCESAR """
from datetime import datetime
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import Optional

class InventoryBase(BaseModel):
    
    product: str = Field(index = True)
    price: int 
    description: str
    stock: int
    
class InventoryDB(SQLModel, table = True):
    
    code: Optional[int] = Field(index=True, primary_key=True, autoincrement=True)
    product: str 
    price: int 
    description: str
    stock: int
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)
    