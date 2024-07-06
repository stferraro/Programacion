import math

def area_circulo(radio):
    return math.pi * radio**2   


def volumen_cilindro(radio, altura):
    return area_circulo(radio) * math.pi * radio * altura


radio = float(input("Radio: "))
altura = float(input("Altura: "))
area_circulo = area_circulo(radio)
volumen_cilindro = volumen_cilindro(radio, altura)
print(f"Area del circulo: {area_circulo:.2f} -- volumen del cilindro: {volumen_cilindro:.2f}")    