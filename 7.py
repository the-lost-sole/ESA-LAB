

# Calculating the distance by using ultrasonic sensor

# 1.Printing

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

trig=5
echo=12

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trig,GPIO.LOW)
time.sleep(2)

i=0


while i<10:
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.02)
    GPIO.output(trig,GPIO.LOW)
    while GPIO.input(echo)==0:
        start_time=time.time()
    while GPIO.input(echo)==1:
        bounce_time=time.time()
    pulse_dur=bounce_time-start_time
    distance=round(pulse_dur*17150/2)
    print(f"{distance}cm")
    time.sleep(2)
    i=i+1



# 2.Interfacing an LED

import RPi.GPIO as GPIO 
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

trig=5
echo=12
led=13

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(led,GPIO.OUT,intial=GPIO.LOW)
GPIO.setup(trig,GPIO.OUT)


i=0

while i<10:
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.02)
    GPIO.output(trig,GPIO.LOW)
    while GPIO.input(echo)==0:
        start_time=time.time()
    while GPIO.input(echo)==1:
        bounce_time=time.time()
    pulse_dur=bounce_time-start_time
    distance=round(pulse_dur*17150/2)
    if distance<10:
        GPIO.output(led,GPIO.HIGH)
    print(f"{distance}cm")
    time.sleep(2)
    i=i+1



# Interfacing a buzzer


import RPi.GPIO as GPIO 
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

trig=5
echo=12
buzz=13

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(buzz,GPIO.OUT,initial=GPIO.LOW)


i=0

while i<10:
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.02)
    GPIO.output(trig,GPIO.LOW)
    buzz=GPIO.PWM(13,100)
    buzz.start(0)
    while GPIO.input(echo)==0:
        start_time=time.time()
    while GPIO.input(echo)==1:
        bounce_time=time.time()
    pulse_dur=bounce_time-start_time
    distance=round(pulse_dur*17150/2)
    if distance<10:
        for x in range(0,100,5):
            buzz.ChangeDutyCycle(x)
            time.sleep(0.1)
        buzz.stop()
    print(f"{distance}cm")
    time.sleep(2)
    i=i+1










