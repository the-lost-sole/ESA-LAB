import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led=[8,10,12]
for x in led:
    GPIO.setup(x,GPIO.OUT)
P=GPIO.PWM(8,100)
Q=GPIO.PWM(10,100)
R=GPIO.PWM(12,100)
P.start(0)
Q.start(0)
R.start(0)
while True:
    for x in range(0,100,10):
        P.ChangeDutyCycle(x)
        Q.ChangeDutyCycle(x)
        R.ChangeDutyCycle(x)
        time.sleep(0.1)
    for x in range(100,0,-10):
        P.ChangeDutyCycle(x)
        Q.ChangeDutyCycle(x)
        R.ChangeDutyCycle(x)
        time.sleep(0.1)