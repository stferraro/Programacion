import funciones as fn

lista = []

if __name__ == '__main__':
    while True:
        numero = float(input("Ingresa un numero: "))
        
        if numero < 0:
            print('hasta luego')
            print(f'maximo {max}')
            print(f'minimo {min}')
            print(f'promedio {prom:.2f}')
            print(f'suma {suma}')
            print(f'{lista}')
            break
        else:
            lista.append(numero)
            max = fn.mayor(*lista)
            min = fn.menor(*lista)
            prom = fn.promedio(*lista)
            suma = fn.suma(*lista)