class Persona:
    
    def __init__(self, nombre, apellido, cedula, cuentas_bancarias):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._cuentas_bancarias = cuentas_bancarias

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, value):
        self._apellidos = value

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @property
    def cuentas_bancarias(self):
        return self._cuentas_bancarias

    @cuentas_bancarias.setter
    def cuentas_bancarias(self, value):
        self._cuentas_bancarias = value
        
    def agregar_cuenta(self, cuenta_bancaria):
        self._cuentas_bancarias.append(cuenta_bancaria)
        
    def eliminar_cuenta(self, cuenta_bancaria):
        cuentas_bancarias = [c for c in self._cuentas_bancarias if c._numero != cuenta_bancaria._numero]
        if cuenta_bancaria.numero in cuentas_bancarias:
            self._cuentas_bancarias.remove(cuenta_bancaria)
            print("Cuenta eliminada")
        else:
            print("La Cuenta no existe en el banco")
            
    def listar_cuentas(self):
        for cuenta_bancaria in self._cuentas_bancarias:
            print(cuenta_bancaria)
            
    def buscar_cuenta(self, numero):
        for cuenta_bancaria in self._cuentas_bancarias:
            if cuenta_bancaria._numero == numero:
                return cuenta_bancaria
        return None
    
    def depositar_saldo(self, cuenta_bancaria, monto):
        cuenta_bancaria = self.buscar_cuenta(cuenta_bancaria)
        if cuenta_bancaria:
            cuenta_bancaria.depositar(monto)
        else:
            print("La cuenta no existe en el banco")
            
    def retirar_saldo(self, cuenta_bancaria, monto):
        cuenta_bancaria = self.buscar_cuenta(cuenta_bancaria)
        if cuenta_bancaria:
            cuenta_bancaria.retirar(monto)
        else:
            print("La cuenta no existe en el banco")
            
    def __str__(self):
        cuentas_str = ""
        for cuenta_bancaria in self._cuentas_bancarias:
            cuentas_str += f"{cuenta_bancaria}\n"
        return f"Persona: {self._nombre} {self._apellido} Cedula: {self._cedula}\nCuentas: \n{cuentas_str}"
            
                