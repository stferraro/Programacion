from boleto import Boleto


class Persona:
    def __init__(self, cedula, nombre, apellido, num_deposito, lista_boletos):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._num_deposito = num_deposito
        self._lista_boletos = lista_boletos

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

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
    def num_deposito(self):
        return self._num_deposito

    @num_deposito.setter
    def num_deposito(self, value):
        self._num_deposito = value

    @property
    def lista_boletos(self):
        return self._lista_boletos

    @lista_boletos.setter
    def lista_boletos(self, value):
        self._lista_boletos = value
        
    def add_boletos(self, boleto):
        self._lista_boletos.append(boleto)
        
    def __str__(self):
        str = f"Persona: {self._cedula}, {self._nombre}, {self._apellido}, {self._num_deposito}"
        for boleto in self._lista_boletos:
            str += boleto.__str__()
        return str
  