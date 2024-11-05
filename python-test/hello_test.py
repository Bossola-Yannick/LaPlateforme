# -------------------PRINT INPUT TYPEOF-------------------------

# print(type("hello, world") )
# print(type(3))
# print(type(3.5))

# mon_entier = 12
# ma_variable = "hello-world!"

# print(ma_variable + str(mon_entier + 1))

# age = input("quel est ton age ?")
# print(age)

# (0 °C × 9/5) + 32 = 32 °F

# temperature = input("quelle est la temperature en °C ?")
# print("il fait ", str(float(temperature) * 9/5 + 32 ), " °F")


# ---------------------IF ELSE ELIF COMPARATEUR-------------------------------

# note = input("votre moyenne au BAC ?")
# if int(note) >= 12 and int(note) < 14:
#     print("assez bien!")
# elif int(note) >= 14 and int(note) < 16:
#     print("Bien!")
# elif int(note) >= 16 and int(note) < 18:
#     print("très bien!!")
# elif int(note) >= 18:
#     print("félicitation")
# else:
#     print("tu est une quiche!!!")

# -----------------LISTE (tableau)---------------------------

ma_liste = [42, "vache", 1.3]
print(ma_liste)
# append permet de rajouté un élément à la liste
# ma_liste.append(12)
# print(ma_liste)
# remove permet de supprimer une valeur 
ma_liste.remove(1.3)
print(ma_liste)
# le 'in' permet de savoir si un élément est présent dans la liste
print(3 in [1,2,3,4,5,6])

# ------------------boucle WHILE ---------------------------
print('boucle while')
i = 0
while i <= 2:
    print(i)
    i += 1 

# ------------------boucle FOR ---------------------------
print('boucle for')
for lettre in ['a','b','c']:
    print(lettre)

print('boucle for un nombre de foi précise')
for i in range(5):
    print(i)

#  --------------- projet pendu -------------------------
print("trouve une lettre du mot mystère")

mystery = "python"
life = 7

while life > 0:
    letter = input("entrée une lettre: ")
    if letter in mystery:
        print(mystery)
    else:
        life -= 1
        print('il vous reste',life,'chance')
