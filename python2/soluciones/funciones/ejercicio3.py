import funciones as fn

diccionario = {}

def descuento(valor):
    if valor > 150:
        descuento = valor * 0.15
    return valor - descuento

def pedir_datos():
    while True:
        producto = input("Ingresa el nombre del producto(n para cerrar): ")
        if producto == "n":
            print(f'el producto con valor mas alto es {claveMax}: {max}, el mas bajo es {claveMin}: {min} y la suma de todos es {suma}')
            print(f'el total es igual a:{total:.2f}')
            break
        else:
            valor = int(input("Ingresa el valor del producto: "))
            diccionario[producto] = valor
            print(diccionario)
            listaValores = list(diccionario.values())
            max = fn.mayor(*listaValores)
            claveMax = list(diccionario.keys())[listaValores.index(max)]
            min = fn.menor(*listaValores)
            claveMin = list(diccionario.keys())[listaValores.index(min)]
            suma = fn.suma(*listaValores)
            total = descuento(suma)

if __name__ == '__main__':
    pedir_datos()
