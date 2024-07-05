
saldoInicial = 1000

print ("Ingresa la operacion a realizar :")
print ("1. Ingresar dinero a la cuenta ")
print ("2. Retirar dinero de la cuenta ")
print ("3. Mostrar dinero disponible en la cuenta ")
print ("4. Salir")

operacion = int(input ("introduce la operacion: --> "))

if (operacion == 1) :
    resultado = float(input("Que cantidad de dinero vas a ingresar: --> "))
    resultado += saldoInicial
    print(f"{resultado:.2f}")
elif (operacion == 2) :
    saldo = float (input ("Cuanto dinero vas a Sacar: --> "))
    if (saldo > saldoInicial) :
        print("El saldo que quieres retirar es mayor a lo disponible no puedes realizar la operacion")
    else :
        resultado = saldoInicial - saldo
        print(f"{resultado:.2f}")
elif (operacion == 3) :
    print(f"{saldoInicial:.2f}")
elif (operacion == 4) :
    print("Hasta luego")
else: 
    print ("operacion errada")