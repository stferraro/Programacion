import random


jugada = "s"

while jugada == "s" :
    
    jugada = input("Quieres jugar s/n: --> ").lower()
    
    if jugada == "s" :
        
        print ("Piedra , Papel o Tijera")

        print ("1 Piedra")
        print ("2 Papel")
        print ("3 Tijera")

        jugadaComputadora = random.randint(1, 3)
        jugadaPersonal = int(input("Que quieres Piedra, Papel o Tijera --> "))

        if (jugadaComputadora == jugadaPersonal):
    
            print("empate")
            
            if (jugadaComputadora == 1):
            
                print("Personal: Piedra")
                print("Computadora; Piedra")
            
            elif (jugadaComputadora == 2):
                
                print("Personal: Papel")
                print("Computadora: Papel")
            
            elif (jugadaComputadora == 3) :
                
                print ("Personal: Tijera")
                print ("Personal: Tijera")
    
        elif (jugadaComputadora == 1) and (jugadaPersonal == 2) :
    
            print("Ganaste")
            print("Personal: Papel" )
            print("Computadora: Piedra")

        elif (jugadaComputadora == 2) and (jugadaPersonal == 1) :
    
            print("Perdiste")
            print("Personal: Piedra")
            print("Computadora: Papel")
    
        elif (jugadaComputadora == 3) and (jugadaPersonal == 1) :
         
            print("Ganaste")
            print("Personal: Piedra")
            print("Computadora: Tijera")
    
        elif (jugadaComputadora == 2) and (jugadaPersonal == 3) :
    
            print("Ganaste")
            print("Personal: Tijera")
            print("Computadora: Papel")
    
        elif (jugadaComputadora == 1) and (jugadaPersonal == 3) :
    
            print("perdiste")
            print("Personal: Tijera")
            print("Computadora: Piedra")
    
        elif (jugadaComputadora == 3) and (jugadaPersonal == 2) :
            print("perdiste")
            print("Personal: Papel")
            print("Computadora: Tijera")
    
    elif (jugada != "s") and (jugada != "n") :
        
        print ("error, en la jugada")
        jugada = "s"
        
    else :
        print ("Hasta Luego")
