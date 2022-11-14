

import board
import busio
import adafruit_bmp280
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
# Sensor als Objekt erstellen in Abhaengigkeit von I2C
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
# Dieser Wert muss an den aktuellen Luftdruck Ihres Standorts geaendert werden
# ansonsten kommt es zu Ungenauigkeiten
# Wetterdienste koennen Ihnen Auskunft geben
# 1013.25 hPa ist der mittlere Luftdruck auf Meereshoehe
sensor.sea_level_pressure = 1013.25
# Ausgabe der Messwerte
while True:
    if sensor.temperature < 30:
        GPIO.output(17, True)
        GPIO.output(22, False)
        GPIO.output(27, False)
    elif sensor.temperature < 35:
        GPIO.output(17, False)
        GPIO.output(22, False)
        GPIO.output(27, True)
    else:
        GPIO.output(17, False)
        GPIO.output(22, True)
        GPIO.output(27, False)