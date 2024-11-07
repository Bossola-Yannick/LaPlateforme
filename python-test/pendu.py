#  --------------- projet pendu -------------------------
print("ON VA JOUER ENSEMBLE")


mystery = "python"

response = "_" * len(mystery)

life = 7



while life > 0 and mystery != response: 
    letter = input("entrée une lettre: ")

    if letter in mystery:
        for i in range(len(mystery)):
            if mystery[i] == letter:
                response = response[:i] + letter + response[i + 1:]
    else:
        life -= 1

    if response == mystery:
        print('BRAVO!! le mot est:', mystery)
    elif life == 0:
        print("Dommage c'est perdu, le mot mystère est", mystery)
    else:
        print("il vous reste:",life, "vie")
        print("le mot cherché est:", response)