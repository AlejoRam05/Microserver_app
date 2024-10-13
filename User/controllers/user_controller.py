from User.models.user_model import UserMain, user_client
from typing import Annotated
from sqlmodel import Session, create_engine
from fastapi import Depends
from dotenv import load_dotenv
import os

load_dotenv()
sqlite_url= os.getenv("sqlite_file_name")
if sqlite_url is None:
    raise ValueError("La variable de entorno sqlite_file_name no esta definida")
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def create_cliente(cliente: UserMain, session: SessionDep) -> UserMain:
    try:
    
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        return cliente
    except:
        session.rollback() #desace los cambios en caso de error
        raise ValueError("Error al crear el usuario")
