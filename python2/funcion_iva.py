def funcion_iva(base, iva):
    return base + base * (iva / 100)


base = float(input("ingrese la base imponible: "))
iva = float(input("ingrese el porcentaje de iva: "))
valor = funcion_iva(base, iva)

print(f"el valor de la base imponible es: {base:.2f}")
print(f"el valor del iva es:  {iva:.2f}")
print(f"el valor del iva es:  {valor:.2f}")