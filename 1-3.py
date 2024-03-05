import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 23
times = 1

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin,0)
time.sleep(times)
GPIO.output(pin,1)
time.sleep(times)
GPIO.output(pin,0)
time.sleep(times)
GPIO.output(pin,1)
time.sleep(times)
GPIO.output(pin ,0)

GPIO.cleanup()
