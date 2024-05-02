class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "No se puede dividir entre 0"

    def __str__(self) -> str:
        return f"suma: {self.sumar()}\nresta: {self.restar()}\nmultiplicacion: {self.multiplicar()}\ndivision: {self.dividir()}"
    
    

calculadora = Calculadora(10, 5)
print(calculadora)
calculadora2 = Calculadora(10, 0)
print(calculadora2)
    
    