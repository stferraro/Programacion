#bucle while

import math

numero = int (input("digite un numero: "))

while numero < 0 :
    print("Error--> el numero tiene que ser positivo")
    numero = int (input("digite un numero: "))

print(f"raiz cuadrada {(math.sqrt(numero)):.2f}")