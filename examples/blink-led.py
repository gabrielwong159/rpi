import time
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Runtime error. Try sudo")

LED = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

while True:
	try:
		GPIO.output(LED, 1)
		time.sleep(1)
		GPIO.output(LED, 0)
		time.sleep(1)

	except KeyboardInterrupt:
		print "\nexiting\n"
		GPIO.cleanup()
