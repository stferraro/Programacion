from cuenta import Cuenta

class Cliente:
    
    def __init__(self, nombre, apellido, cedula, cuentas):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.cuentas = cuentas

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, value):
        self.apellido = value

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, value):
        self.cedula = value

    def get_cuentas(self):
        return self.cuentas

    def set_cuentas(self, value):
        self.cuentas = value
        
    def agregaCuenta(self, cuenta):
        self.cuentas.append(cuenta)
        
    def __str__(self) -> str:
        cuentas_str = '\n'.join([str(cuenta) for cuenta in self.cuentas])
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Cedula: {self.cedula}, \nCuentas: \n{cuentas_str}"
    
    def crea_txt(self):
        try:
            with open(f"{self.cedula}.txt", "w") as f:
                f.write(self.__str__())
        except FileNotFoundError as fn:
            print(fn)
            print("Error al crear el archivo")
            
            
cliente = Cliente("Juan", "Perez", "123456789", [])
cuenta = Cuenta(1234, "Ahorro", 1000)
cuenta2 = Cuenta(5678, "Corriente", 2000)

cliente.agregaCuenta(cuenta)
cliente.agregaCuenta(cuenta2)

cliente.crea_txt()


            

        
    