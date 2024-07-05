import funciones as fn

def convierte_en_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def pedir_celsius():
    lista = []
    while True:
        celsius = float(input("Ingresa la temperatura en grados celsius: "))
        if celsius == 1000:
            break
        else:
            lista.append(celsius)
    return lista

if __name__ == '__main__':
    localidad = input("Ingresa la localidad: ")
    lista = pedir_celsius()
    max = fn.mayor(*lista)
    min = fn.menor(*lista)
    prom = fn.promedio(*lista)
    listaValores = [max, min, prom]
    print(listaValores)
    maxFah = convierte_en_fahrenheit(max)
    minFah = convierte_en_fahrenheit(min)
    promFah = convierte_en_fahrenheit(prom)
    print(f'La localidad {localidad} tiene el maximo {maxFah}°F y el minimo {minFah}°F con un promedio de {promFah:.2f}°F')
