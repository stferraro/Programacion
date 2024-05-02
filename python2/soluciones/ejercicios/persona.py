class Persona:
    
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad
        
    def saludar(self):
        print("Hola, mi nombre es", self.nombre + " y tengo", self.edad, "años")
 
        
p = Persona("Juan", 23)
p.saludar() # Imprime "Hola, mi nombre es Juan y tengo 23 años"