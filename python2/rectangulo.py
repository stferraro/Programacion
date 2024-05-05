class Rectangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    def area(self):
        return self._base * self._altura
    
    def perimetro(self):
        return 2 * (self._base + self._altura)
    
    def __str__(self):
        return f'Rectangulo de base: {self._base} cm y altura: {self._altura} cm tiene un area de {self.area()} cm² y un perimetro de {self.perimetro()} cm'
    
    
rectangulo = Rectangulo(10, 5)
print(rectangulo)