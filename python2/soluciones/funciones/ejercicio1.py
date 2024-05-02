from funciones import *

def pedir_datos():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cedula = input("Cedula: ")
    salarioMensual = float(input("Salario mensual: "))
    lista = [nombre, apellido, cedula, salarioMensual]
    return lista

def utilidad(salarioMensual):
    salarioDiario = (salarioMensual / 30)
    return 30 * (salarioDiario)

def vacaciones(salarioMensual):
    return 15/12 * 4 * salarioMensual

def total(*datos):
    suma = 0
    for i in datos:
        suma += i
    if suma > 1000:
        bono = suma * 0.1
        total = suma + bono
    return total

if __name__ == '__main__':
    datos = pedir_datos()
    salarioMensual = float(datos[3])
    utilidad = utilidad(salarioMensual)
    vacaciones = vacaciones(salarioMensual)
    print(f'El trabajador {datos[0]} {datos[1]} de la cedula {datos[2]} tiene una utilidad de {utilidad:.2f} y vacaciones de {vacaciones:.2f}')
    total = total(utilidad, vacaciones)
    print(total)


