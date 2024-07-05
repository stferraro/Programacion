"""

simula el funcionamiento de una calculadora realizando las cuatro operaciones aritmeticas basicas


"""

num1 = float(input("numero1: "))
num2 = float(input("numero2: "))

operacion = input("ingresa la operacion que quieres realizar: --> ").upper()

if (operacion == "S") :
    resultado = num1 + num2
    print (f"\n{resultado:.2f}")
elif (operacion == "R") :
    resultado = num1 - num2
    print (f"\n{resultado:.2f}")
elif (operacion == "P") or (operacion == "M"):
    resultado = num1 * num2
    print (f"\n{resultado:.2f}")
elif (operacion == "D") :
     resultado = num1 / num2
     print (f"\n{resultado:.2f}")
else :
    print ("se equivoco de operacion")
     
    