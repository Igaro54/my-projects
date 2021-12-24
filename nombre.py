from collections import deque

nbr_mult = input("Choisir une quantité de nombre à lister : ")
nbr = deque([])
last_nbr = deque([])

def parity(nbr, number):                                                    #Déf calcul de la parité
    if nbr % 2 == 0:
        print(str(number + 1), ") Le nombre", nbr, "est pair.")
    else:
        print(str(number + 1), ") Le nombre", nbr, "est impair.")
def premier(nbr, number):                                                   #Déf calcul nombre premier
    add = 0
    for i in range(1, nbr + 1):
        if (nbr / i) % 2 == 1:
            add = add + 1
        elif (nbr / i) % 2 == 0:
            add = add - 1
    if add == 2:
        print(str(number + 1), ") Le nombre", nbr, "est un nombre premier.")

for i in range (int(nbr_mult)):                                             #Ajout de nombre(s)
    print(str(i + 1), ") Donner un nombre : ", end="")
    nbr.appendleft(int(input()))
last_nbr = nbr.copy()
for number in range (int(nbr_mult)):                                        #Définition des nombres
    parity(nbr.pop(), number)
    premier(last_nbr.pop(), number)