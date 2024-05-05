class Libro:
    
    def __init__(self, nombre, codigo, genero):
        self._nombre = nombre
        self._codigo = codigo
        self._genero = genero

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value
    
    def __str__(self):
        return f"Nombre: {self._nombre} Codigo: {self._codigo} Genero: {self._genero}"

        
        