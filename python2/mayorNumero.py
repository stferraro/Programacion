a = int (input("Valor de a:--> "))
b = int (input("Valor de b:--> "))
c = int (input("Valor de c:--> "))

if (a >= b) and (a >= c):
    print(f"{a} es el numero mayor")
elif (b >= a) and (b >= c):
    print(f"{b} es el numero mayor")
elif (c >= b) and (c >= a) :
    print(f"{c} es el numero mayor")
