import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 24
key = 21


GPIO.setup(led, GPIO.OUT)
GPIO.setup(key, GPIO.IN)

GPIO.output(led, GPIO.input(key))


#GPIO.cleanup()
