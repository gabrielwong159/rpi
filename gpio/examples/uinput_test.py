import time
import uinput

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Runtime error. Try sudo")

device = uinput.Device([uinput.KEY_T])

BUTTON = 5

prev = False
curr = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(BUTTON, GPIO.IN)

def buttonPressed():
	device.emit_click(uinput.KEY_T)

while True:
	try:
		if (GPIO.input(BUTTON)):
			curr = True
			if (not(prev)):
				buttonPressed()
		else:
			curr = False

		prev = curr

	except KeyboardInterrupt:
		print "\nexiting"
		GPIO.cleanup()

