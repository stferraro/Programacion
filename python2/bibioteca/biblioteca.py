from libro import Libro

class Biblioteca:
    def __init__(self, libros):
        self._libros = libros

    @property
    def libros(self):
        return self._libros

    @libros.setter
    def libros(self, value):
        self._libros = value
        
    def agregar_libro(self, libro):
        self._libros.append(libro)
        
    def eliminar_libro(self, libro):
        self._libros.remove(libro)
        
    def __str__(self):
        libros_str = "\n".join(libro.__str__() for libro in self._libros)
        return f"Libros: \n{libros_str}"
    

libro1 = Libro("libro1", "codigo1", "genero1")
libro2 = Libro("libro2", "codigo2", "genero2")
libro3 = Libro("libro3", "codigo3", "genero3")    
biblioteca = Biblioteca([])
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
print(biblioteca)
