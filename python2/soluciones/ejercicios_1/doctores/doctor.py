from paciente import Paciente

class Doctor:
    
    def __init__ (self, nombre, apellido, cedula, pacientes):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
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
    
    @property
    def pacientes(self):
        return self._pacientes

    @pacientes.setter
    def pacientes(self, value):
        self._pacientes = value
        
    def agregar_paciente(self, paciente):
        self._pacientes.append(paciente)
        
    def ganacia_total(self):
        return sum([p.get_costo() for p in self._pacientes])
        
    def __str__(self):
        pacientes_str = "\n".join(str(paciente) for paciente in self._pacientes)
        return f"Nombre: {self._nombre}\nApellido: {self._apellido}\nCedula: {self._cedula}\nPacientes: {pacientes_str} \nGanancia total: {self.ganacia_total():.2f}"
    
    def crear_txt(self):
        try:
            archivo = open("datos/doctor.txt", "w")
            archivo.write(self.__str__())
            archivo.close()
            print("se ha creado el archivo")
        except FileNotFoundError:
            print("el archivo no existe")
            
    def leer_txt(self):
        lista = []
        try:
            archivo = open("datos/doctor.txt", "r")
            lista = list(archivo.readlines())
            archivo.close()
        except FileNotFoundError:
            print("el archivo no existe")
        return lista
    
    def crear_txt2(self):
        try:
            with open("datos/doctor2.txt", "w") as archivo:
                archivo.write(self.__str__())
                print("se ha creado el archivo")
        except FileNotFoundError:
            print("el archivo no existe")
    
pac = Paciente("Juan", "Perez", "123456789", 25, "Cardiopatia")
paciente1 = Paciente("Maria", "Lopez", "123456789", 35, "Cancer")
paciente2 = Paciente("Pedro", "Gonzalez", "123456789", 45, "Diabetes")
paciente3 = Paciente("Ana", "Martinez", "123456789", 55, "Asma")
paciente4 = Paciente("Luis", "Ramirez", "123456789", 65, "Gripe")
paciente5 = Paciente("Sofia", "Hernandez", "123456789", 75, "Covid")
doctor = Doctor("Doctor", "Perez", "123456789", [])
doctor.agregar_paciente(pac)
doctor.agregar_paciente(paciente1)
doctor.agregar_paciente(paciente2)
doctor.agregar_paciente(paciente3)
doctor.agregar_paciente(paciente4)
doctor.agregar_paciente(paciente5)

print(doctor)
doctor.crear_txt()
doctor.crear_txt2()
