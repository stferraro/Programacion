class Pelicula:
    
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    def __str__(self):
        return f'Pelicula: {self._nombre}'