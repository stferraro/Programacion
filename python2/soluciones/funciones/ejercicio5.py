import funciones as fn

vehiculos = {}

def pedirDatos():
    while True:
        modelo = input("Ingresa el modelo(n para cerrar): ")
        if modelo == "n":
            print(vehiculos)
            break
        else:
            costo = float(input("Ingresa el costo: "))
            vehiculos[modelo] = costo
            print(vehiculos)

if __name__ == '__main__':
    pedirDatos()
    max = fn.mayor(*vehiculos.values())
    claveMax = list(vehiculos.keys())[list(vehiculos.values()).index(max)]
    min = fn.menor(*vehiculos.values())
    claveMin = list(vehiculos.keys())[list(vehiculos.values()).index(min)]
    suma = fn.suma(*vehiculos.values())
    print(f'el vehiculo con valor maximo es {claveMax}: {max}')
    print(f'el vehiculo con valor minimo es {claveMin}: {min}')
    print(f'la suma de todos los valores es {suma}')
    listaValores = [max, min, suma]

