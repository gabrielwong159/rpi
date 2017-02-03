# in order to get the server running, the following commands are required
# 	export FLASK_APP=hello.py
#	sudo -E flask run --host 0.0.0.0

import time
import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

import neopixel
LED_COUNT = 60
LED_PIN = 18
LED_BRIGHTNESS = 63
strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN)
strip.setBrightness(LED_BRIGHTNESS)
strip.begin()
strip.show()
BLUE = neopixel.Color(0,0,127)

from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
	return "Main page!"

@app.route("/hello")
def hello():
	return "Hello, World!"

@app.route("/led")
def led():
	GPIO.output(LED_PIN, not(GPIO.input(LED_PIN)))
	return 'success'

@app.route("/neopixel")
def neop():
	for i in range(LED_COUNT):
		strip.setPixelColor(i, BLUE)
	strip.show()
	return 'pew'

@app.route("/write")
def write():
	f = open('test','w')
	f.write('hello')
	f.close()
	return '1'

if __name__ == "__main__":
	app.run()
