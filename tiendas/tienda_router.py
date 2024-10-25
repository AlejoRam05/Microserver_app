from fastapi import APIRouter, Depends, HTTPException
from .tienda_model import get_session  #conexion a la base de datos
from .tienda_schemas import TiendaDB, TiendaBase
from sqlmodel import Session
from typing import Annotated
import httpx

SessionDep = Annotated[Session, Depends(get_session)] 

router = APIRouter(prefix="/tiendas", tags=["tiendas"])


@router.get("/")
async def obtener_invetario(session: SessionDep):
    tienda = session.query(TiendaDB).all()
    return tienda
    
@router.post("/add", response_model=TiendaBase)
async def agregar_tienda(tienda: TiendaBase, session: SessionDep):
    db_tienda = TiendaDB(**tienda.dict())
    session.add(db_tienda)
    session.commit()
    session.refresh(db_tienda)
    return db_tienda

@router.get("/{tienda_id}", response_model=TiendaBase)
async def obtener_tienda(tienda_id: int, session: SessionDep):
    tienda = session.get(TiendaDB, tienda_id)
    if not tienda:
        return {"error": "Tienda no encontrada"}
    return tienda

url_product = "http://127.0.0.1:8000/product/"
@router.get("/product/{id}")
async def get_product(id: int):
    async with httpx.AsyncClient() as client:
        try:
            # Request product from the Product service
            response = await client.get(f"{url_product}{id}")
            
            # Raise HTTP exception if the response status is not 200 OK
            response.raise_for_status()
            
            # Return the response data from the Product service
            return response.json()

        except httpx.RequestError as exc:
            # Connection errors
            raise HTTPException(status_code=503, detail=f"Connection error with Product service: {exc}")
        except httpx.HTTPStatusError as exc:
            # If the Product service returns a non-200 status code
            raise HTTPException(status_code=exc.response.status_code, detail=f"Product service error: {exc.response.text}")
        except Exception as e:
            # General exceptions
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")