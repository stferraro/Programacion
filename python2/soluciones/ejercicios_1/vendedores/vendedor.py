class Vendedor:
    
    def __init__(self, nombre, apellido, cedula, salario_base, cargo, num_ventas):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._salario_base = salario_base
        self._cargo = cargo
        self._num_ventas = num_ventas

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
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, value):
        self._salario_base = value

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    @property
    def num_ventas(self):
        return self._num_ventas

    @num_ventas.setter
    def num_ventas(self, value):
        self._num_ventas = value
        
    def get_calcular_salario(self):
        self._cargo = self._cargo.capitalize()
        if self._cargo == "Coordinador":
            return self._salario_base + self._num_ventas * 10
        else:
            return self._salario_base + self._num_ventas * 5
        return 0
    
    def __str__(self):
        return f"Nombre: {self._nombre}\nApellido: {self._apellido}\nCedula: {self._cedula}\nSalario: {self.get_calcular_salario():.2f}"


        
    