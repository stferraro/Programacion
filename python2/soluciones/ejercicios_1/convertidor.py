class Convertidor:
    
    def __init__(self, tasa, bs):
        self._tasa = tasa
        self._bs = bs

    @property
    def tasa(self):
        return self._tasa

    @tasa.setter
    def tasa(self, value):
        self._tasa = value

    @property
    def bs(self):
        return self._bs

    @bs.setter
    def bs(self, value):
        self._bs = value
        
    def get_conversion(self):
        try:
            return self._bs / self._tasa
        except ZeroDivisionError:
            print("la tasa no puede ser 0")
    
    def __str__(self):
        return f" el total de Bs: {self._bs} a convertir es igual a {self.get_conversion():.2f} USD"
    
    def crear_txt(self):
        try:
            archivo = open("conversion.txt", "w")
            archivo.write(self.__str__())
            archivo.close()
        except FileNotFoundError:
            print("el archivo no existe")
            
    def crear_txt2(self):
        try:
            with open("conversion2.txt", "w") as archivo:
                archivo.write(self.__str__())
        except FileNotFoundError:
            print("el archivo no existe")
            
    def leer_txt(self):
        lista = []
        try:
            archivo = open("datos.txt", "r")
            lista = list(archivo.readlines())
            archivo.close()
        except FileNotFoundError:
            print("el archivo no existe")
        return lista

bs = float(input("ingrese el valor a convertir: "))
tasa = float(input("ingrese la tasa del dolar: "))
convertidor = Convertidor(tasa, bs)
print(convertidor)
convertidor.crear_txt()
convertidor.crear_txt2()
lista = convertidor.leer_txt()
if lista:
    print(lista)
    tasa1 = float(lista[0])
    bs1 = float(lista[1])
    convertidor1 = Convertidor(bs1, tasa1)
else:
    print("el archivo esta vacio")

print(convertidor1)
