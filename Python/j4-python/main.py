# JOB 1
print("")
print("JOB 1 : ")

def my_print_hello():
    print("Hello World")

my_print_hello()

print("")

# JOB 2
print("")
print("JOB 2 : ")
name = input("Votre prénom ? : ")
def my_print_name(name):
    print(f"Ton nom est {name}. ")
my_print_name(name)

print("")
# JOB 3
print("")
print("JOB 3 : ")

a = int(input('entrez votre 1er nombre : '))
b = int(input('entrez votre 2eme nombre : '))
def add(a, b):
   print(f"résultat de {a} + {b} = ", a + b)

add(a, b) 

print("")
# JOB 4
print("")
print("JOB 4 : ")

def get_hello():
    print("Hello La Plateforme")
get_hello()
 
print("")
# JOB 5
print("")
print("JOB 5 : ")

num1 = float(input("entrez un nombre : "))
operator = (input("entrez un opérateu : +, -, *, /, % "))
num2 = float(input("entrez un nombre : "))
def calcule(num1, operator, num2):
    if operator == "+":
        print(f"Le resultat de {num1} {operator} {num2} = ", num1 + num2)
    elif operator == "-":
        print(f"Le resultat de {num1} {operator} {num2} = ", num1 - num2)
    elif operator == "*":
        print(f"Le resultat de {num1} {operator} {num2} = ", num1 * num2)
    elif operator == "/":
        print(f"Le resultat de {num1} {operator} {num2} = ", num1 / num2)
    elif operator == "%":
        print(f"Le resultat de {num1} {operator} {num2} = ", num1 % num2)

calcule(num1, operator, num2)


print("")
# JOB 6
print("")
print("JOB 6 : ")

my_nombre = int(input("entrez un nombre positif ou négatif : "))
def nombre(a):
    if a > 0:
        print("Positif !")
    elif a < 0:
        print("Négatif ! ")
    else:
        print("Votre nombre est 0 !")

nombre(my_nombre)

print("")
# JOB 7
print("")
print("JOB 7 : ")
my_language = input('entrez votre language de programation : ')

def langage(a):
    if a == "Javascript":
        print(" Tu est un Dev Web")
    elif a == "Python":
        print(" Tu est un Dev IA")
    elif a == "java":
        print(" Tu est un Dev logiciel")
    elif a == "reactjs":
        print(" Tu est un Dev Mobile")
    else:
        print("Un jour, je serai le meilleur développeur")

langage(my_language)

print("")
# JOB 8
print("")
print("JOB 8 : ")

type = input("Entrez le type fruits ou légumes : ")
saison = input("Entrez une saison : été ou hiver : ")
def equilibre(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "été":
            print("Poire, fraise et cassis")
    elif type == "légumes":
        if saison == "hiver":
            print("carotte, topinambour et endive")
        elif saison == "été":
            print("artichaud, aubergine et navet")
equilibre(type, saison)
print("")
# JOB 9
print("")
print("JOB 9 : ")

notes = input("Entrez vos note : ").split()

def moyenne(notes):
    total = 0
    for i in notes:
        total += int(i)
    moyenne = total / len(notes)
    if 15 <= moyenne <= 20 :
        print(f"Trés bon élève, moyenne : {moyenne}")
    elif 11 <= moyenne < 15 :
        print(f"Bon élève, moyenne : {moyenne}")
    elif 8 <= moyenne < 11 :
        print(f"Elève moyen, moyenne : {moyenne}")
    elif 0 <= moyenne < 8 :
        print(f"T'est Nul à chier !, moyenne : {moyenne}")

moyenne(notes)

print("")
# JOB 10
print("")
print("JOB 10 : ")

def pair_impair(number):
        if number >= 0:
            if number % 2 == 00:
                print("le nombre est pair !")
            elif number % 2 != 00:
                print("le nombre est impair !")
        else:
            print("Le nombre DOIT être positif !")
            number = input("Entrez un nombre : ")
            pair_impair(number)


number = input("Entrez un nombre : ")

pair_impair(int(number))

print("")
# JOB 11
print("")
print("JOB 11 : ")
number = int(input('donnez un nombre ! : '))

def time_to_text(number):
    conversion = number / 60
    heure = int(conversion)
    minute = int((conversion - heure) * 60)
    print(f"{heure} heures, {minute} minutes")
    
time_to_text(number)

print("")

# BONUS
print("BONUS")

name = input("entrez votre nom : ")

def inverso(name):
    name = list(name)
    back_name = []
    while len(back_name) != len(name):
        for i in name[::-1]:
            back_name.append(i)
    reverse_name = ''.join(back_name)
    print(reverse_name)

inverso(name)

