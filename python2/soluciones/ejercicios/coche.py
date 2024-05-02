class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def arrancar(self):
        print("El coche ha arrancado")

    def acelerar(self):
        print("El coche está acelerando")

    def frenar(self):
        print("El coche está frenando")

    def cambiar_marca(self, nueva_marca):
        self.marca = nueva_marca
        print("La marca del coche ha sido cambiada a", nueva_marca)

audi = Coche("Audi", "A4", 2020)
audi.cambiar_marca("BMW")
print(audi.marca)  # salida: BMW