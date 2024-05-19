class Materia:
    
    def __init__(self, codigo, nombre, nota, credito):
        self._codigo = codigo
        self._nombre = nombre
        self._nota = nota
        self._credito = credito

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, value):
        self._nota = value

    @property
    def credito(self):
        return self._credito

    @credito.setter
    def credito(self, value):
        self._credito = value
        
    def valor_para_promedio(self):
        return (self._nota * self._credito)
    
    def suma_credito(self):
        credito_inicial = 0
        credito_inicial += self._credito
        return credito_inicial
    
    def __str__(self):
        return f"Código: {self._codigo}, Nombre: {self._nombre}, Nota: {self._nota}, Credito: {self._credito}"
