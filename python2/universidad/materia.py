class Materia:
    def __init__(self, nombre, nota, creditos):
        self._nombre = nombre
        self._creditos = creditos
        if  nota < 0 or nota > 20:
            raise ValueError("La nota proporcionada no es válida")
        self._nota = nota

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, value):
        self._creditos = value

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, value):
        try:
            if value < 0 or value > 20:
                raise ValueError("El valor no es válido")
            self._nota = value
        except ValueError as e:
            return str(e)

  
    def valor_materia(self):
        return self._creditos * self._nota
        
    def __str__(self) -> str:
        return f"nombre: {self._nombre} Nota: {self._nota} Creditos: {self._creditos}"
    