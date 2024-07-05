import math


class Cilindro:
    
    def __init__(self, diametro, altura):
        self._diametro = diametro
        self._altura = altura

    @property
    def diametro(self):
        return self._diametro

    @diametro.setter
    def diametro(self, value):
        self._diametro = value

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, value):
        self._altura = value
        
    def calcula_radio(self):
        return self._diametro / 2
    
    def calcula_area(self):
        return 2 * (math.pi * self.calcula_radio() ** 2) + (2 * math.pi * self.calcula_radio() * self._altura) 
    
    def calcula_volumen(self):
        return math.pi * self.calcula_radio()**2 * self._altura
    
    def __str__(self) -> str:
        str1 = f'El cilindro de diametro: {self._diametro} cm y altura: {self._altura} cm tiene:\n'
        resultados = [
            f'Area: {self.calcula_area():.2f} cm²',
            f'Volumen: {self.calcula_volumen():.2f} cm³'
            ]
        str1 += '\n'.join(resultados)
        return str1

        

cilindro = Cilindro(38, 22)
print(cilindro)
    