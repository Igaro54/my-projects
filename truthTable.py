"""

Title : truthTable.py
Author : Kylian Renout
Last time updated : 16/01/21
Version : 1.0

"""


_continue = ""
lang = ""
tab_size = -1 #Appel de la variable à 3 valeurs (-1 : Valeur par défaut, 0 : Grand tableau, 1 : Petit tableau) / Permet également de corriger les erreurs


def table(question, tab_size): #Définition de la fonction qui calcule la valeur de var_a et de var_b selon le type de l'opérant
    var_a = 0
    var_b = 0
    if tab_size == 0: #Affiche l'en-tête du tableau en fonction de sa taille demandée
        print("|------------------------|\n|    a   |   b   |   s   |")
    elif tab_size == 1:
        print("|----------------|\n|    a   |   s   |")
    else: #Corrige l'utilisateur si l'opérateur inséré n'est pas valide (tab_size = -1)
        if lang == "ENG" or lang == "eng":
            print("Operator not found. Please use one of the proposed operators.")
        elif lang == "FRA" or lang == "fra":
            print("Opérateur non reconnu. Veuillez utiliser un des opérateurs proposés.")
    for var_a in range(0, 2): #Calcule pour var_a les valeurs 0 et 1
        for var_b in range(0, 2): #Calcule pour var_b les valeurs 0 et 1
            if question == "AND" or question == "ET" or question == "&":
                result = var_a & var_b
            if question == "OR" or question == "OU" or question == "|":
                result = var_a | var_b
            if question == "^":
                result = var_a ^ var_b
            if tab_size == 0:
                print("|------------------------|\n|   ", var_a,"  |  ", var_b,"  |  ", result,"  |") #Impression de la table de vérité à 3 colonnes
        if question == "==":
            result = var_a
        if question == "not" or question == "non":
            result = int(not(var_a)) 
        if tab_size == 1:
            print("|----------------|\n|   ", var_a,"  |  ", result,"  |") #Impression de la table de vérité à 2 colonnes
    if tab_size == 0:
        print("|------------------------|")
    elif tab_size == 1:
        print("|----------------|")


while (not lang == "ENG" or not lang == "fra" or not lang == "eng" or not lang == "fra") and not _continue == "n":
    lang = input("Quelle langue souhaitez-vous utiliser / Which language would you like to use (ENG, FRA)? : ") #Appel de la variable qui définit la langue du programme (ENG, FRA)
    if lang != "ENG" and lang != "FRA" and lang != "eng" and lang != "fra":
        print("Langue inconnu. Veuillez réessayer / Unknown language. Please retry")
    else:    
        while not _continue == "n":
            if lang == "FRA" or lang == "fra": #Programme en langue française
                question = input("De quel opérateur voulez-vous la table de vérité (ET, &, OU, |, ^, == et NON) ? : ") #Question posée à l'utilisateur
                if question == "et" or question == "ou" or question == "ET" or question == "OU" or question == "^" or question == "&" or question == "|" or question == "==": #Vérifie si le tableau devra être grand ou petit
                    question = question.upper()
                    print("Table de vérité de : a", question, "b")
                else:
                    if question == "non" or question == "NON": 
                        question = question.lower()
                        print("Table de vérité de : non(a)")
                if question == "non" or question == "==": #Vérifie si l'opérant doit définir le tableau avec 2 ou 3 colonnes
                    tab_size = 1
                else:
                    if question == "ET" or question == "OU" or question == "&" or question == "|" or question == "^":
                        tab_size = 0
                    else:
                        tab_size = -1
                table(question, tab_size)
                while not _continue == "n" or not _continue == "o": #Permet d'avoir uniquement 2 réponses possibles "o" et "n"
                    _continue = input("Voulez vous continuer ? (o/n) : ")
                    if _continue != "n" and _continue != "o": 
                        print("Veuillez entrer une réponse valide.")
                    else:
                        break
            if lang == "ENG" or lang == "eng": #Programme en langue anglaise (code similaire à celui de la langue française)
                question = input("Which operator do you want the truth table from (AND, &, OR, |, ^, == et NOT)? : ")
                if question == "and" or question == "or" or question == "AND" or question == "OR" or question == "^" or question == "&" or question == "|" or question == "==":
                    question = question.upper()
                    print("Truth table of: a", question, "b")
                else:
                    if question == "not" or question == "NOT":
                        question = question.lower()
                        print("Truth table of: not(a)")
                if question == "not" or question == "==":
                    tab_size = 1
                else:
                    if question == "AND" or question == "OR" or question == "&" or question == "|" or question == "^":
                        tab_size = 0
                    else:
                        tab_size = -1
                table(question, tab_size)
                while not _continue == "n" or not _continue == "y":
                    _continue = input("Do you want to continue? (y/n) : ")
                    if _continue != "n" and _continue != "y":
                        print("Please enter a valid answer.")
                    else:
                        tab_size = -1
                        break

if lang == "fra" or lang == "FRA": #Message de fin du programme
    print("{Programme terminé}")
if lang == "eng" or lang == "ENG":
    print("{Program ended}")