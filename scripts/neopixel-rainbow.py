# example use of neopixel library to create moving rainbow effect

# note that PWM pins are required for neopixels
# PWM0 - GPIO 12,18
# PWM1 - GPIO 13,19

import time
from neopixel import *

NUM_PIXELS = 60
LED_PIN = 18
BRIGHTNESS = 255

# setPixelColor takes in a Color object as a parameter, hence the need for conversion
def rgb(r=0,g=0,b=0):
        return Color(g,r,b)

RED = rgb(255,0,0)
ORANGE = rgb(255,127,0)
YELLOW = rgb(255,255,0)
GREEN = rgb(0,255,0)
BLUE = rgb(0,0,255)
INDIGO = rgb(75,0,130)
VIOLET = rgb(148,0,211)

colors = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET][::-1]


def initLED():
        global strip
        strip = Adafruit_NeoPixel(NUM_PIXELS, LED_PIN)
        strip.begin()
        strip.setBrightness(BRIGHTNESS)
        strip.show()

def rainbow():
        n = len(colors)

        for i in range(NUM_PIXELS):
                for j in range(NUM_PIXELS):
                        strip.setPixelColor((i+j)%NUM_PIXELS, colors[j%n])
                strip.show()
                time.sleep(0.1)
