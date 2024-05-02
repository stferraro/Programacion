class Materia:
    
    def __init__(self, nombre, nota, creditos):
        self._nombre = nombre
        self._nota = nota
        self._creditos = creditos

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, value):
        self._nota = value

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, value):
        self._creditos = value

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, value):
        self._nota = value

        
    def __str__(self) -> str:
        return f"nombre: {self._nombre} Nota: {self._nota} Creditos: {self._creditos}"
    
materia1 = Materia("Matematicas", 10, 3)
materia2 = Materia("Fisica", 9, 3)
materia3 = Materia("Quimica", 9, 5)
print(materia1)
print(materia2)
print(materia3)