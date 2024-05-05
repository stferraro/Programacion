class Producto:
    def __init__(self, nombre,modelo, marca, cantidad, precio):
        self._nombre = nombre
        self._modelo = modelo
        self._marca = marca
        self._cantidad = cantidad
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value
        
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value
        
    def costo(self):
        return self._precio * self._cantidad
    
    def __str__(self):
        return f"Nombre:{self._nombre}\n Modelo:{self._modelo}\n Marca:{self._marca}\n Cantidad:{self._cantidad}\n Precio:{self._precio}\n Costo:{self.costo()}"
    
