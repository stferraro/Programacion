from materia import Materia


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

    @property
    def nombre(self, value):
        self._nombre = value

    @property
    def cedula(self):
        return self._cedula

    @property
    def apellido(self):
        return self._apellido

    @property
    def apellido(self, value):
        self._apellido = value

    @property
    def matricula(self):
        return self._matricula

    @property
    def materias(self):
        return self._materias
    
    def agregar_materia(self, materia):
        self._materias.append(materia)
        
    def calcular_promedio(self):
        suma = sum([materia.valor_materia() for materia in self._materias])
        total_creditos = sum([materia.creditos for materia in self._materias])
        return suma / total_creditos

    def __str__(self):
        estudiante_str = f"Estudiante: {self._nombre} {self._apellido} Cedula: {self._cedula} Matricula: {self._matricula}"
        materias_str = '\n'.join(materia.__str__() for materia in self._materias)
        return estudiante_str +'\n' + materias_str
    
estudiante = Estudiante("Juan", "Perez", 123456, 12345, [])
materias = []
for i in range(6):
    nombre_materia = input(f"Ingrese el nombre de la materia {i+1}: ")
    nota = float(input(f"Ingrese la nota de la materia {i+1}: "))
    while nota < 0 or nota > 20:
        nota = float(input("La nota no es válida. Ingrese una nota entre 0 y 20: "))
        if nota.isdigit(nota) or nota < 0 or nota > 0 and nota <= 20:
            break
    creditos = int(input(f"Ingrese los creditos de la materia {i+1}: "))
    materia = Materia(nombre_materia, nota, creditos)
    estudiante.agregar_materia(materia)

promedio = estudiante.calcular_promedio()
print(estudiante)
print(f'Promedio: {promedio:.2f}')
