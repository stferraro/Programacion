"""
pide un caracter e indica si es una vocal o no

"""

#lower() metodo que retorna una copia y la transforma en una valor en minuscola


caracter = input("ingresa una letra:--> ").lower()  

if (caracter == "a") or (caracter == "e") or (caracter == "i") or (caracter == "o") or (caracter == "u") :
    print (f"El caracter es una vocal")
elif len(caracter) > 1 :
    print (f"Valor incorrecto")
else :
    print (f"El caracter es una consonante")