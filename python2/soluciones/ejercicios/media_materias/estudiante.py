from materia import *


class Estudiante:
    
    def __init__(self, nombre, apellido, cedula, matricula, materias):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._matricula = matricula
        self._materias = materias

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def cedula(self):
        return self._cedula
    
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        self._matricula = value

    @property
    def materias(self):
        return self._materias

    @materias.setter
    def materias(self, value):
        self._materias = value
        
    def agrega_materia(self, materia):
        self._materias.append(materia)
        
    def eliminar_materia(self, materia):
        self._materias.remove(materia)
        
    def calcular_promedio(self):
        suma = 0
        for materia in self._materias:
            suma += materia.nota
        return suma / len(self._materias) 
    
    def __str__(self) -> str:
        materias_str = ""
        for materia in self._materias:
            materias_str += materia.__str__() + "\n"
        return f"Estudiante: {self._nombre} {self.apellido} Cedula: {self._cedula} Matricula: {self._matricula} \nmaterias:\n{materias_str}"


estudiante = Estudiante("Juan", "Perez", 123456, 12345, [])
print(estudiante)
materias = []
materia1 = Materia("Matematicas", 10, 3)
materia2 = Materia("Fisica", 9, 3)
materia3 = Materia("Fisica", 9, 5)
estudiante.agrega_materia(materia1)
estudiante.agrega_materia(materia2)
estudiante.agrega_materia(materia3)
promedio = estudiante.calcular_promedio()
print(f'Promedio: {promedio:.2f}')
print(estudiante)