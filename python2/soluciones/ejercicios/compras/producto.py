class Producto:
    
    def __init__(self, nombre, cantidad, precio ):
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value
        
    def total(self):
        return self._cantidad * self._precio
        
    def __str__(self):
        return f"Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"

        
    