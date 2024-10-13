"""Definimos la entidad USER"""
from pydantic import EmailStr
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import text
from dotenv import load_dotenv
import os
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

class DatabaseUser:
    
    @staticmethod
    def create_db():
        load_dotenv()
        sqlite_file_name = os.getenv("sqlite_file_name")
        sqlite_url = f"sqlite:///{sqlite_file_name}"
        connect_args = {"check_same_thread": False}
        engine = create_engine(sqlite_url, connect_args=connect_args)
        SQLModel.metadata.create_all(engine) # crea la base de  datos
        try:
            with Session(engine) as session:
                tables = session.exec(text("SELECT name FROM sqlite_master WHERE type='table';")).all()
                print("Tablas creadas:", tables)
        except Exception as e:
            print("Error al interactuar con el Database", e)