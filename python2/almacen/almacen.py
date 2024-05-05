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
        
    def agregarProducto(self, producto):
        self._productos.append(producto)
        
    def eliminarProducto(self, producto):
        self._productos.remove(producto)
        
    def __str__(self):
        productos_str = '\n'.join(producto.__str__() for producto in self._productos)
        return f'Productos: \n{productos_str}'
    
    def __len__(self):
        return len(self._productos)
    
producto = Producto('Manzana', '123', 10, 100)
producto2 = Producto('Pera', '456', 20, 120)
producto3 = Producto('Naranja', '789', 30, 160)
listaProductos = [producto, producto2, producto3]
almacen = Almacen(listaProductos)
print(almacen)