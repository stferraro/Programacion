'''Se necesita crear una aplicación que nos permite convertir la cantidad de BS que
tenemos en dólares. De manera específica la aplicación va a trabajar con la tasa del
dólar BCV del día. La aplicación va a pedir el valor de la tasa del dólar en ese momento
la cantidad en BS a convertir en dólares y imprimir el resultado de la conversión con
dos valores decimales.'''

tasaDolarBCV = float(input("Tasa del dia: "))
bs = float(input("Cantidad de Bs a convertir a $: "))

dolares = bs / tasaDolarBCV
print(f"La cantidad en dolares es: {dolares:.4f} $$")
