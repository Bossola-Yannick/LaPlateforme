# Job 1 affichage des chiffres dans le terminal
print("JOB 1")
for i in range(21):
    print(i)

# Job 2 affichage des chiffres 1/2
print("JOB 2")
for i in range(0,20,2):
    print(i)

# Job 3 affchage du carré des chiffre
print("JOB 3")
for i in range(21):
    print(i*i)
2
# Job 4 affichage des tables de multiplication de 1 à N (N = input)
print("JOB 4")
limite = int(input("Entrez un entier supérieur à zéro : "))
N=1
while N <= limite:
    print("table de multiplication de", N, ":")
    for i in range(1,11):
        print( N, "x", i, "=", N*i)
    N += 1

# Job 5 transformation de for en while
print("JOB 5")
for N in range(1,13):
    print(N)
nombre = 1
while nombre < 13:
    print(nombre)
    nombre += 1

# Job 6 affichage resultat de multiplication de M par 7
print("JOB 6")
M = int(input("rentrez un entier : "))
while M >= 0:
    print(M, "x 7" "=", M*7)
    M -= 1

# Job 7
print("JOB 7")
X, tour, les_tours = 12, [], []
while X >= 1:
    tour.append(X)
    les_tours.append(X*3-2)
    X -= 1
if len(tour) == 12:
    tour.reverse()
    les_tours.reverse()
    for i in tour:   
        print("Tour", tour[i-1], ": ", les_tours[i-1])
        
# Job 8
print("JOB 8")
X, tour, les_tours = 12, [], []
while X >= 1:
    tour.append(X)
    les_tours.append(X*2)
    X -= 1
if len(tour) == 12:
    tour.reverse()
    les_tours.reverse()
    for i in tour:   
        print("Tour", tour[i-1], ": ", les_tours[i-1])

# job 7 et 8 mais en boucle for
print("JOB 7 et 8")
for i in range(1, 13):
    print("tour", i, " : ", i*3-2)

for i in range(1, 13):
    print("tour", i, " : ", i * 2)

# Job 9
print("JOB 9")
pair_1 = []
impair_2 = []
for i in range(1,30):
    if (i % 2) == 0:
        pair_1.append(i)
    else:
        impair_2.append(i)
print(f"Les nombres pairs sont : {pair_1}")
print(f"Les nombres impairs sont : {impair_2}")


# Job 10 entré des nombres et il seront classé en pairs ou impairs
print("JOB 10")
nombre = []
pair = []
impair = []

while len(nombre) <= 5:
    n = int(input("Veuillez entrer un nombre entier : "))
    nombre.append(n)
    if ( n % 2) == 0:
        pair.append(n)
    elif (n % 2) != 0:
        impair.append(n)
print("les nombres choisis sont : ", nombre)    
print("les nombres", pair, "son pairs !" )
print("les nombres", impair, "son impairs !" )
