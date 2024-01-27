'''Aplicacion en python que recibe en input nombre, apellido, peso y estatura y da como resultado el valor del indice de
masa corporea de la persona'''


nombre = input("Nombre:")
apellido = input("Apellido: ")
estatura = float(input("Estatura: "))
peso = float(input("Peso: "))

imc = peso/pow(estatura, 2)

print(f"el IMC de la persona: {nombre} {apellido} es de {imc:.2f}")
print("El IMC de la persona: {} {} es {:.2f}".format(nombre, apellido, imc))