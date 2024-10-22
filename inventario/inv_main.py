from fastapi import FastAPI
from inventario.models.inv_model import Inventario
from inventario.routers.inv_router import router as inventario

app = FastAPI()
app.include_router(inventario)


@app.get("/")
async def root():
    return {"Inventario": "Inventario"}




@app.on_event("startup")
def startup_event():
    Inventario.create_inventory_db()