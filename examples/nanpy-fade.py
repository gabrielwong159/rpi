# docs - https://github.com/nanpy/nanpy

from nanpy import ArduinoApi, SerialManager
from time import sleep

connection = SerialManager()
a = ArduinoApi(connection=connection)

LED = 13
brightness = 0
fadeAmount = 5

a.pinMode(LED, a.OUTPUT)

while True:
    a.analogWrite(LED, brightness)
    brightness+= fadeAmount

    if brightness == 0 or brightness == 255:
        fadeAmount = -fadeAmount

    sleep(0.03)

""" other basic functions - ArduinoApi.py
a.digitalRead(pin)
a.digitalWrite(pin, value)
a.analogRead(pin)
a.analogWrite(pin, value)
a.millis()
a.pulseIn(pin, value)
a.shiftOut(dataPin, clockPin, bitOrder, value)
"""
