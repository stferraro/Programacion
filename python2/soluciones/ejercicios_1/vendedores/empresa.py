from vendedor import Vendedor

class Empresa:
    def __init__(self, nombre, rif, vendedores):
        self._nombre = nombre
        self._rif = rif
        self._vendedores = vendedores

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def rif(self):
        return self._rif

    @rif.setter
    def rif(self, value):
        self._rif = value

    @property
    def vendedores(self):
        return self._vendedores

    @vendedores.setter
    def vendedores(self, value):
        self._vendedores = value
        
    def agregar_vendedor(self, vendedor):
        self._vendedores.append(vendedor)
        
    def get_calcula_total_gastos(self):
        return sum([vendedor.get_calcular_salario() for vendedor in self._vendedores])
    
    def __str__(self):
        vendedores_str = "\n".join([str(vendedor) for vendedor in self._vendedores])
        total_gastos = self.get_calcula_total_gastos()
        return f"Nombre: {self._nombre}\nRIF: {self._rif}\nVendedores:\n{vendedores_str}\nTotal de gastos: {total_gastos:.2f}"
    
    
vendedor1 = Vendedor("John", "Doe", "123456789", 1000, "Coordinador", 10)
vendedor2 = Vendedor("Jane", "Smith", "987654321", 500, "Cajero", 5)
vendedor3 = Vendedor("Michael", "Johnson", "456789123", 2000, "Gerente", 20)
vendedores = [vendedor1, vendedor2]
empresa = Empresa("Mi Empresa", "123456789", vendedores)
empresa.agregar_vendedor(vendedor3)

print(empresa)
    

 