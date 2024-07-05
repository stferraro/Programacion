from empleado import Empleado


class Empresa:
    
    def __init__(self, nombre, rif, empleados):
        self._nombre = nombre
        self._rif = rif
        self._empleados = empleados

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
    def empleados(self):
        return self._empleados

    @empleados.setter
    def empleados(self, value):
        self._empleados = value
        
    def agregar_empleados(self, empleado):
        self._empleados.append(empleado)
        
    def total_pagos(self):
        return sum(empleado.sueldo_total() for empleado in self._empleados)

    def __str__(self):
        return f'\n'.join([str(empleado) for empleado in self._empleados])+ f'\nTotal de pagos: {self.total_pagos()}'
        

empleado = Empleado('Juan', 'Perez', '123456', 10000, 5)
empleado2 = Empleado('Pedro', 'Lopez', '123457', 20000, 10)
empleado3 = Empleado('Maria', 'Garcia', '123458', 30000, 15)
listaEmpleados = [empleado,empleado2,empleado3]

empresa = Empresa('Tecno', 'J-12345678-9', listaEmpleados)

print(empresa)
        
    
    

        
    