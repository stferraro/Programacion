from abc import ABC, abstractmethod

class AutomovilAbstracto(ABC):

    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frenar(self):
        pass

class AutomovilGasolina(AutomovilAbstracto):

    def acelerar(self):
        print("Suministrando gasolina al motor")

    # Código para acelerar el automóvil

    def frenar(self):
        print("Frenando el automóvil")
        
    # Código para frenar el automóvil

class AutomovilElectrico(AutomovilAbstracto):

    def acelerar(self):
        print("Suministrando energía eléctrica al motor")

    # Código para acelerar el automóvil eléctrico

    def frenar(self):
        print("Frenando el automóvil eléctrico")

    # Código para frenar el automóvil eléctrico

class AutomovilDeportivo(AutomovilAbstracto):

    def acelerar(self):
        print("Acelerando el automóvil deportivo")

    # Código para acelerar el automóvil deportivo

    def frenar(self):
        print("Frenando el automóvil deportivo")
        
    # Código para frenar el automóvil deportivo
    
automovil = AutomovilDeportivo()
automovil.acelerar()
automovil.frenar()