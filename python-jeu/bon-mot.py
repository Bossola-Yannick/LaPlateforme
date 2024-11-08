#  --------------- projet pendu -------------------------
import random

print("Peut tu trouver le mot auquel je pense?")

ma_liste = [
    "banane", "pomme", "poire", "fraise", "orange", "kiwi", "prune", "melon", "mandarine",
    "abricot", "mangue", "cerise", "nectarine", "framboise", "myrtille", "raisin", "figue", "pêche",
    "grenade", "pamplemousse", "mandarine", "litchi", "papaye", "cantaloup", "pistache", "amande",
    "noisette", "noix", "coco", "avocat", "tomate", "carotte", "poivron", "courgette", "concombre",
    "aubergine", "chou", "brocoli", "haricot", "pois", "radis", "navet", "salade",
    "épinard", "roquette", "basilic", "menthe", "persil", "thym", "romarin", "ciboulette", "estragon",
    "origan", "lavande", "sauge", "fenouil", "moutarde", "ail", "oignon", "échalote", "gingembre",
    "curcuma", "cumin", "paprika", "coriandre", "cardamome", "sel", "poivre", "sucre", "farine",
    "riz", "pâtes", "pain", "boulangerie", "fromage", "beurre", "lait", "yaourt", "crème", "œuf",
    "saucisse", "bacon", "poulet", "dinde", "bœuf", "agneau", "poisson", "thon", "saumon", "truite",
    "langoustine", "crevette", "moules", "calamar", "huître", "escargot", "pizza", "hamburger",
    "sandwich", "soupe", "salade", "quiche", "tarte", "gâteau", "biscuit", "chocolat", "bonbon", 
    "glace", "crêpe", "pain au chocolat", "croissant", "brioche", "gaufre", "macaron", "pâtisserie"
]
mystery = random.choice(ma_liste)

response = "_" * len(mystery)

life = 10

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