class Cybertruck:
    marque = "Tesla"
    model = "Cybertruck"
    annee = 2023

    def klaxonner(self):
        print("bip bip !!")


cybertruck = Cybertruck()

# accedé à une valeur de la class
print("pour voir la marque :", cybertruck.marque)

# faire klaxonner la voiture
print("avance abruti :")
cybertruck.klaxonner()

# constructur afin de pouvoir créer differente voiture et non pas juste une

class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque =marque
        self.modele = modele
        self.annee = annee

    def klaxon(self):
        print("je vais t'arracher les yeux tête de cul!!!!")


# création de voiture

leon = Voiture(marque="SEAT", modele="Leon", annee="2016") 
subaru = Voiture(marque="SUBARU", modele="Impresa", annee="2023")

class Pizza:
    def __init__(self, base, ingredient,taille, prix):
        self.base = base
        self.ingredient = ingredient
        self.prix = prix
        self.taille = taille

    def add_ingredient(self, new_ingredient):
        if new_ingredient == "ananas":
            print("BOOM! on ne mettra jamais d'ananas sur la pizza. CAPICE!!")
        self.ingredient.append(new_ingredient)
        self.prix = self.prix +1


base = input("tomate ou blanche ?")

taille = input("quelle taille m ou xl ?")

ingredient = input ("quelle garniture ?")

ingredient = ingredient.split(", ")

if taille == "m":
    prix = 5 + len(ingredient)
elif taille == "xl":
    prix = 7 +len(ingredient)
    
pizza = Pizza(
    base = base,
    ingredient = ingredient,
    prix = prix,
    taille = taille
)
print("Vous avez commendé une pizza base :", pizza.base)
print("Vous avez commendé une pizza taille :", pizza.taille)
print("Avec une garniture composées de :", pizza.ingredient)
print("Cela coutera :", pizza.prix,"€")