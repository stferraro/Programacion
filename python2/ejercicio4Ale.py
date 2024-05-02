"""****************************************************************************************

    Dado el radio de una circunferencia calcula el área y la longitud de la circuferencia
    
*******************************************************************************************"""

import math

radio = float(input("ingresa el valor del radio de la circunferencia: "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio


print (f"El área de la circunferencia es igual a {area:.2f} ")
print (f"La longitud de la circunferencia es igual a {longitud:.2f}")




