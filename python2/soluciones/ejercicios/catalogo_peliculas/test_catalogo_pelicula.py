from catalogo_pelicula import CatalogoPeliculas
from pelicula import Pelicula

def menu(opcion):
    print("BIENVENIDO AL CATALOGO DE PELICULAS")
    print("1. AGREGAR PELICULA")
    print("2. LISTAR PELICULAS")
    print("3. ELIMINAR PELICULA")
    print("0. SALIR")
    print("".center(50, "*"))
    return opcion

def ejecutaOperaciones(opcion):
    listaPeliculas = []
    while opcion != 0:
        opcion = menu(opcion)
        if opcion < 0 or opcion > 3:
            print("Opcion no valida")
            print("".center(50, "*"))
            opcion = int(input("Ingrese una opcion: "))
            opcion = menu(opcion)
        elif opcion == 1:
            nombre = input("Ingrese el nombre de la pelicula: ")
            pelicula = Pelicula(nombre)
            catalogoPeliculas = CatalogoPeliculas(listaPeliculas)
            catalogoPeliculas.agregar_pelicula(pelicula)
            print("Pelicula agregada")
            print(catalogoPeliculas)
            opcion = int(input("Ingrese una opcion: "))
            opcion = menu(opcion)
        elif opcion == 2:
            catalogoPeliculas.listar_peliculas()
            print("".center(50, "*"))
            opcion = int(input("Ingrese una opcion: "))
            opcion = menu(opcion)
        elif opcion == 3:
            print(catalogoPeliculas)
            nombre = input("Ingrese el nombre de la pelicula: ")
            catalogoPeliculas.eliminar_pelicula(Pelicula(nombre))
            print("Pelicula eliminada")
            print(catalogoPeliculas)
            print("".center(50, "*"))
            opcion = int(input("Ingrese una opcion: "))
            opcion = menu(opcion)
    else: 
        print("GRACIAS POR UTILIZAR EL CATALOGO DE PELICULAS")
    
if __name__ == "__main__":
    opcion = int(input("Ingrese una opcion: "))
    ejecutaOperaciones(opcion)   