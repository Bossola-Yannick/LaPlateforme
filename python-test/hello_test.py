# -------------------PRINT INPUT TYPEOF-------------------------

print(type("hello, world") )
print(type(3))
print(type(3.5))

mon_entier = 12
ma_variable = "hello-world!"

print(ma_variable + str(mon_entier + 1))

age = input("quel est ton age ?")
print(age)

temperature = input("quelle est la temperature en °C ?")
print("il fait ", str(float(temperature) * 9/5 + 32 ), " °F")