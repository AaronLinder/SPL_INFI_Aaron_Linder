import random

def addition():
    zahl1 = int(input())
    zahl2 = int(input())
    summe = zahl1 + zahl2
    return summe


def randomint():
    randomNumber = random.randint(100,200)
    return randomNumber

def wort():
    i = int(input())
    array = ["Aaron", "Luca M.", "Luca f."]
    return array[i]


print(addition())
print(randomint())
print(wort())
