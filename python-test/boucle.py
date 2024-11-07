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

#  fonction range avec les paramettre start: valeur de départ, stop: valeur de fin , step: valeur incrémentation 

print("fonction range avec paramettre start,stop,step")
for i in range(2, 10, 2):
    print(i)