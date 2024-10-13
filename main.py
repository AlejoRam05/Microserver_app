from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, create_engine
from typing import List
from User.models.user_model import DatabaseUser, UserMain, create_cliente, read_clientes
from dotenv import load_dotenv
import os 

app = FastAPI()
load_dotenv()
sqlite_file_name = os.getenv("sqlite_file_name")
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
async def root():
    return {"mensaje": "Hola Penguin"}

@app.post("/login")
async def incluir_user(user: UserMain, session: Session = Depends(get_session)):
    new_user = await create_cliente(user, session)
    return new_user

@app.get("/login", response_model=List[UserMain])
async def lista_user(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    lista_usuarios = await read_clientes(session, offset, limit)
    return lista_usuarios

@app.get("/login/{id}")
async def ver_usuario(id: int, session: Session = Depends(get_session)):
    usuario = session.get(UserMain, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return usuario

@app.on_event("startup")
def startup_event():
    DatabaseUser.create_db()
