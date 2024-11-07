# --------------------- projet Juste Prix ---------------------------
import random
print("Trouverez vous le juste prix")

mystery_number = random.randint(1, 100)

my_response = ""

life = 10

trial_number = 0

while life > 0 and mystery_number != my_response:
    my_response = int(input(" veuillez choisir un chiffre entre 1 et 100 "))
    trial_number += 1
    life -= 1
    print("your life :", life)
    if my_response < mystery_number:
        print("le nombre recherché est plus grand!")
    elif my_response > mystery_number:
        print("le nombre recherché est plus petit")
    elif my_response == mystery_number:
        print(" BRAVO tu as réussi à trouver le nombre mystère en : ", trial_number, "coups")