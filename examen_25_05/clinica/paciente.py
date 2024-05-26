class Paciente:
    
    def __init__(self, nombre, apellido, cedula, enfermedad, costo_consulta):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.enfermedad = enfermedad
        self.costo_consulta = costo_consulta

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, value):
        self.apellido = value

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, value):
        self.cedula = value

    def get_enfermedad(self):
        return self.enfermedad

    def set_enfermedad(self, value):
        self.enfermedad = value

    def get_costo_consulta(self):
        return self.costo_consulta

    def set_costo_consulta(self, value):
        self.costo_consulta = value
        
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Cedula: {self.cedula}, Enfermedad: {self.enfermedad}, Costo de la consulta: {self.costo_consulta}"

        
    