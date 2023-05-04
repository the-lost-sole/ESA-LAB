import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pir=29
led=32

GPIO.setup(pir,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

GPIO.output(GPIO.LOW)

while True:
    if(GPIO.input(pir)):
        GPIO.output(led,GPIO.HIGH)
        print("on")
        time.sleep(1)
    else:
        GPIO.output(led,GPIO.LOW)
        print("off")
        time.sleep(1)



# Interfacing 7 segment display


import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin=[8,10,12,16,18,22,24]
PIR_INPUT=29


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
GPIO.setup(PIR_INPUT,GPIO.IN)
count=0


def digitDisplay(digit):
    for x in range(0,7):
        GPIO.output(gpin[x],digit[x])


while True:
    if(GPIO.input(PIR_INPUT)):
        print("MOvement detected")
        count+=1
        count%=10
        if count==0:
            digitDisplay(digits[0])
        elif count==1:
            digitDisplay(digits[1])
        elif count==2:
            digitDisplay(digits[2])
        time.sleep(0.2)
    else:
        print("No movement detected")
        time.sleep(1)
  
