class Automovil:

    def __init__(self, marca, modelo, color, velocidad_maxima):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__velocidad_maxima = velocidad_maxima
        self.__velocidad_actual = 0

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    @property
    def _modelo(self):
        return self.__modelo

    @_modelo.setter
    def _modelo(self, value):
        self.__modelo = value

    @property
    def _color(self):
        return self.__color

    @_color.setter
    def _color(self, value):
        self.__color = value

    @property
    def _velocidad_maxima(self):
        return self.__velocidad_maxima

    @_velocidad_maxima.setter
    def _velocidad_maxima(self, value):
        self.__velocidad_maxima = value

    @property
    def _velocidad_actual(self):
        return self.__velocidad_actual

    @_velocidad_actual.setter
    def _velocidad_actual(self, value):
        self.__velocidad_actual = value
        
    def __str__(self):
        return f"Automovil marca: {self._marca}, modelo: {self._modelo}, color: {self._color}, velocidad maxima: {self._velocidad_maxima}, velocidad actual: {self._velocidad_actual}"
    

automovil = Automovil("Ford", "Mustang", "Rojo", 250)
print(automovil) 