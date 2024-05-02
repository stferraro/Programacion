class Triangulo:


    def __init__(self,base,altura):
        self.base = base
        self.altura = altura


    
    def area(self):
        return self.base*self.altura/2
    

base = 5
altura = 4
triangulo = Triangulo(base, altura)
c = triangulo.area()
print(c)