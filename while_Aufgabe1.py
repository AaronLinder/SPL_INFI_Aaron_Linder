import random

summe = 0
randomNumber = 0

while True:
    randomNumber = random.randint(10,30)
    if randomNumber == 15 or randomNumber == 25:
        break
    summe =  summe + randomNumber
    print(randomNumber)

print(summe)