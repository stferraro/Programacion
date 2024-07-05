from producto import Producto

class Almacen:
    def __init__(self, productos):
        self._productos = productos

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, value):
        self._productos = value
        
    def agregar_productos(self, producto):
        self._productos.append(producto)
        
    def total_precio_productos(self):
        return sum(producto.valor_total() for producto in self._productos)
    
    def total_productos(self):
        return len(self._productos)
        
    def __str__(self):
        productos_str = '\n'.join([lugar.__str__() for lugar in self._productos])
        total = f'\nTotal de productos: {self.total_productos()}'
        valor_total = f'\nTotal de productos: {self.total_precio_productos():.2f}'
        return "".join([productos_str, total, valor_total])
    
    def crear_txt(self):
        try:
            with open("almacen.txt", "w") as f:
                f.write(self.__str__())
        except FileNotFoundError as fn:
            print(fn)
            print("Error al crear el archivo")
            
almacen = Almacen([])
producto = Producto(1234, "Coca Cola", 100, 500)
producto2 = Producto(5678, "Fanta", 100, 500)
producto3 = Producto(9012, "Sprite", 100, 500)

almacen.agregar_productos(producto)
almacen.agregar_productos(producto2)
almacen.agregar_productos(producto3)

almacen.crear_txt()
print(almacen)
        
    