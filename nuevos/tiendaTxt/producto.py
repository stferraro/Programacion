class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self._codigo = codigo
        self._nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, value):
        self.cantidad = value

    def get_precio(self):
        return self.precio

    def set_precio(self, value):
        self.precio = value
        
    def get_calculo_total(self):
        return self.cantidad * self.precio
        
    def __str__(self):
        return f"Código: {self._codigo}, Nombre: {self._nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
