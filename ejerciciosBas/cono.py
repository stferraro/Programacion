import math

radio = float(input("Valor del radio: "))
altura = float(input("Altura del cono: "))

g = math.sqrt(radio**2+altura**2)

areaCono = math.pi * radio * (radio + g)
volumenCono = (math.pi * radio**2 * altura) / 3

print(f"{areaCono: .2f}, {volumenCono: .2f}")