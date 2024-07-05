from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from controller.conexion import Base, Conexion
import random

class Boleto(Base):
    __tablename__ = "boletos"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, index=True, unique=True)
    precio = Column(Integer)
    propietario_id = Column(Integer, ForeignKey("personas.id"))

    propietario = relationship("Persona", back_populates="boletos")

    @classmethod
    def crear_boleto(cls, precio, propietario_id):
        sesion = Conexion.obtener_sesion()
        try:
            # Generar un número de boleto único
            numero = cls.generar_numero_unico(sesion)
            if numero is None:
                raise Exception("No se pudo generar un número de boleto único")

            # Crear el boleto con el número generado
            boleto = cls(numero=numero, precio=precio, propietario_id=propietario_id)
            sesion.add(boleto)
            sesion.commit()
            sesion.refresh(boleto)
            return boleto
        finally:
            sesion.close()

    @staticmethod
    def generar_numero_unico(sesion):
        numeros_existentes = [boleto.numero for boleto in sesion.query(Boleto).all()]
        numeros_disponibles = [numero for numero in range(1, 101) if numero not in numeros_existentes]
        if numeros_disponibles:
            return random.choice(numeros_disponibles)
        else:
            return None
