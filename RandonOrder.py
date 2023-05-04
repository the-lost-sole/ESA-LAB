import RPi.GPIO as GPIO
from time import sleep
import random
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,intial=GPIO.LOW)
GPIO.setup(10,GPIO.OUT,intial=GPIO.LOW)
GPIO.setup(12,GPIO.OUT,intial=GPIO.LOW)
choices=[8,10,12]
while True:
    temp=random.choice(choices)
    GPIO.output(temp,GPIO.HIGH)
    sleep(1)
    GPIO.output(temp,GPIO.LOW)
    sleep(1)