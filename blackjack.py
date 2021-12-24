import random as rand

while 1:
    try:
        money = int(input("Choissisez le montant que vous souhaitez déposer : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre valide")

def cardsDropping(bet, money):
    player_score = 0
    dealer_score = 0
    aceRemoved = False
    playerHand, dealerHand = [rand.randint(1,13), rand.randint(1,13)], [rand.randint(1,13)]
    for playerCards in playerHand:
        if playerCards == 1:
            player_score += 11
        elif playerCards > 10:
            player_score += 10
        else:
            player_score += playerCards
    if playerHand.count(1) == 2:
        player_score = 12
    if dealerHand[0] <= 10:
        dealer_score = dealerHand[0]
    else:
        dealer_score += 10
    if dealerHand[0] == 1:
        dealer_score = 11
    while 1:
        print("Le total de vos cartes est égal à :", str(player_score),"\nLa première carte du croupier est :", str(dealer_score))
        if player_score != 21:
            question = input("Souhaitez-vous une nouvelle carte ? (oui/non) : ")
            if question == "oui":
                playerHand.append(rand.randint(1,13))
                if playerHand[len(playerHand)-1] <= 10:
                    player_score += playerHand[len(playerHand)-1]
                else:
                    player_score += 10
                if player_score > 21 and playerHand.count(1) == 0 or aceRemoved == True:
                    break
                elif player_score > 21 and playerHand.count(1) != 0 and aceRemoved != True:
                    player_score -= 10
                    playerHand.remove(1)
                    aceRemoved = True
                if player_score == 21:
                    print("Le total de vos cartes est égal à :", str(player_score), "\nC'est le maximum possible.")
                    break
            elif question == "non":
                break
            else:
                print("Erreur, veuillez réessayer")
        else:
            print("Le total de vos cartes est égal à :", str(player_score), "\nVous avez un BlackJack !")
            break
    if player_score > 21:
        print("Le total de vos cartes est égal à :", str(player_score), "\nVous êtes au dessus de 21.\nVous avez donc perdu.")
        money -= bet
    else:
        dealerPlaying(player_score, dealer_score, dealerHand, bet, money)

def dealerPlaying(player_score, dealer_score, dealerHand, bet):
    aceRemoved = False
    while 1:
        if dealer_score < 17:
            dealerHand.append(rand.randint(1,13))
            if dealerHand[len(dealerHand)-1] > 10:
                dealer_score += 10
            elif dealerHand[len(dealerHand)-1] == 1:
                dealer_score += 11
                if dealer_score > 21 and aceRemoved != True:
                    dealer_score -= 10
                    dealerHand.remove(1)
                    aceRemoved = True
            else:
                dealer_score += dealerHand[len(dealerHand)-1]
        else:
            break
    global money
    if dealer_score > 21:
        print("Le total des cartes du croupier est égal à :", str(dealer_score), "\nLe croupier est au dessus de 21.\nVous avez donc gagné.")
        money += bet
    elif player_score < dealer_score:
        print("Le total des cartes du croupier est égal à :", str(dealer_score), "\nLe croupier est au dessus de vous.\nVous avez donc perdu.")
        money -= bet
    elif player_score > dealer_score:
        print("Le total des cartes du croupier est égal à :", str(dealer_score), "\nVous êtes au dessus du croupier.\nVous avez donc gagné.")
        money += bet
    elif player_score == dealer_score:
        print("Le total des cartes du croupier est égal à :", str(dealer_score), "\nVous êtes à égalité.\nPar conséquent, vous êtes remboursés.")   

while 1:
    print("Votre solde est de :", money, "€")
    while 1:
        try:
            bet = int(input("Choissisez le montant que vous souhaitez parier : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide")
    input("Appuyez sur Entrée pour lancer la partie")
    cardsDropping(bet, money)