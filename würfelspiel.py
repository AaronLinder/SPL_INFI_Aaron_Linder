import random

while True:
    summe = 0
    summeComputer = 0
    print("Selektieren sie die gewünschte Funktion: \n 1. Spielen \n 2. Spiel Benenden \n")
    eingabe = int(input())

    if eingabe == 1:
        i = 0
        while i < 6:
            print("Selektieren sie die geünschte Option: \n 1. Würfeln \n 2. Spiel Abbrechen")
            eingabe = int(input())
            if eingabe == 1:
                würfel1 = random.randint(1,6)
                würfel2 =random.randint(1,6)
                summe = summe + würfel1
                summeComputer = summeComputer + würfel2
                print("Sie haben eine" , würfel1 , " gewürfelt, der Computer hat eine " , würfel2 , " gewürfelt \n ihr Augensumme ist " , summe , "\n die Augensumme des Computers ist " , summeComputer, "\n")
            elif eingabe == 2:
                break
            else:
                print("unglültige Eingabe \n")
            i = i +1
        if summe < summeComputer:
            print("Der Computer Hat gewonnen \n")
        elif summe > summeComputer:
            print("Sie haben gewonnen")
        else:
            print("Unentschieden")
    elif eingabe == 2:
        break
    else:
        print("unglültige Eingabe \n")