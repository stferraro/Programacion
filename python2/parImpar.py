n1 = int (input("Numero 1: --> "))
n2 = int (input("Numero 2: --> "))

if (n1 > 0) and (n2 > 0):
    print ("numero correcto")
    if ((n1 % 2) == 0) and ((n2% 2) == 0):
        print(f"{n1} y {n2} son numeros pares")
    else: 
        if (n1 % 2) == 0 and (n2 % 2) != 0:
            print (f"{n1} es par")
            print (f"{n2} es impar")
        elif ((n1 % 2) != 0) and ((n2 % 2) != 0) :
            print(f"{n1} y {n2} son numeros impares")
        else : 
            print (f"{n1} es impar")
            print (f"{n2} es par")
else :
    print ("numero incorrecto")
    
        

    