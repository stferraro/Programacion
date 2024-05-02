"""

calculadora sencilla


"""

print ("Menu de operaciones")
print ("1.Suma")
print ("2.Resta")
print ("3.Multiplicacion")
print ("4.Division")
print ("0.Salir")

operacion = 1

while operacion != 0 :
    
    operacion = int(input("Escoje la operacion a realizar: --> "))
   
    if operacion == 1 :
        numero1 = float (input("Ingresa el numero 1: --> "))
        numero2 = float (input("Ingresa el numero 2: --> "))
        numero3 = numero1 + numero2
        print (f"La suma es igual a {numero3:.2f}")
   
    elif operacion == 2:
        numero1 = float (input("Ingresa el numero 1: --> "))
        numero2 = float (input("Ingresa el numero 2: --> "))
        numero3 = numero1 - numero2
        print (f"La resta es igual a {numero3:.2f}")
   
    elif operacion == 3 :
        numero1 = float (input("Ingresa el numero 1: --> "))
        numero2 = float (input("Ingresa el numero 2: --> "))
        numero3 = numero1 * numero2
        print (f"el producto es igual a {numero3:.2f}")
   
    elif operacion == 4 :
        numero1 = float (input("Ingresa el numero 1: --> "))
        numero2 = float (input("Ingresa el numero 2: --> "))
   
        while numero2 == 0 :
            numero2 = float (input("Error el valor del numero no puede ser negativo.Ingresa el numero 2: --> "))       
        numero3 = numero1 / numero2
        print (f"el producto es igual a {numero3:.2f}")
        
    elif operacion == 0 :
        print ("Hasta luego")

    
    
        
