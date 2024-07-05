costoMoto = float(input("Costo de la moto: "))
costoCarro = float(input("Costo del carro: "))

cantidadMoto = int(input("Numero de motos vendidas: "))
cantidadCarro = int(input("Numero de carros vendidos: "))

gananciaMoto = costoMoto * 0.1
gananciaCarro = costoCarro * 0.15

gananciaDiaMoto = gananciaMoto * cantidadMoto
gananciaDiaCarro = gananciaCarro * cantidadCarro

gananciaTotal = gananciaDiaMoto + gananciaDiaCarro

print(f"La ganancia total del vendedor en el dia es igual a : {gananciaTotal:.2f}")
