
# Implementing 7-segment display

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin=[8,10,12,16,18,22,24,33,35,37]

for x in pin:
    GPIO.setup(x,GPIO.OUT)

digits=[
    [0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1],
    [0,0,1,0,0,1,0],
    [0,0,0,0,1,1,0],
    [1,0,0,1,1,0,0],
    [0,1,0,0,1,0,0],
    [0,1,0,0,0,0,0],
    [0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0]
]

gpin=[8,10,12,16,18,22,24]

def digitDisplay(digit):
    for x in range(0,7):
        GPIO.output(gpin[x],digit[x])


while True:
    GPIO.output(37,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(35,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(33,GPIO.HIGH)
    time.sleep(1)
    for digit in digits:
        digitDisplay(digit)
        time.sleep(1)
    GPIO.output(33,GPIO.LOW)
