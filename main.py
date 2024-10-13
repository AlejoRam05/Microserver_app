from fastapi import FastAPI
from User.routers.user_routers import router as user_router
from User.models.user_model import DatabaseUser

app = FastAPI()

# Incluir el router desde el archivo user_routers.py
app.include_router(user_router)

@app.on_event("startup")
def startup_event():
    DatabaseUser.create_db()
