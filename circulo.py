'''Es necesario desarrollar una aplicación en Python que permita calcular el área y el
perimetro de una circunferencia dado el valor del radio'''

import math

radio = float(input("Radio de la circuferencia: "))

p = 2 * math.pi * radio
a = math.pi * pow(radio, 2)

print (f"La circuferencia de radio: {radio} tiene area: {a:.2f} y perimetro: {p:.2f}")