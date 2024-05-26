from paciente import Paciente


class Doctor:
    
    def __init__(self, nombre, apellido, cedula, especialidad, pacientes):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._especialidad = especialidad
        self._pacientes = pacientes

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, value):
        self._especialidad = value

    @property
    def pacientes(self):
        return self._pacientes

    @pacientes.setter
    def pacientes(self, value):
        self._pacientes = value
        
    def agregar_paciente(self, paciente):
        self._pacientes.append(paciente)
        
    def total_consultas(self):
        return sum(paciente.costo_consulta for paciente in self._pacientes)
    
    def __str__(self):
        pacientes_str = '\n'.join([paciente.__str__() for paciente in self._pacientes])
        str = f"Nombre: {self._nombre}, Apellido: {self._apellido}, Cedula: {self._cedula}, Especialidad: {self._especialidad}, \nPacientes: \n{pacientes_str}"
        total = f'\nTotal de consultas: {self.total_consultas():.2f}'
        return "".join([str, total])
    
    def crear_txt(self):
        try:
            with open("clinica.txt", "w") as f:
                f.write(self.__str__())
        except FileNotFoundError as fn:
            print(fn)
            print("Error al crear el archivo")
            

            
doctor = Doctor("Julian", "Gonzalez", "123456789", "Cardiologo", [])

paciente = Paciente("Julian", "Gonzalez", "123456789", "Diabetes", 500)
paciente1 = Paciente("Filipo", "Gonzalez", "12332776", "Cancer", 1500)
paciente2 = Paciente("Javier", "Gonzalez", "1234523", "Fiebre", 1500)

doctor.agregar_paciente(paciente)
doctor.agregar_paciente(paciente1)
doctor.agregar_paciente(paciente2)

print(doctor)
doctor.crear_txt()

            
            

        
    