'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada
paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
programa que lea el número de payasos y muñecas vendidos en el último pedido y
calcule el peso total del paquete que será enviado.'''

PESOPAYASO = 112
PESOMUNECA = 75

cantidadPayasos = int(input("Cantidad de Payasos: "))
cantidadMunecas = int(input("Cantidad de Muñecas: "))

pesoTotal = (cantidadPayasos * PESOPAYASO) + (cantidadMunecas * PESOMUNECA)

print(f"El peso total del paquete es de {pesoTotal:.2f}")

costoPayaso = float(input("Costo del payaso: "))
costoMunecas = float(input("Costo de la muñeca: "))

costoPaquete = costoPayaso * cantidadPayasos + costoMunecas * cantidadMunecas

print (f"El costo total del paquete es igual a {costoPaquete:.2f}")

costoTotalPaquete = ((costoPaquete * 10) /100) + costoPaquete

print (f"El costo total del paquete es igual a {costoTotalPaquete:.2f}")

