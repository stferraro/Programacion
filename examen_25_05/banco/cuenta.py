class Cuenta:
    def __init__(self, num_cuenta, tipo_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo

    def get_num_cuenta(self):
        return self.num_cuenta

    def set_num_cuenta(self, value):
        self.num_cuenta = value

    def get_tipo_cuenta(self):
        return self.tipo_cuenta

    def set_tipo_cuenta(self, value):
        self.tipo_cuenta = value

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, value):
        self.saldo = value
        
    def __str__(self):
        return f"Numero de Cuenta: {self.num_cuenta}, Tipo de Cuenta: {self.tipo_cuenta}, Saldo: {self.saldo}"
    
    

        
    