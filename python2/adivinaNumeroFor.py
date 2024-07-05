import random

nombre = input ("Ingresa tu nomre --> : ")
print (f"Bienvenido {nombre} al juego de adivina el numero")

numero = random.randint(1, 100)
numeroJugada = int(input("Ingresa un valor entero entre 1 y 100 : --> "))

for i in range (numeroJugada) :
    
    numeroJugada == numero
    
    if (numeroJugada < numero) :
        
        numeroJugada = int(input("has ingresado un valor muy bajo prueba con un numero mas alto: --> "))
        
    elif (numeroJugada > numero):
        
        numeroJugada = int(input("has ingresado un valor muy alto prueba con un numero mas bajo: --> "))
        
print(f"Adivinaste el numero {numero}")