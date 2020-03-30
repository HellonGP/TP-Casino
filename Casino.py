from random import randrange
from math import ceil

argent = 1000
continuer_partie = True

print("Tu as", argent, "$")

while continuer_partie:
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        print("Choisir entre")
        nombre_mise = input("0 et 49 : ")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Tu n'as rien saisi")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Nombre negatif")
        if nombre_mise > 49:
            print("Nombre superieur a 49")

    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Montant mise : ")
        try:
            mise = int(mise)
        except ValueError:
            print("Tu n'as rien saisi")
            mise = -1
            continue
        if mise <= 0:
            print("Mise negative / nulle")
        if mise > argent:
            print("Tu n'as rien saisi")

    numero_gagnant = randrange(50)
    print("La roulette tourne...", numero_gagnant)

    if numero_gagnant == nombre_mise:
        print("Bravo ! Vous gagnez", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2:
        mise = ceil(mise * 0.5)
        print("Bonne couleur ! Vous gagnez", mise, "$")
        argent += mise
    else:
        print("Perdu...")
        argent -= mise

    if argent <= 0:
        print("Vous etes ruine !")
        continuer_partie = False
    else:
        print("Tu as a present", argent, "$")
        print("Quitter le Casino ?")
        quitter = input("(o/n) ")
        if quitter == "o" or quitter == "O":
            print("Aurevoir")
            continuer_partie = False
            break
