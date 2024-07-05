class Cliente:
    
    def __init__(self, nombre, apellido, cedula, placa_vehiculo, costo_reparacion):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._placa_vehiculo = placa_vehiculo
        self._costo_reparacion = costo_reparacion

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
    def placa_vehiculo(self):
        return self._placa_vehiculo

    @placa_vehiculo.setter
    def placa_vehiculo(self, value):
        self._placa_vehiculo = value

    @property
    def costo_reparacion(self):
        return self._costo_reparacion

    @costo_reparacion.setter
    def costo_reparacion(self, value):
        self._costo_reparacion = value
        
    def __str__(self):
        return f"Nombre: {self._nombre}, Apellido: {self._apellido}, Cedula: {self._cedula}, Placa Vehiculo: {self._placa_vehiculo}, Costo de Reparacion: {self._costo_reparacion}"

        
    