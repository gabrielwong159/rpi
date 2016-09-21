import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Runtime error. Try sudo")

LED = 4
BUTTON = 5

prev = False
curr = False
state = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def buttonPressed():
	global state

	state = not(state)
	GPIO.output(LED, state)
	print state

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
		print "\nexiting\n"
		GPIO.cleanup()

