#condicionales combinados

edad = int (input ("Digite la edad: --> "))

if 0<edad<100 :  
    print("Edad Correcta")
    if edad>=18:
        print("Es mayor de edad")
        
else :
    print("Edad incorrecta")