"""Definimos la entidad USER"""
from pydantic import EmailStr, BaseModel
from datetime import datetime
from typing import Optional, Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import text
from dotenv import load_dotenv
import os 
from fastapi import Depends, HTTPException, Query

# from dotenv import load_dotenv
#BaseModel nos ayuda a crear nuestro modelo
load_dotenv()
sqlite_file_name = os.getenv("sqlite_file_name")
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

class UserClient(BaseModel):
    name: str = Field(index=True)
    username: str = Field(index=True)
    email: EmailStr 

class UserMain(SQLModel,UserClient, table=True):
    "Valores/Data que debe ingresar el usuario, valores que espera la Clase User"
    id: int = Field(default=None, primary_key=True)
    hashed_password: str 
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)

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


async def create_cliente(cliente: UserMain, session: SessionDep) -> UserMain:
    try:
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        return cliente
    except Exception as e:
        session.rollback()  # Deshacer cambios en caso de error
        raise HTTPException(status_code=400, detail=f"Error al crear el usuario: {str(e)}")
    
async def read_clientes(session: SessionDep, offset: int=0, limit: Annotated[int, Query(le=100)]=100) -> list[UserMain]:
    statement = select(UserMain).offset(offset).limit(limit)
    return session.exec(statement).all()
