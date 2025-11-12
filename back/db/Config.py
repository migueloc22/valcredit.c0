from sqlalchemy import create_engine ## create_engine es para crear la conexion a la base de datos
from sqlalchemy.ext.declarative import declarative_base # declarative_base es para crear las clases base de los modelos
from sqlalchemy.orm import sessionmaker # sessionmaker es para crear la sesion de la base de datos

import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL:", DATABASE_URL)  # Depuración

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL no está definida. Verifica tu archivo .env.")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# class Settings:
#     def __init__(self):
#         self.database_url = os.getenv("DATABASE_URL")