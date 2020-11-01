import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        GPIO.output(17, 1)
        time.sleep(0.5)
        if GPIO.input(17):
            print("about to turn off")
        GPIO.output(17, 0)
        time.sleep(0.5)
        if GPIO.input(17):
            print("about to turn on")
except KeyboardInterrupt:
    GPIO.cleanup()
        