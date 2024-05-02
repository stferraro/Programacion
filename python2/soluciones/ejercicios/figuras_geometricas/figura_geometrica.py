class FiguraGeometrica:
    
    def __init__(self, lado):
        self._lado = lado
        
    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, valor):
        self._lado = valor
        
class Cuadrado(FiguraGeometrica):
    
    def __init__(self, lado):
        super().__init__(lado)
        
    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado * 4
    
    def __str__(self):
        return f"Cuadrado de lado {self.lado} tiene un area de {self.area()} y un perimetro de {self.perimetro()}"
    
class Triangulo(FiguraGeometrica):
    
    def __init__(self, lado):
        super().__init__(lado)
        
    def area(self):
        return (self.lado * self.lado) / 2
    
    def perimetro(self):
        return self.lado * 3
    
    def __str__(self):
        return f"Triangulo de lado {self.lado} y altura {self.lado} tiene un area de {self.area()} y un perimetro de {self.perimetro()}"
    
triangulo = Triangulo(10)
print(triangulo)
cuadrado = Cuadrado(10)
print(cuadrado)
  
    