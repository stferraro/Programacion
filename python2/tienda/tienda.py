from producto import Producto


class Tienda:
    def __init__(self, nombre, rif, productos):
        self._nombre = nombre
        self._rif = rif
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)
        
    def get_total(self):
        return sum([producto.precio for producto in self._productos])
    
    
    def get_costo_mayor(self):
        if len(self._productos) == 0:
            return 0
        return max([producto.precio for producto in self._productos])
    
    def get_costo_menor(self):
        if len(self._productos) == 0:
            return 0
        return min([producto.precio for producto in self._productos])
    
    def __str__(self):
        productos_str = "\n".join([str(producto) for producto in self._productos])
        return f"Nombre: {self._nombre}\n RIF: {self._rif}\n Productos: {productos_str}"
    
    def get_suma_productos(self):
        if len(self._productos) == 0:
            return 0
        return sum([producto.costo() for producto in self._productos])
    
producto = Producto("Mouse", "Logitech", "Logitech", 5, 1200)
producto2 = Producto("Mouse", "Logitech", "Logitech", 20, 200)
producto3 = Producto("Televisor", "Sankey", "Samsung", 10, 1000)
tienda = Tienda("Tienda", "J-123456789", [])
tienda.agregar_producto(producto)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)
maxi = tienda.get_costo_mayor()
mini = tienda.get_costo_menor()
suma = tienda.get_suma_productos()
print(tienda)
print(f"El costo mayor es: {maxi}")
print(f"El costo menor es: {mini}")
print(f"La suma de los productos es: {suma}")
print(tienda.get_total())
