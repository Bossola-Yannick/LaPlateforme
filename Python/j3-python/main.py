import math

# JOB 1
print("")
print("JOB 1 : ")
print("")
valeur_1 = input("Entrez un 1er nombre entier entre 1 et 10 : ")
valeur_2 = input("Entrez un 2eme nombre entier entre 1 et 10 : ")

if valeur_1 == valeur_2:
    print("Valeur 1 est égal à Valeur 2 ! ")
else:
    print("Valeur 1 et valeur 2 ne sont pas égal ! ")

print("")

# JOB 2
print("")
print("JOB 2 : ")
print("")
age = int(input("Votre Age : "))

if age > 18:
    print("Tu peux voter !")
else:
    print("tu ne peux pas voter !")

print("")

# JOB 3
print("")
print("JOB 3 : ")
print("")
ma_liste = []
for i in range(0,101):
    ma_liste.append(i)
    if i == 26 or i ==37 or i ==88:
        ma_liste.remove(i)
print(ma_liste)
        
print("")

# # JOB 4
# print("")
# print("JOB 4 : ")
# print("")
for i in range(0,36):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz / Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("")

# JOB 5
print("")
print("JOB 5 : ")

def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
for n in range(1,100):
    if is_prime(n) == True:
        print(n," est premier !")

print("")

# JOB 6
print("")
print("JOB 6 : ")

nombre = int(input("entrez un nombre entier : "))

if nombre % 2 == 0:
    print(f"le nombre {nombre} est pair !")
else:
    print(f"le nombre {nombre} est impair !")

print("")

# JOB 7
print("")
print("JOB 7 : ")

chaine = "abcdefghijklmnopqrstuvwxyz"

for i in chaine:
    if chaine.index(i) % 2 != 00:
        print(chaine[:chaine.index(i)])

print("")

# JOB 8
print("")
print("JOB 8 : ")

mes_nombres = []
ab= float(input("Entrez une valeur pour ab :"))
ac= float(input("Entrez une valeur pour ac :"))
bc= float(input("Entrez une valeur pour bc :"))
mes_nombres.append(ab)
mes_nombres.append(ac)
mes_nombres.append(bc)
plus_grand_nombre = max(mes_nombres)
mes_nombres.remove(plus_grand_nombre)

if plus_grand_nombre < mes_nombres[0] + mes_nombres[1]:
    print("Il est possible de faire un triangle avec ces mesures !")
    if plus_grand_nombre == mes_nombres[0] and plus_grand_nombre == mes_nombres[1]:
        print("Ce sera un triangle équilatéral !")
    elif plus_grand_nombre == mes_nombres[0] or plus_grand_nombre == mes_nombres[1] or mes_nombres[0] == mes_nombres[1]:
        print("Ce sera un triangle isocèle !")
    elif plus_grand_nombre * plus_grand_nombre == ((mes_nombres[0] * mes_nombres[0]) + (mes_nombres[1] * mes_nombres[1])):
        print("Ce sera un triangle rectangle !")
    else:
        print("Ce sera un triangle quelconque !")
else:
    print("Il n'est pas possible de tracer un triangle avec ces mesure !")

