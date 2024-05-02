def mayor (*numeros):
    mayor = float('-inf')
    for num in numeros:
        if num > mayor:
            mayor = num
    return mayor

def menor (*numeros):
    menor = float('inf')
    for num in numeros:
        if num < menor:
            menor = num
    return menor

def suma (*numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma

def promedio (*numeros):
    sum = suma
    for num in numeros:
        suma += num
    return suma / len(numeros)