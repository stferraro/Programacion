from pelicula import Pelicula


class Tienda:
    def __init__(self, peliculas):
        self._peliculas = peliculas

    @property
    def peliculas(self):
        return self._peliculas

    @peliculas.setter
    def peliculas(self, value):
        self._peliculas = value
        
    def agregar_pelicula(self, pelicula):
        self._peliculas.append(pelicula)

        
    def __str__(self) -> str:
        peliculas_str = '\n'.join(pelicula.__str__() for pelicula in self._peliculas)
        return f'Peliculas: \n{peliculas_str}'
    
    
tienda = Tienda([])
pelicula = Pelicula("Pelicula 1", "Genero 1", 1)
pelicula2 = Pelicula("Pelicula 2", "Genero 2", 2)
tienda.agregar_pelicula(pelicula)
tienda.agregar_pelicula(pelicula2)
print(tienda)