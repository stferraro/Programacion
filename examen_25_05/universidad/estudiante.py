class Estudiante:
    
    def __init__(self, codigo, nombre, apellido, cedula):
        self._codigo = codigo
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

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
        
    def __str__(self):
        return f"Código: {self._codigo}, Nombre: {self._nombre}, Apellido: {self._apellido}, Cedula: {self._cedula}"

        
    