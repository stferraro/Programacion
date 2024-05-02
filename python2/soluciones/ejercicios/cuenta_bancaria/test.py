from cuenta_bancaria import CuentaBancaria
from persona import Persona


def menu(opcion):
    print("BIENVENIDO AL SISTEMA DEL BANCO")
    print("1. AGREGAR Cuenta")
    print("2. Listar Cuentas")
    print("3. Depositar Saldo")
    print("4. Retirar Saldo")
    print("5. Eliminar Cuenta")
    print("0. SALIR")
    print("".center(50, "*"))
    return opcion

def ejecutaOperacion(opcion):
    listaCuentas = []
    while opcion != 0:
        opcion = menu(opcion)
        if opcion < 0 or opcion > 5:
            print("Opcion no valida")
            print("".center(50, "*"))
            opcion = int(input("Ingrese una opcion: "))
            opcion = menu(opcion)
        elif opcion == 1:
            nombre = input("Ingrese el nombre de la persona: ")
            apellido = input("Ingrese el apellido de la persona: ")
            cedula = input("Ingrese la cedula de la persona: ")
            persona = Persona(nombre, apellido, cedula, listaCuentas)
            numero_cuenta = input("Ingrese el numero de cuenta: ")
            tipo_cuenta = input("Ingrese el tipo de cuenta: ")
            saldo = float(input("Ingrese el saldo de la cuenta: "))
            cuenta = CuentaBancaria(numero_cuenta, tipo_cuenta, saldo)
            persona.agregar_cuenta(cuenta)
            print("Cuenta agregada")
            print("".center(50, "*"))
            print(persona)
            opcion = int(input("Ingrese una opcion: "))
            opcion = menu(opcion)
        elif opcion == 2:
            persona.listar_cuentas()
            print("".center(50, "*"))
            opcion = int(input("Ingrese una opcion: "))
            opcion = menu(opcion)
        elif opcion == 3:
            numero_cuenta = input("Ingrese el numero de cuenta: ")
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            persona.depositar_saldo(numero_cuenta, cantidad)
            print("Cuenta depositada")
            print("".center(50, "*"))
            opcion = int(input("Ingrese una opcion: "))
            opcion = menu(opcion)
        elif opcion == 4:
            numero_cuenta = input("Ingrese el numero de cuenta: ")
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            persona.retirar_saldo1(numero_cuenta, cantidad)
            print("Cuenta retirada")
            print("".center(50, "*"))
            opcion = int(input("Ingrese una opcion: "))
            
            
            
if __name__ == "__main__":
    opcion = 1
    ejecutaOperacion(opcion)
    