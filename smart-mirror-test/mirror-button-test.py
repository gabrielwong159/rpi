import time
import uinput

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Runtime error. Try sudo")

KEYS = [uinput.KEY_1, uinput.KEY_2, uinput.KEY_3, uinput.KEY_4, uinput.KEY_5, uinput.KEY_6, uinput.KEY_7, uinput.KEY_8]
device = uinput.Device(KEYS)

# green, green, yellow, blue, red, pink, black, white
BUTTONS = [6, 13, 20, 19, 12, 16, 21, 5]

prev = [False, False, False, False, False, False, False, False]
curr = [False, False, False, False, False, False, False, False]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(BUTTONS, GPIO.IN, GPIO.PUD_DOWN)

def buttonPressed():
	for i in range(len(BUTTONS)):
            if GPIO.input(BUTTONS[i]):
                curr[i] = True
                if prev[i] == False:
                    device.emit_click(KEYS[i])
            else:
                curr[i] = False

	    prev[i] = curr[i]

while True:
	try:
            buttonPressed()
	except KeyboardInterrupt:
            print "\nexiting"
            GPIO.cleanup()

