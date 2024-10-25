"""MODELO DE QUE DATOS ESTARIA ESPERANDO PARA PROCESAR """
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import Optional

class Product(BaseModel):

    name_product: str
    descripcion_product: str
    price: int
    stock: int

class ProductDB(Product, SQLModel, table = True):

    id: Optional[int] = Field(primary_key=True, default=None)


