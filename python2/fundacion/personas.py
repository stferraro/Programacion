class Persona:
    def __init__(self, nombre,apellido, cedula, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._edad = edad

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
        
    def __str__(self):
        return f"{self._nombre} {self._apellido} {self._cedula} {self._edad}"

        

  