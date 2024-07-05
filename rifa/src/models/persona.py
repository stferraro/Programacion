from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from controller.conexion import Base, Conexion

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    cedula = Column(String, unique=True, index=True)
    correo = Column(String, index=True)
    num_pago = Column(String, unique=True, index=True)

    boletos = relationship("Boleto", back_populates="propietario")