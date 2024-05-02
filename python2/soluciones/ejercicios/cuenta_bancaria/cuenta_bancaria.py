class CuentaBancaria:
    
    def __init__(self, numero, tipo, saldo):
        self.__numero = numero
        self.__tipo = tipo
        self.__saldo = saldo

    @property
    def _numero(self):
        return self.__numero

    @_numero.setter
    def _numero(self, value):
        self.__numero = value

    @property
    def _tipo(self):
        return self.__tipo

    @_tipo.setter
    def _tipo(self, value):
        self.__tipo = value

    @property
    def _saldo(self):
        return self.__saldo

    @_saldo.setter
    def _saldo(self, value):
        self.__saldo = value
        
    def depositar(self, cantidad):
        self.__saldo += cantidad
        
    def retirar(self, cantidad):
        self.__saldo -= cantidad
        
    def __str__(self):
        return f'Numero: {self._numero} Tipo: {self._tipo} Saldo: {self._saldo}'

       