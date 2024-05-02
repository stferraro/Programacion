class Triangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def _base(self):
        return self.__base

    @_base.setter
    def _base(self, value):
        self.__base = value

    @property
    def _altura(self):
        return self.__altura

    @_altura.setter
    def _altura(self, value):
        self.__altura = value


    def area(self):
        return (self.__base * self.__altura) / 2
    
    def perimetro(self):
        return self.__base * 3
    
    def __str__(self):
        return f'Base: {self._base} Altura: {self._altura} Area: {self.area()} Perimetro: {self.perimetro()}'
        
b = float(input("Ingresa la base: "))
h = float(input("Ingresa la altura: "))
triangulo = Triangulo(b, h)
print(triangulo)