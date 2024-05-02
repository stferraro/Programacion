from automovil import Automovil

class AutomovilDeportivo(Automovil):
    
    def __init__(self, marca, modelo, color, velocidad_maxima, aleron):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self.__aleron = aleron

    @property
    def _aleron(self):
        return self.__aleron

    @_aleron.setter
    def _aleron(self, value):
        self.__aleron = value

        
    def encender_aleron(self):
        print("Encendiendo alerón")
            

automovilDeportivo = AutomovilDeportivo("Ford", "Mustang", "Rojo", 250, True)
automovilDeportivo.encender_aleron()