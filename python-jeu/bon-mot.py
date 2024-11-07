#  --------------- projet pendu -------------------------
import random

print("Peut tu trouver le fruit auquel je pense?")

ma_liste = ["banane", "pomme", "poire", "fraise", "orange", "kiwi", "prune", "melon", "mandarine"]
mystery = random.choice(ma_liste)

response = "_" * len(mystery)

life = 1

letter_response = []


while life > 0 and mystery != response: 
    print(response)
    letter = input("entrée une lettre: ")
    letter_response.append(letter)
    print(letter_response)
    if letter in mystery:
        for l in range(len(mystery)):
            if  mystery[l] == letter:
                response = response[:l] + letter + response[l + 1:]

    else:
        life -= 1

    if response == mystery:
        print('BRAVO!! le mot est:', mystery)
    elif life == 0:
        print("Dommage c'est perdu, le mot mystère est", mystery)
    else:
        print("il vous reste:",life, "vie")
        print("le mot cherché est:", response)