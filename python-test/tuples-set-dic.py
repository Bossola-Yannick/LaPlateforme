# --------------------------- TUPLES -----------------------
# les tuples sont imuable a la differences des liste
# on peut utiliser 2 methodes sur les tuples count & index
# index nous donne l'index de l'élément désigné
# count nous donne le nombre de foi que l'élément est dans le tuples
nombre = (1,3,2,3,4,3)
nombres = (1,2,3,4,5)

print(nombre.count(3)) # il y as 3 fois le chiffre 3
print(nombres.index(3)) # le chiffre 3 est à l'index 2

# ------------------------- SET --------------------------
# pas d'ordre précis et pas de doublon, pas possible de sélectionné un index ou de modifié une valeur
set_de_nombre = { 3,4,2,4,1,0,2,3}

print("valeur du set :",set_de_nombre)

    #possible d'ajouter une valeur
set_de_nombre.add(5)
print("ajout du 5 :",set_de_nombre)

    #possible de retirer une valeur
set_de_nombre.remove(0)
print("retrait du 0 :",set_de_nombre)

    # unir plusieur set = union()
    # voir les commun de plusieur set = intersection()
    # voir les différences entre le set selectionné et un autre set = difference()

set_1 = {1,2,3}
set_2 = {4,5,6}
set_3 = {1,2,3}
set_4 = {2,3,4}

print("union :", set_1.union(set_2))
print("intersection :",set_2.intersection(set_4))
print("différence :", set_2.difference(set_4))
print("différence :", set_4.difference(set_2))


# ------------------------- DICTIONNAIRE --------------------------
# type d'ensemble clef valeur avec un ordre précis, pas de doublon de clef possible

nombres = { "un":1, "deux":2, "trois":3, "autre":1}
print("valeur :", nombres["un"])

# pour voir une valeur mais qu'elle n'existe pas = get()
print("recherche valeur innexistante :", nombres.get("cinq"))

# modifié ou ajouter une nouvelle paire clef/valeur = update()
nombres.update({"cinq":5})
print("ajout d'une clef/valeur", nombres )
nombres.update({"un":2})
print("modification clef/valeur", nombres )

# retirer une Clef/valeur
nombres.pop("autre")
print("retirer la clef/valeur autre=1 :", nombres)

# recupérer toute les clef = keys
print("les clefs de mon dico :", nombres.keys())
# recupérer toute les valeurs = values
print("les valeurs de mon dico :", nombres.values())

# faire une liste de tuple contenant les paires clef/valeur = items()
print("les items clef/valeur de mon dico :", nombres.items())
