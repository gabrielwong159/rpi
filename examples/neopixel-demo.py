# note that PWM pins are required for neopixels
# PWM0 - GPIO 12,18
# PWM1 - GPIO 13,19

import time
from neopixel import *

NUM_PIXELS = 60
LED_PIN = 18
BRIGHTNESS = 255

strip = Adafruit_NeoPixel(NUM_PIXELS, LED_PIN)
strip.begin()
strip.setBrightness(BRIGHTNESS)
strip.show()

GREEN = Color(255,0,0)
RED = Color(0,255,0)
BLUE = Color(0,0,255)

ORANGE = Color(127,255,0)


for i in range(NUM_PIXELS):
	strip.setPixelColor(i, ORANGE)

strip.show()
