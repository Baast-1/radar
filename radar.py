import time
import os
import random

TOURS = 10
VERT = "\033[92m"
ROUGE = "\033[91m"
RESET = "\033[0m" 

cibles = []
for i in range(3):
    ligne_cible = random.randint(0, TOURS - 1)
    colonne_cible = random.randint(0, TOURS - 1)
    position = [ligne_cible, colonne_cible]
    cibles.append(position)

for balayage in range(TOURS):
    os.system("clear")
    print(VERT+ """
            ==============================
                        RADAR
            ==============================
            """ + RESET
        )
    for ligne in range(TOURS):
        for colonne in range(TOURS):
            if colonne == balayage:
                print(VERT + "|" + RESET, end=" ")
            elif [ligne, colonne] in cibles and colonne < balayage:
                print(ROUGE + "●" + RESET, end=" ")
            else:
                print(VERT + "." + RESET, end=" ")
        print()
    for cible in cibles:
        if cible[1] < balayage:
            print(f"Cible en ligne {cible[0]}, colonne en {cible[1]}")
    time.sleep(1)
