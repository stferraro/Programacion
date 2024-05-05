class Pelicula:
    def __init__(self, nombre, genero, codigo):
        self._nombre = nombre
        self._genero = genero
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    def __str__(self):
        return f"Nombre: {self._nombre} Genero: {self._genero} Codigo: {self._codigo}"