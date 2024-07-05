from juguete import Juguete

class Tienda:
    
    def __init__(self, juguetes):
        self._juguetes = juguetes

    @property
    def juguetes(self):
        return self._juguetes

    @juguetes.setter
    def juguetes(self, value):
        self._juguetes = value
        
    def agregarJuguete(self, juguete):
        self._juguetes.append(juguete)
        
    def eliminarJuguete(self, juguete):
        self._juguetes.remove(juguete)
        
    def __str__(self):
        juguetes_str = '\n'.join(juguete.__str__() for juguete in self._juguetes)
        return f'Juguetes: \n{juguetes_str}'
    
    def __len__(self):
        return len(self._juguetes)
    
tienda = Tienda([])
juguete = Juguete("Juguete 1", "123", 10, 100)
juguete2 = Juguete("Juguete 2", "456", 20, 120)
juguete3 = Juguete("Juguete 3", "789", 30, 160)
tienda.agregarJuguete(juguete)
tienda.agregarJuguete(juguete2)
tienda.agregarJuguete(juguete3)
print(tienda)