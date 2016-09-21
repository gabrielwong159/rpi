import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Runtime error. Try sudo")

BUTTON = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUTTON, GPIO.IN)

while(1):
    if (GPIO.input(BUTTON)==GPIO.HIGH):
        print("YES")
    else:
        print("NO")

    time.sleep(0.5)
