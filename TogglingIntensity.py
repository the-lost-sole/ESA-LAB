import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
BUTTON_PIN=16
GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(12,GPIO.OUT)
P=GPIO.PWM(12,100)
P.start(0)
while True:
    GPIO.wait_for_edge(BUTTON_PIN,GPIO.RISING)
    for x in range(0,100,5):
        P.ChangeDutyCycle(x)
        sleep(0.1)
    print("Max")
    GPIO.wait_for_edge(BUTTON_PIN,GPIO.RISING)
    for x in range(100,0,-5):
        P.ChangeDutyCycle(x)
        sleep(0.1)
    print("Min")
GPIO.cleanup()