from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def product_root():
    mensaje = {"saludo": "Productos"}
    return mensaje["saludo"]


