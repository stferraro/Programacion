'''Es necesario desarrollar una aplicación en Python que realice las siguientes
operaciones Pida al usuario ingresar la temperatura máxima del día y la temperatura
mínima , determine la temperatura media del día y además la convierte en Fareneheit y
las imprima en pantalla sin valores decimales.'''

temperaturaMaxima = float(input("Temperatura maxima del dia: "))
temperaturaMinima = float(input("Temperatura minima del dia: "))
temperaturaMedia = (temperaturaMaxima + temperaturaMinima) / 2

tF = ((temperaturaMedia * 9) / 5) + 32

print(f"la temperatura en grados farenheit es de : {tF:.2f}")