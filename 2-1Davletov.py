import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

for i in 2, 3, 4, 17, 27, 22, 10, 9:
    GPIO.setup(i, GPIO.OUT)

for number in range (3):
    for i in 2, 3, 4, 17, 27, 22, 10, 9:
        GPIO.output(i, 1)
        time.sleep(0.1)
        GPIO.output(i, 0)

for i in 2, 3, 4, 17, 27, 22, 10, 9:
    GPIO.output(i, 0)
GPIO.cleanup()