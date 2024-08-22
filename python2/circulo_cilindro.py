import math

def area_circulo(radio):
    return math.pi * radio**2   


def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura


radio = float(input("Radio: "))
altura = float(input("Altura: "))
area_circ = area_circulo(radio)
volumen_cilin = volumen_cilindro(radio, altura)
print(f"Area del circulo: {area_circ:.2f} Volumen del cilindro: {volumen_cilin:.2f}")