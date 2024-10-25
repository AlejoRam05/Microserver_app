from dotenv import load_dotenv
import os
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy import text
from contextlib import contextmanager
from .tienda_schemas import TiendaDB # Importar el modelo correctamente

# Cargar variables de entorno
load_dotenv()
sqlite_file_name = os.getenv("sqlite_file_name_tiendas")
if not sqlite_file_name:
    raise ValueError("El nombre del archivo SQLite no está configurado correctamente en el archivo .env.")
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
conn_inv = engine.connect()


def get_session():
    """Genera una sesión de la base de datos."""
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


class Tienda:
    @staticmethod
    def create_inventory_db():
        """Crea la base de datos y las tablas para el inventario."""
        try:
            # Asegurarse de que el modelo TiendaDB está registrado
            SQLModel.metadata.create_all(engine)
            
            # Verificar qué tablas fueron creadas
            with Session(engine) as session:
                tables = session.exec(text("SELECT name FROM sqlite_master WHERE type='table';")).all()
                print("Tablas creadas:", tables)
        
        except Exception as e:
            # Imprimir el error detallado
            print("Error al interactuar con la base de datos:", e)
            raise
