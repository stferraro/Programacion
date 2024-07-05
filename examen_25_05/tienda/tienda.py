from prenda import Prenda

class Tienda:
    
    def __init__(self, prendas):
        self._prendas = prendas

    @property
    def prendas(self):
        return self._prendas

    @prendas.setter
    def prendas(self, value):
        self._prendas = value
        
    def agregar_prenda(self, prenda):
        self._prendas.append(prenda)
        
    def total_prendas(self):
        return len(self._prendas)
    
    def valor_total(self):
        return sum([prenda.valor_total() for prenda in self._prendas])
    
    def __str__(self):
        prendas_str = '\n'.join([prenda.__str__() for prenda in self._prendas])
        total_prendas = f'\nTotal de prendas: {self.total_prendas()}'
        valor_total = f'\nTotal de prendas: {self.valor_total():.2f}'
        return "".join([prendas_str, total_prendas, valor_total])
    
    def crear_txt(self):
        try:
            with open("tienda.txt", "w") as f:
                f.write(self.__str__())
        except FileNotFoundError as fn:
            print(fn)
            print("Error al crear el archivo")
            
tienda = Tienda([])

prenda = Prenda(1234, "Coca Cola", 5, 500)
prenda2 = Prenda(5678, "Fanta", 4, 300)
prenda3 = Prenda(9012, "Sprite", 1000, 200)

tienda.agregar_prenda(prenda)
tienda.agregar_prenda(prenda2)
tienda.agregar_prenda(prenda3)

tienda.crear_txt()
print(tienda)