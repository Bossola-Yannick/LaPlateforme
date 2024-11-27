import random

#  Job 2 
print(10 + 3)

#  Job 4
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(alphabet)

# Job 5
alphabet.reverse()
print(alphabet)

# Job 6
ma_string = "Je suis une string"
print(ma_string)

# Job 7
num1, num2 = 40, 2
print(num1 + num2)

# Job 8
num1, num2 = 3, 14
print(num1 * num2)

# Job 9
print("GESTION DU STOCK")
name = "pikachu"
prix_unit = 10
reste_stock = 0
jour = 1
vente_day = 0

next_day = input("passer au jour suivant ?  oui ou non ")

while next_day == "oui":
    vente_day = random.randint(1, 5)
    livraison = int(input("j'en ai reçu :"))
    reste_stock = livraison + reste_stock
    print("j'ai", reste_stock, name, "en stock au prix de", prix_unit,"€ l'unité")
    while vente_day > 0:
        achat = int(input("Veuillez sélectionner la quantité voulut : "))
        if achat <= reste_stock:
            prix_achat = achat * prix_unit
            print("Votre total d'acaht est de :", prix_achat,"€")
            reste_stock = reste_stock - achat
            print("Il reste", reste_stock, name, "en stock")
            vente_day -= 1
            if reste_stock == 0:
                print("Plus de stock !")
                break
        elif achat >= reste_stock:
            print("Désolé, nous ne pouvons donner suite à votre demande. il nous reste que :", reste_stock, "pikachu !")
    next_day = input("passer au jour suivant ?  oui ou non ")
    jour += 1
    prix_unit = (prix_unit * 1.01)
    print("Suite à la demande, les", name, "coute 10% plus chère, soit", prix_unit, "€ pour le jour:", jour)
    if next_day == "non":
        print("Dommage le magasin est en liquidation judiciaire ! ")
print("Dommage le magasin est en liquidation judiciaire ! ")


# Job 10 initialisation du compte d'investissement avec taux 
print("CALCUL DU RENDEMENT D'INVESTISSEMENT")
montant_investi = 0
montant_depot = 0
montant_retrait = 0

def mon_investissement():
    taux_annuel = 5
    if montant_investi >= 15000:
        taux_annuel += 15
    elif 10000 <= montant_investi < 15000:
        taux_annuel += 5
    else:
        taux_annuel = 2
    new_rendement = (montant_investi * taux_annuel) / 100
    return print("Le gain annuel est de votre dépot de base est de :", new_rendement, "€, pour un montant investi de :", montant_investi, "€ et un taux de : ", taux_annuel, "%")

operation = input('Veuillez choisir quelle opération vous désirez faire : dépot ou retrait ou fini ? ')

while operation != "fini":
    if operation == "dépot":
        montant_depot = int(input("Veuillez indiquer le montant déposé : "))
        montant_investi =  montant_investi + montant_depot
        mon_investissement()
        operation = input('Veuillez choisir quelle opération vous désirez faire : dépot ou retrait ou fini ? ')
    elif operation == "retrait":
        montant_retrait = int(input("Veuillez indiquer votre retrait : "))
        if montant_retrait > montant_investi:
            print("Désolé mais tu n'est pas aussi riche que cela !!! Reste réaliste!")
            operation = input('Veuillez choisir quelle opération vous désirez faire : dépot ou retrait ou fini ? ')
        else:    
            montant_investi =  montant_investi - montant_retrait
            mon_investissement()
            operation = input('Veuillez choisir quelle opération vous désirez faire : dépot ou retrait ou fini ? ')
    else:
        print("Nous n'avons pas compris votre commande")
        operation = input('Veuillez choisir quelle opération vous désirez faire : dépot ou retrait ou fini ? ')

print("Merci de votre visite.")

# Job bonus
print("IL Y AS T'IL UN E DANS LE MOT")
reponse = input("Faire un essai : yes or no ")

while reponse != "no":
    if reponse == "yes":
        le_mot = input("Veuillez entrer un mot : ")
        if "e" in le_mot:
            print( "Votre mot est :",le_mot,". La lettre 'e' est dans votre mot !")
            reponse = input("Faire un essai : yes or no ")
        else:
            print("Votre mot est :",le_mot,". Il n'y as pas de 'e' dans votre mot !")
            reponse = input("Faire un essai : yes or no ")
    elif reponse != "no" and reponse != "yes":
        print("Je n'ai pas compris votre réponse")
        reponse = input("Faire un essai : yes or no ") 

print("Bonne journée")   



    






