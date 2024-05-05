from personas import Persona

class Fundacion:
    
    def __init__(self, nombre, rif, personas):
        self._nombre = nombre
        self._rif = rif
        self._personas = personas

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def rif(self):
        return self._rif

    @rif.setter
    def rif(self, value):
        self._rif = value

    @property
    def personas(self):
        return self._personas

    @personas.setter
    def personas(self, value):
        self._personas = value
        
        
    def agregarPersona(self, persona):
        self._personas.append(persona)
        
    def eliminarPersona(self, persona):
        self._personas.remove(persona)
        
    def __str__(self):
        personas_str = '\n'.join (persona.__str__() for persona in self._personas)
        return f"{self._nombre} {self._rif} {personas_str}"
    
    
persona = Persona('Juan', 'Perez', 'V-123456789', 23)
persona1 = Persona('Pedro', 'Perez', 'V-123456786', 24)
persona2 = Persona('Maria', 'Perez', 'V-123456785', 25)

fundacion = Fundacion('Fundacion', 'J-123456789', [persona, persona1, persona2])

print(fundacion)