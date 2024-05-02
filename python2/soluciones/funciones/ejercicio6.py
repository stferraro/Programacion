import funciones as fn

def pedir_datos():
    nombre_cliente = input("Ingresa el nombre del cliente: ")
    apellido_cliente = input("Ingresa el apellido del cliente: ")
    cedula_cliente = input("Ingresa la cedula del cliente: ")
    lista = [nombre_cliente, apellido_cliente, cedula_cliente]
    return lista

def diccionarioProductos():
    diccionarioProductos = {}
    while True:
        nombre = input("Ingresa el nombre del producto(n para cerrar): ")
        if nombre == "n":
            print(diccionarioProductos)
            break
        else:
            valor = float(input("Ingresa el valor del producto: "))
            diccionarioProductos[nombre] = valor
            print(diccionarioProductos)
    return diccionarioProductos

def total(valor):
    descuento = 0
    if valor > 2500:
        descuento = valor * 0.20
    return valor - descuento

if __name__ == '__main__':
    diccionario = diccionarioProductos()
    max = fn.mayor(*diccionario.values())
    claveMax = list(diccionario.keys())[list(diccionario.values()).index(max)]
    min = fn.menor(*diccionario.values())
    claveMin = list(diccionario.keys())[list(diccionario.values()).index(min)]
    suma = fn.suma(*diccionario.values())
    totalF = total(suma)
    print(f'el proyecto con valor maximo es {claveMax}: {max}, el mas bajo es {claveMin}: {min} y la suma de todos es {suma}')
    print(f'el total es igual a {totalF:.2f}')