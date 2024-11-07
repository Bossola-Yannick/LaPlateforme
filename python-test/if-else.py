# ---------------------IF ELSE ELIF COMPARATEUR-------------------------------

note = input("votre moyenne au BAC ?")
if int(note) >= 12 and int(note) < 14:
    print("assez bien!")
elif int(note) >= 14 and int(note) < 16:
    print("Bien!")
elif int(note) >= 16 and int(note) < 18:
    print("très bien!!")
elif int(note) >= 18:
    print("félicitation")
else:
    print("tu est une quiche!!!")