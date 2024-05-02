from producto import Producto


class Compra:
    def __init__(self, productos ):
        self._productos = productos

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, value):
        self._productos = value
        
    def agregarProducto(self, producto):
        self._productos.append(producto)
            
    def total_producto(self):
        total_producto = 0
        for p in self._productos:
            total_producto += p.total()
        return total_producto

            
    def __str__(self):
        productos_str = ""
        total_producto = 0
        for p in self._productos:
            productos_str += p.__str__() + "\n"
            total_producto = self.total_producto()
        return f'Productos: \n{productos_str}\nTotal: {total_producto}'
    
producto = Producto("Manzana", 5, 100)
compra = Compra([producto])
compra.agregarProducto(producto)
producto2 = Producto("Pera", 3, 120)
compra.agregarProducto(producto2)
producto3 = Producto("Naranja", 2, 160)
compra.agregarProducto(producto3)
print(compra)
            