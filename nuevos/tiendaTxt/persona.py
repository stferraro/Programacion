from producto import Producto

class Persona:
    
    def __init__(self, cedula, nombre, apellido, lista_productos):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._lista_productos = lista_productos

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
    def lista_productos(self):
        return self._lista_productos

    @lista_productos.setter
    def lista_productos(self, value):
        self._lista_productos = value

    def add_productos(self, producto):
        self._lista_productos.append(producto)
        
    def get_calculo_total(self):
        total = 0
        for i in self._lista_productos:
            total += i.get_calculo_total()
        if total > 1000:
            total = total - ((total * 10)/100)
        return total
        # return sum(producto.get_calculo_total() for producto in self._lista_productos)
    
    def __str__(self):
        productos_str = "\n".join([producto.__str__() for producto in self._lista_productos])
        persona_str = f"Cedula: {self._cedula}, Nombre: {self._nombre}, Apellido: {self._apellido}"
        str1 = ''.center(50, '*')
        total = self.get_calculo_total()
        valor_final = ''.join([persona_str, "\n", str1, "\n", productos_str , "\n", "Total: " , "\t\t\t\t\t\t", str(total)])
        return valor_final
        
    def crea_txt(self):
        with open('persona.txt', 'w') as f:
            try:
                f.write(self.__str__())
            except FileNotFoundError:
                print('No se encontro el archivo')
                
    def crea_excel(self):
        with open('persona.xlsx', 'w') as f:
            try:
                f.write(self.__str__())
            except FileNotFoundError:
                print('No se encontro el archivo')
                
                
                
persona = Persona('V-15693289', 'Gerardo Ali', 'Ferraro Schelijasch', [])
lista_productos = []

producto = Producto('123', 'Coca Cola', 2, 100)
producto1 = Producto('111', 'Azucar', 3, 200)
producto2 = Producto('333', 'Leche', 4, 300)

persona.add_productos(producto)
persona.add_productos(producto1)
persona.add_productos(producto2)

print(persona)
persona.crea_txt()
persona.crea_excel()


            