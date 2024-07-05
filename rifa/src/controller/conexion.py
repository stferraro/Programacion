# Importamos las bibliotecas necesarias
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Cargamos las variables de entorno desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'config', '.env')
load_dotenv(dotenv_path)

# Obtenemos las variables de entorno para la configuración de la base de datos
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Creamos la cadena de conexión a la base de datos
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Creamos el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creamos la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creamos la base para las clases del modelo
Base = declarative_base()

class Conexion:
    @staticmethod
    def obtener_sesion():
        return SessionLocal()


try:
    conexion = Conexion()
    session = conexion.obtener_sesion()
    print("Conexión exitosa")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
    
