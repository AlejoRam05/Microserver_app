"""Creación de la base de datos para el inventario"""
from dotenv import load_dotenv
import os
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy import text


# Cargar variables de entorno
load_dotenv()
sqlite_file_name = os.getenv("sqlite_file_name_inv")
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    """Genera una sesión de la base de datos."""
    with Session(engine) as session:
        yield session

class Inventario:
    @staticmethod
    def create_inventory_db():
        """Crea la base de datos y las tablas para el inventario."""
        SQLModel.metadata.create_all(engine)
        try:
            with Session(engine) as session:
                tables = session.exec(text("SELECT name FROM sqlite_master WHERE type='table';")).all()
                print("Tablas creadas:", tables)
        except Exception as e:
            print("Error al interactuar con la base de datos", e)
