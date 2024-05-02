class Calculadora:
    
    def __init__(self, a ,b):
        self.__a = a 
        self.__b = b

    @property
    def _a(self):
        return self.__a

    @_a.setter
    def _a(self, value):
        self.__a = value

    @property
    def _b(self):
        return self.__b

    @_b.setter
    def _b(self, value):
        self.__b = value

        
    def suma(self,a ,b):
        return self.__a+ self.__b
    
    def resta (self, a ,b):
        return self.__a - self.__b
    
    def multiplicacion (self, a ,b):
        return self.__a * self.__b
    
    def division (self, a ,b):
        if self.__b == 0:
            return "No se puede dividir por 0"
        return self.__a / self.__b

a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))    
calculadora = Calculadora(a, b)
print(calculadora.suma(a, b))
print(calculadora.resta(a, b))
print(calculadora.multiplicacion(a, b))
print(calculadora.division(a, b))
    
    
    
        
    