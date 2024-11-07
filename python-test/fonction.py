# ----------------- FONCTION -------------------------------------

def ma_fonction():
    ma_variable = 1
    print("ma variable est", ma_variable)


ma_fonction()

#  ----------------- Paramettre de variable ---------------------

def ma_new_fonction(ma_new_variable=13):
    print("ma nouvelle variable est", ma_new_variable)


ma_new_fonction(42)
ma_new_fonction()

#  ---------------- Projet 4 --------------------------

def mon_range(a):
    l = []
    i = 0
    while i < a:
        l.append(i)
        i += 1
        
    return l


print(mon_range(6))

