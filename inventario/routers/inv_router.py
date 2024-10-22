from fastapi import APIRouter, Depends
from inventario.models.inv_model import get_session  #conexion a la base de datos
from inventario.schemas.inv_schemas import InventoryDB
from sqlmodel import Session


router = APIRouter(prefix="/inventario", tags=["Inventario"])


@router.get("/")
async def obtener_invetario(session: Session = Depends(get_session)):
    inventario = session.query(InventoryDB).all()
    return inventario
    

