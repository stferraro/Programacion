class CuentaBancaria:
    
    def __init__(self,nombre, apellido, cedula, saldo):
        self.__nombre = nombre
        self.__saldo = saldo
        self.__apellido = apellido
        self.__cedula = cedula

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _saldo(self):
        return self.__saldo

    @_saldo.setter
    def _saldo(self, value):
        self.__saldo = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value


    @property
    def _saldo(self):
        return self.__saldo

    @_saldo.setter
    def _saldo(self, value):
        self.__saldo = value
        
    def depositar(self, cantidad):
        self.__saldo += cantidad
        return self.__saldo
    
    def retirar(self, cantidad):
        self.__saldo -= cantidad
        return self.__saldo
    
    def __str__(self) -> str:
        return f'Nombre: {self._nombre} Apellido: {self._apellido} Cedula: {self._cedula} Saldo: {self._saldo}'
    
cuenta = CuentaBancaria('Gerardo', 'Ferraro','15693289',5000)
print(cuenta)    