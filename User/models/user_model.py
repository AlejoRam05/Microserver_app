"""Definimos la entidad USER"""
from typing import Annotated
from pydantic import BaseModel, EmailStr
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import text
# from dotenv import load_dotenv
#BaseModel nos ayuda a crear nuestro modelo

class UserMain(SQLModel, table=True):
    "Valores/Data que debe ingresar el usuario, valores que espera la Clase User"
    id: int | None = Field(default=None, primary_key= True)
    name: str = Field(index=True)
    username: str = Field(index=True)
    email: EmailStr 
    hashed_password: str 
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None
    
# name: str | None = None  "| None = None -> nos permite obviar ese parametro"
async def user_client(usuarios: UserMain) -> UserMain:
    return usuarios


def create_db():
    sqlite_file_name = r"C:\\Users\\Creativa\\Documents\\GitHub\\Microserver_app\\User\\user_database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, connect_args=connect_args)
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        tables = session.exec(text("SELECT name FROM sqlite_master WHERE type='table';")).all()
        print("Tablas creadas:", tables)
