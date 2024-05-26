from cliente import Cliente

class Taller:
    
    def __init__(self, clientes):
        self._clientes = clientes

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self, value):
        self._clientes = value
        
    def agregar_vehiculo(self, vehiculo):
        self._clientes.append(vehiculo)
        
    def total_reparaciones(self):
        return sum(cliente.costo_reparacion for cliente in self._clientes)
        
    def __str__(self):
        clientes_str = '\n'.join([cliente.__str__() for cliente in self._clientes])
        total_reparaciones = f'\nTotal de Reparaciones: {self.total_reparaciones()}'
        return "".join([clientes_str, total_reparaciones])
    
    def crear_txt(self):
        try:
            with open("taller.txt", "w") as f:
                f.write(self.__str__())
        except FileNotFoundError as fn:
            print(fn)
            print("Error al crear el archivo")
            
            
taller = Taller([])

cliente = Cliente("Juan", "Perez", 123456789, "ABC123", 500.00)
cliente2 = Cliente("Pedro", "Lopez", 987654321, "DEF456", 600.00)
cliente3 = Cliente("Maria", "Garcia", 456789123, "GHI789", 700.00)

taller.agregar_vehiculo(cliente)
taller.agregar_vehiculo(cliente2)
taller.agregar_vehiculo(cliente3)

taller.crear_txt()
print(taller)
            
    