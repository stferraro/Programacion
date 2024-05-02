class Empleado:
    def __init__(self, nombre,apellido, cedula, sueldo_base,horas_extra):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._sueldo_base = sueldo_base
        self._horas_extra = horas_extra

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @property
    def sueldo_base(self):
        return self._sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, value):
        self._sueldo_base = value

    @property
    def horas_extra(self):
        return self._horas_extra

    @horas_extra.setter
    def horas_extra(self, value):
        self._horas_extra = value
        
    def sueldo_total(self):
        return self._sueldo_base + self._horas_extra * 5
    
    def __str__(self):
        return f'{self._nombre} {self._apellido} {self._cedula} {self._sueldo_base} {self._horas_extra} {self.sueldo_total()}'
    
    

