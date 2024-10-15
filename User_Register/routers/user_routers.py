from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, create_engine
from typing import List
from User_Register.models.user_model import UserMain, create_cliente, read_clientes
from dotenv import load_dotenv
import os

# Cargar variables de entorno una vez
load_dotenv()

# Configuración del router
router = APIRouter(prefix="/register", tags=["Usuarios"])

# Configuración de la base de datos
sqlite_file_name = os.getenv("sqlite_file_name")
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

# Dependencia para obtener la sesión
def get_session():
    with Session(engine) as session:
        yield session

# Rutas de API
@router.get("/star")
async def root():
    """Mensaje de bienvenida a la barbería."""
    return {"mensaje": "Bienvenido a la barbería"}

@router.post("/")
async def incluir_user(user: UserMain, session: Session = Depends(get_session)):
    """Incluir un nuevo usuario en la base de datos."""
    new_user = await create_cliente(user, session)
    return new_user

@router.get("/", response_model=List[UserMain])
async def lista_user(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    """Obtener una lista de usuarios con paginación."""
    lista_usuarios = await read_clientes(session, offset, limit)
    return lista_usuarios

@router.get("/{id}")
async def ver_usuario(id: int, session: Session = Depends(get_session)):
    """Ver los detalles de un usuario por su ID."""
    usuario = session.get(UserMain, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
