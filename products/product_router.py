from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from .product_model import get_session
from .product_schemas import ProductDB, Product
from .producer import send_message_to_queue
from sqlmodel import Session
import pybreaker



product_router = APIRouter(prefix="/product", tags=["Products"])
SessionDep = Annotated[Session, Depends(get_session)]


class FormularioBreaker:

    def __init__(self, fail_max = 3, reset_timeout=10):
        self.breaker = pybreaker.CircuitBreaker(fail_max=fail_max, reset_timeout=reset_timeout)


    def obtener_inventario(self, session: Session):
        try:
            return self.breaker.call(self._get_producto_data, session)
        except:
            return HTTPException(status_code=503, detail=" Servicio no disponible")
        
    def _get_producto_data(self, session: Session):
        return session.query(ProductDB).all()

breaker_form = FormularioBreaker()

@product_router.get("/")
async def search_product(session: Session = Depends(get_session)):
    productos = breaker_form.obtener_inventario(session)
    return productos


@product_router.post("/add", response_model=Product)
async def add_products(producto: Product, session: SessionDep):
    db_productos = ProductDB(**producto.dict())
    session.add(db_productos)
    session.commit()
    session.refresh(db_productos)
    
    # Send product update message to RabbitMQ
    await send_message_to_queue(f"Product added: {db_productos.name_product}")
    
    return db_productos
    
@product_router.get("/{id}", response_model=Product)
async def obtener_producto(id: int, session: SessionDep):
    producto = session.get(ProductDB, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Product not found")
    return producto