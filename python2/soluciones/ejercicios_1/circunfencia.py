import math


class Circuferencia:
    
    def __init__(self, diametro):
        self._diametro = diametro

    @property
    def diametro(self):
        return self._diametro

    @diametro.setter
    def diametro(self, value):
        self._diametro = value
        
    def get_radio(self):
        return self._diametro / 2
    
    def area(self):
        return math.pi * self.get_radio() ** 2
    
    def perimetro(self):
        return math.pi * self._diametro
    
    def __str__(self):
        return f"El radio es {self.get_radio():.2f}, el area es {self.area():.2f} y el perimetro es {self.perimetro():.2f}"
    
    
    
    
diametro = float(input("ingrese el valor del diametro: "))
circuferencia = Circuferencia(diametro)
print(circuferencia)    
    
    
    
        
        