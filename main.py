from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    saludo = {"mensaje": "Hola Penguin"}
    return saludo["mensaje"]

# uvicorn main:app --reload