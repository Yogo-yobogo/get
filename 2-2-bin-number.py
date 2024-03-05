import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0 , 5, 12, 6]
number = [1, 1, 1, 1, 1, 1, 1, 1]
for i in dac:
    GPIO.setup(i, GPIO.OUT)

for i in range(7, -1, -1):
    GPIO.output(dac[i], number[i])

time.sleep(15)

for i in dac:
    GPIO.output(i, 0)
GPIO.cleanup()