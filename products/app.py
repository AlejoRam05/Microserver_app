from fastapi import FastAPI
from .product_model import ProductsDB
from .product_router import product_router as productos
import pybreaker
import yaml


app = FastAPI()

app.include_router(productos)

with open("/home/penguin/Documentos/Microserver_app/product.yaml", "r") as file:
    custom_openapi_schema = yaml.safe_load(file)

@app.get("/openapi.json")
async def openapi():
    return custom_openapi_schema

@app.get("/")
async def product_root():
    mensaje = {"saludo": "Productos"}
    return mensaje["saludo"]

@app.on_event("startup")
async def startup_event():
    try:
        ProductsDB.create_product_db()
        print("Base de datos creada exitosamente.")
    except pybreaker.CircuitBreakerError:
        print("Circuit Breaker activado. Evitando nuevas conexiones a la base de datos.")

