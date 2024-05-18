from libro import Libro


class Biblioteca:
    def __init__(self, lista_libros):
        self._lista_libros = lista_libros

    @property
    def lista_libros(self):
        return self._lista_libros

    def add_libros(self, libro):
        self._lista_libros.append(libro)
        
    def __str__(self):
        return "\n".join([str(libro) for libro in self._lista_libros])
    
    def crea_txt(self):
        with open('/home/gerardo/desarrollo/Programacion/nuevos/filesTxt/biblioteca.txt', 'w') as f:
            try:
                f.write(self.__str__())
            except FileNotFoundError:
                print('No se encontro el archivo')
                
biblioteca = Biblioteca([])
libros = []
libro1 = Libro('111', 'Cien Años de Soledad', 'Novela')
libro2 = Libro('222', 'El Señor de los Anillos', 'Fantasia')
libro3 = Libro('333', 'El principito', 'Novela')

biblioteca.add_libros(libro1)
biblioteca.add_libros(libro2)
biblioteca.add_libros(libro3)

print(biblioteca)
biblioteca.crea_txt()