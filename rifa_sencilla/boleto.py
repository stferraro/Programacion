import random

class Boleto:
    def __init__(self, price):
        self._number = self.generate_number()
        self._price = price

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._numbers = value
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        try :
            if value < 0:
                raise ValueError
            self._price = value
        except ValueError:
            return "El valor no es válido"
        
    def generate_number(self):
        while True:
            value = random.choice(range(1, 101))
            if value not in Boleto.numbers:
                Boleto.numbers.add(value)
                return value
                
    def __str__(self):
        return f"Boleto: {self._number}, Precio: {self._price}"
    