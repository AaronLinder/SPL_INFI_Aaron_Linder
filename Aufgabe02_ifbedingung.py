import random

randomNumber = random.randint(1,100)
randomNumber2 = random.randint(1,100)

print(randomNumber)
print(randomNumber2)

if randomNumber < randomNumber2 and randomNumber < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")
if randomNumber < 30 or randomNumber2 < 30:
    print("Eine der beiden ist kleiner als 30")
if randomNumber < 50 and randomNumber2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")
