class Paciente:
    
    def __init__ (self, nombre, apellido, cedula, edad, patologia):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._edad = edad
        self._patologia = patologia

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
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    @property
    def patologia(self):
        return self._patologia

    @patologia.setter
    def patologia(self, value):
        self._patologia = value
        
    def get_costo (self):
        costo = 0
        if self._edad >= 0 and self._edad <= 18:
            costo = 5
        elif self._edad >= 19 and self._edad <= 40:
            costo = 10
        else:
            costo = 15
        return costo
    
    def __str__(self):
        return f"Nombre: {self._nombre}\nApellido: {self._apellido}\nCedula: {self._cedula}\nEdad: {self._edad}\nPatologia: {self._patologia}\nCosto: {self.get_costo()}" 
