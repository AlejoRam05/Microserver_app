from fastapi import FastAPI
from User.models.user_model import DatabaseUser
app = FastAPI()

@app.get("/")
async def root():
    saludo = {"mensaje": "Hola Penguin"}
    return saludo["mensaje"]

# uvicorn main:app --reload

@app.get("/login")
async def user():
    pass
   
@app.on_event("startup")
def startup_event():
    DatabaseUser.create_db()