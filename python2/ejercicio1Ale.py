"""**************************************************
           
            a^3 * (b^2 - 2 a c) / 2 b

****************************************************"""



a = float(input("introduce el valor de la variable a: "))

b = float (input("introduce el valor de la variable b: "))

c = float (input("introduce el valor de la variable c: "))


resultado = ((a**3) * (b**2 - (2 * a*c))/ (2 * b))

resultado = round(resultado, 2)

print(f"el resultado es {resultado}")




 