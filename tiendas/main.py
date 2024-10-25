from fastapi import FastAPI
from .tienda_model import Tienda
from .tienda_router import router as Tiendas 
from .consumer import consume_queue
import asyncio

app = FastAPI()
app.include_router(Tiendas)


@app.get("/")
async def root():
    return {"Bienvenida": "Lista de Tiendas"}


@app.on_event("startup")
def startup_event():
    Tienda.create_inventory_db()
    asyncio.create_task(consume_queue())