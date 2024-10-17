from fastapi import FastAPI
from inventario.models.inv_model import Inventario

app = FastAPI()



@app.on_event("startup")
def startup_event():
    Inventario.create_inventory_db()