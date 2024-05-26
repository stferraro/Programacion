from estudiante import Estudiante

class Universidad:
    
    def __init__(self, estudiantes):
        self._estudiantes = estudiantes

    @property
    def estudiantes(self):
        return self._estudiantes

    @estudiantes.setter
    def estudiantes(self, value):
        self._estudiantes = value
        
    def agregar_estudiante(self, estudiante):
        self._estudiantes.append(estudiante)
        
    def __str__(self):
        estudiantes_str = '\n'.join([estudiante.__str__() for estudiante in self._estudiantes])
        return f"Estudiantes: \n{estudiantes_str}"
    
    def crear_txt(self):
        try:
            with open("universidad.txt", "w") as f:
                f.write(self.__str__())
        except FileNotFoundError as fn:
            print(fn)
            print("Error al crear el archivo")
            
universidad = Universidad([])

estudiante = Estudiante(1234, "Juan", "Perez", 123456789)
estudiante2 = Estudiante(5678, "Pedro", "Lopez", 987654321)
estudiante3 = Estudiante(9012, "Maria", "Garcia", 456789123)

universidad.agregar_estudiante(estudiante)
universidad.agregar_estudiante(estudiante2)
universidad.agregar_estudiante(estudiante3)

universidad.crear_txt()
print(universidad)
