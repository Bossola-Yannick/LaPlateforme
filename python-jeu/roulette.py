# ------------------------- Duel -------------------------------
import random

bullet = random.randint(1, 6)
bullet_out = {0}
bullet_in_gun = 6

playeur = 1

billy = 1

print("Hey gringo! tu est prêt à mourir?")

while bullet_in_gun != 0 and playeur != 0 and billy != 0:
    bullet_choice = int(input("allez fait tourné le barillet et tire! choisir un chiffre entre 1 et 6 : "))
    if bullet_choice in bullet_out:
        print("EH GRINGO me prend pas pour un jambon et fait mieux tourner que ca !")
        print (bullet_out)        
        bullet_choice = int(input("choisir un nombre qui n'as pas été déjà pris : "))
    if bullet_choice == bullet:
        print("BOOM! HAHAHA t'est mort Gringo!")
        playeur -= 1
        break
    bullet_out.add(bullet_choice)
    print (bullet_out)

    print("A moi de faire tourner, vzzz click!")
    bullet_choice = random.randint(1 , 6)
    if bullet_choice in bullet_out:
        bullet_choice = random.randint(1, 6)
    bullet_out.add(bullet_choice)
    print(bullet_out)
    if bullet_choice == bullet:
        print("BOOM! han gr..ingo...tu..m'..as...eu")
        print("Tu as gagné ce duel! Survivra tu au prochain?")
        billy -= 1
    

    
     
   
   