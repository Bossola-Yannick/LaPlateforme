import random

taille_grille = 5 
axe_x = random.randint(1, taille_grille)
axe_y = random.randint(1, taille_grille)

zone = ["~"]
tir_loupe = []
bullet = 5
couler = False
mon_tir = []

# grille = [["~"] * taille_grille for _ in range(taille_grille)]

def grille_builder():
    for _ in range(taille_grille):
        grille = zone * taille_grille 
        print(" ".join(grille))
grille_builder()

bateau = str(axe_y), str(axe_x)
print("le bateau est en :", bateau)

while bullet > 0 and couler != True:
    
    bateau_x = input("Choisissez un emplacement pour l'axe x (chiffre entre 1 et 5): ")
    bateau_y = input("Choisissez un emplacement pour l'axe y (chiffre entre 1 et 5): ")
    mon_tir = bateau_x, bateau_y
    if mon_tir in tir_loupe:
        print('Vous avez déjà tiré dans cette case, Try Again!')
        print(tir_loupe)
    elif int(bateau_x) > 5 or int(bateau_y) > 5:
        print("veuillez tirer dans la zone de tir, les civils ne sont pas des cible!")
    else:
        tir_loupe.append(mon_tir)
        if mon_tir == bateau:
            print('BOOM le petit bateau')
            grille_builder()
            couler = True
            break
        elif mon_tir != bateau:
            print('Loupé!!')
            bullet -= 1
    grille_builder()
    print("Tir restant : ", bullet)

if bullet == 0:
    print("DOMMAGE! Le bateau était caché en : ", bateau)

