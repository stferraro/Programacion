class PromedioNotas:
    def __init__(self, notas):
        self._notas = notas

    @property
    def notas(self):
        return self._notas

    @notas.setter
    def notas(self, value):
        self._notas = value
        
    def calcula_nota(self, nota):
        return (nota * 20) / 50
    
    def agregar_nota(self,nota):
        self.notas.append(nota)
    
    def promedio(self):
        suma = 0
        for nota in self.notas:
            suma += self.calcula_nota(nota)
        return suma / len(self.notas)

        
    def __str__(self) -> str:
        notas_str = ""
        for nota in self.notas:
            valor = self.calcula_nota(nota)
            notas_str += f' nota : {valor:.2f} '
        return f"Las notas son: {notas_str} y el promedio es: {self.promedio():.2f}"
    
    
    
sumaValor = 0
suma1 = 0
suma2 = 0

while sumaValor != 50:
    valor = float(input("Ingresa valor: "))
    nota1 = float(input("Ingresa nota1: "))
    
    sumaValor += valor
    
    suma1 += nota1
   
    if sumaValor == 50:
        break
    
sumaValor2 = 0
while sumaValor2 != 50:
    valor2 = int(input("Ingresa valor: "))
    sumaValor2 += valor2
    nota2 = float(input("Ingresa nota2: "))
    suma2 += nota2
    
    if sumaValor2 == 50:
        break

prom = PromedioNotas([suma1, suma2])
print(prom)
