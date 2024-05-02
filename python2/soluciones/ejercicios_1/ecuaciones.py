'''
Ecuaciones de segundo grado

del tipo ax^2 + bx + c = 0

soluciones reales

x1 = (-b + sqrt(b^2 - 4ac)) / 2a
x2 = (-b - sqrt(b^2 - 4ac)) / 2a

'''


import math


class Ecuacion:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def discriminante(self):
        return (self.b ** 2) - (4 * self.a * self.c)
    
    def raices(self):
        try:
            x1 =  ((-1 * self.b) + (math.sqrt(self.discriminante()))) / (2 * self.a)
            x2 =  ((-1 * self.b) - (math.sqrt(self.discriminante()))) / (2 * self.a)
            return x1, x2
        except ValueError:
            return "Raices no reales, no es posible realizar la raiz cuadrada de un numero negativo"
    
    def __str__(self) -> str:
        return f"La ecuacion {self.a}x^2 + {self.b}x + {self.c} = 0 tiene {self.discriminante()} como discriminante y las raices son: {self.raices()}"
    
    
    def crear_txt(self):
        try:
            archivo = open("ecuaciones.txt", "a")
            archivo.write(self.__str__())
            archivo.close()
            print("se ha creado el archivo")
        except FileNotFoundError:
            print("el archivo no existe")
            
    def crear_txt2(self):
        try:
            with open("ecuaciones2.txt", "a") as archivo:
                archivo.write(self.__str__())
        except FileNotFoundError:
            print("el archivo no existe")
            
    def leer_txt(self):
        lista = []
        try:
            archivo = open("ecuaciones.txt", "r")
            lista = list(archivo.readlines())
            archivo.close()
        except FileNotFoundError:
            print("el archivo no existe")
        return lista

ecuacion = Ecuacion(2, -3, 5)
print(ecuacion)
ecuacion2 = Ecuacion(1, 1, 1)
print(ecuacion2)
ecuacion3 = Ecuacion(1,3,-4)
print(ecuacion3)
ecuacion.crear_txt()
ecuacion2.crear_txt()
ecuacion3.crear_txt()
ecuacion.crear_txt2()



        
            
        