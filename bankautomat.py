summe = 0

while True:
    print("Selektieren sie die gewünschte Funktion: \n 1. Einzahlen \n 2. Abheben \n 3. Kontostand \n 4. Ende")
    eingabe = int(input())

    if eingabe == 1:
        print("Wie viel wollen Sie einzahlen \n")
        geld = int(input())
        summe += geld
    elif eingabe == 2:
        print("Wie viel wollen Sie abheben \n")
        geld = int(input())
        summe -= geld
    elif eingabe == 3:
        print(summe)
    elif eingabe == 4:
        break
    else:
        print("unglültige Eingabe \n")