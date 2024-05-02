
print("************************************************")
print("|  Conversor de dolares estadounidenses a euro |")
print("************************************************")

dolares = float(input("Que cantidad de dolares quieres convertir: "))

resultado = dolares * 0.93
resultado = round (resultado, 2)
print (f"corresponde a {resultado} euros")

bolivares = float(input("Que cantidad de BS quieres convertir: "))

resultado2 = bolivares / 24.388
resultado2 = round (resultado2, 2)

print (f"corresponde a {resultado2} dolares ")





