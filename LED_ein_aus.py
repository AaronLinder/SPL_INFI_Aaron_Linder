import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
while True:
    userInput = input("Geben Sie e für Licht ein bzw. a für Licht aus ein")
    if userInput == "e":
        GPIO.output(3,True)

    elif userInput == "a":
        GPIO.output(3,False)
    else:
        print("Geben Sie e oder a ein")