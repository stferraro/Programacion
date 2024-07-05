from models.boleto import Boleto

def probar_creacion_boleto():
    precio = 100  # Precio del boleto
    propietario_id = 1  # ID del propietario del boleto

    boleto = Boleto.crear_boleto(precio, propietario_id)
    print("Boleto creado exitosamente:", boleto)

if __name__ == "__main__":
    probar_creacion_boleto()
