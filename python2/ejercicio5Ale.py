nombre = input ("nombre cliente: ")
valorCompra = float(input("costo total: "))

articulos = ("camisa beige, blue jeans talla 38, zapatos talla 43, correa de cuero marca Luis Vuitton")

resultado = (valorCompra - (valorCompra * 0.15)) 

print (f"nombre cliente: {nombre}")
print (f"articulos comprados {articulos}")
print (f"Costo sin descuento {valorCompra:.2f} $$")
print (f"Descuento 15%")
print (f"Valor de la compra {resultado:.2f} $$")
