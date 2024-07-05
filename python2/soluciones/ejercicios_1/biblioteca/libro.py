class Libro:
    def __init__(self, id, titulo, genero, dias_alquiler):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.dias_alquiler = dias_alquiler

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, value):
        self.titulo = value

    def get_genero(self):
        return self.genero

    def set_genero(self, value):
        self.genero = value

    def get_dias_alquiler(self):
        return self.dias_alquiler

    def set_dias_alquiler(self, value):
        self.dias_alquiler = value
        
    def get_costo(self):
        return self.dias_alquiler * 10
    
    def __str__(self):
        return f"-Id: {self.id}\n-Titulo: {self.titulo}\n-Genero: {self.genero}\n-Costo: {self.get_costo()}\n"

        
    