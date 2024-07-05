from libro import Libro


class Biblioteca:
    def __init__(self,libros):
        self.libros = libros

    def get_libros(self):
        return self.libros

    def set_libros(self, value):
        self.libros = value
        
    def add_libro(self, value):
        self.libros.append(value)
        
    def total(self):
        return sum([libro.get_costo() for libro in self.libros])
        

    def __str__(self):
        libros_str = "".join([str(libro) for libro in self.libros])
        return f"Libros: {libros_str}" + f"\nTotal: {self.total()}"
    
    
libro1 = Libro(1, "El principito", "Ciencia Ficcion", 7)
libro2 = Libro(2, "El senor de los anillos", "Fantasia", 5)
libro3 = Libro(3, "Harry Potter", "Fantasia", 10)
libro4 = Libro(4, "El senor de los anillos", "Fantasia", 5) 
libros = [libro1, libro2, libro3, libro4]
biblioteca = Biblioteca(libros)
print(biblioteca)