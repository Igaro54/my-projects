from tkinter import *
import random as rand
from functools import partial

choices = ["Pierre", "Feuille", "Ciseaux"]
score = 0
result = ""

def bot(): 
    return rand.choice(choices)

def rock():
    global score
    botChoice = bot()
    if botChoice == "Ciseaux":
        print("-------------------\nLe choix de l'ordinateur est {0}.\nBien joué, vous avez gagné un point.\n-------------------".format(botChoice))
        score += 1
        resultText.config(text="Le choix de l'ordinateur est {0}.\nBien joué, vous avez gagné un point.".format(botChoice))
    elif botChoice == "Feuille":
        print("-------------------\nLe choix de l'ordinateur est {0}.\nAïe, vous venez de perdre un point.\n-------------------".format(botChoice))
        score -= 1
        resultText.config(text="Le choix de l'ordinateur est {0}.\nAïe, vous venez de perdre un point.".format(botChoice))
    elif botChoice == "Pierre":
        print("-------------------\nLe choix de l'ordinateur est {0}.\nEgalité, votre score ne bouge pas.\n-------------------".format(botChoice))
        resultText.config(text="Le choix de l'ordinateur est {0}.\nEgalité, votre score ne bouge pas.".format(botChoice))
    scoreText.config(text="Score : {}".format(score))

def paper():
    global score
    botChoice = bot()
    if botChoice == "Ciseaux":
        print("-------------------\nLe choix de l'ordinateur est {0}.\nAïe, vous venez de perdre un point.\n-------------------".format(botChoice))
        score -= 1
        resultText.config(text="Le choix de l'ordinateur est {0}.\nAïe, vous venez de perdre un point.".format(botChoice))
    elif botChoice == "Feuille":
        print("-------------------\nLe choix de l'ordinateur est {0}.\nEgalité, votre score ne bouge pas.\n-------------------".format(botChoice))
        resultText.config(text="Le choix de l'ordinateur est {0}.\nEgalité, votre score ne bouge pas.".format(botChoice))
    elif botChoice == "Pierre":
        print("-------------------\nLe choix de l'ordinateur est {0}.\nBien joué, vous avez gagné un point.\n-------------------".format(botChoice))
        score += 1
        resultText.config(text="Le choix de l'ordinateur est {0}.\nBien joué, vous avez gagné un point.".format(botChoice))
    scoreText.config(text="Score : {}".format(score))

def cisor():
    global score
    botChoice = bot()
    if botChoice == "Ciseaux":
        print("-------------------\nLe choix de l'ordinateur est {0}.\nEgalité, votre score ne bouge pas.\n-------------------".format(botChoice))
        resultText.config(text="Le choix de l'ordinateur est {0}.\nEgalité, votre score ne bouge pas.".format(botChoice))
    elif botChoice == "Feuille":
        print("-------------------\nLe choix de l'ordinateur est {0}.\nBien joué, vous avez gagné un point.\n-------------------".format(botChoice))
        score += 1
        resultText.config(text="Le choix de l'ordinateur est {0}.\nBien joué, vous avez gagné un point.".format(botChoice))
    elif botChoice == "Pierre":
        print("-------------------\nLe choix de l'ordinateur est {0}.\nAïe, vous venez de perdre un point.\n-------------------".format(botChoice))
        score -= 1
        resultText.config(text="Le choix de l'ordinateur est {0}.\nAïe, vous venez de perdre un point.".format(botChoice))
    scoreText.config(text="Score : {}".format(score))

window = Tk()

text = Label(window, text="Choisissez quel symbole jouer")
text.pack()

gridMain = PanedWindow(window, orient=HORIZONTAL)
gridMain.pack(side=TOP, padx=2, pady=2)

gridMain.add(Button(gridMain, text="Pierre", command=partial(rock), padx=10, borderwidth=4))

gridMain.add(Button(gridMain, text="Feuille", command=partial(paper), padx=10, borderwidth=4))

gridMain.add(Button(gridMain, text="Ciseaux", command=partial(cisor), padx=10, borderwidth=4))

scoreText = Label(window, text="Score : {}".format(score))
scoreText.pack()

resultText = Label(window, text=result)
resultText.pack()

window.mainloop()