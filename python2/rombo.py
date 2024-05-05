import math


class Rombo:
    
    def __init__(self, diagMay, diagMen):
        self._diagMay = diagMay
        self._diagMen = diagMen

    @property
    def diagMay(self):
        return self._diagMay

    @diagMay.setter
    def diagMay(self, value):
        self._diagMay = value

    @property
    def diagMen(self):
        return self._diagMen

    @diagMen.setter
    def diagMen(self, value):
        self._diagMen = value
        
    def calcula_lado(self):
        return math.sqrt(self._diagMay**2 + self._diagMen**2)/2
    
    def calcula_area(self):
        return (self.diagMay * self.diagMen) / 2
    
    def calcula_perimetro(self):
        return self.calcula_lado() * 4
    
    def __str__(self):
        return f"Diagonal mayor: {self._diagMay}\nDiagonal menor: {self._diagMen}\nLado: {self.calcula_lado():.2f}\nArea: {self.calcula_area():.2f}\nPerimetro: {self.calcula_perimetro():.2f}"
    
rombo = Rombo(2, 3)
rombo2 = Rombo(6,7)

print(rombo)
print(rombo2)

        
    