lista1 = [1, 2, 3, 5, "Alejandro" , "Angel", 2, 3, 3]

lista2 = [2, 3, 4, 6, "gerardo", "Grignani", "gerardo", 5, 6, 2]

conjunto1 = set (lista1)
conjunto2 = set(lista2)

print (conjunto1)
print (conjunto2)

union = list(conjunto1 | conjunto2) 
soloA = list(conjunto1-conjunto2)
soloB = list(conjunto2-conjunto1)
solos = list(conjunto1 & conjunto2)

print (union)
print (soloA)
print (soloB)
print (solos)






