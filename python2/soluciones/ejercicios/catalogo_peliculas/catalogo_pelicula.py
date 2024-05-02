from pelicula import Pelicula

class CatalogoPeliculas:
    def __init__(self, peliculas):
        self._peliculas = peliculas

    @property
    def peliculas(self):
        return self._peliculas

    def agregar_pelicula(self, pelicula):
        self._peliculas.append(pelicula)
        
    def listar_peliculas(self):
        for pelicula in self._peliculas:
            print(pelicula)
            
    def eliminar_pelicula(self, pelicula):
        nombres_peliculas = [p.nombre for p in self._peliculas]
        if pelicula.nombre in nombres_peliculas:
            self._peliculas = [p for p in self._peliculas if p.nombre != pelicula.nombre]
            print("Película eliminada")
        else:
            print("La película no existe en el catálogo")
        
    def __str__(self):
        peliculas_str = ""
        for pelicula in self._peliculas:
            peliculas_str += pelicula.__str__() + "\n"
        return f'Peliculas: \n{peliculas_str}'
