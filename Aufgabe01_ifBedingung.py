import random

randomNumber = random.randint(1,100)
print(randomNumber) 

if randomNumber < 20:
    print("mini")
elif randomNumber < 50:
    print("medium")
else:
    print("large")
