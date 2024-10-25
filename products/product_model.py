from dotenv import load_dotenv
import os
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy import text
from .product_schemas import ProductDB


load_dotenv()
sqlite_file_name = os.getenv("sqlite_file_name_prod")
if not sqlite_file_name:
    raise ValueError("El nombre del archivo SQLite no está configurado correctamente en el archivo .env.")
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
conn_inv = engine.connect()



def get_session():
    """Genera una sesión de la base de datos."""
    with Session(engine) as session:
        yield session

class ProductsDB:
    @staticmethod
    def create_product_db():
        """Crea la base de datos y las tablas para la lista de productos."""
        try:
            # Asegurarse de que el modelo ProductDB está registrado
            SQLModel.metadata.create_all(engine)
        
        except Exception as e:
            # Imprimir el error detallado fallar el circuit breaker
            print("Error al interactuar con la base de datos:", e)
            raise

