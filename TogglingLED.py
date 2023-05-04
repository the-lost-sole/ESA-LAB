import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
BUTTON_PIN=16
LED_PIN=10
GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN,GPIO.OUT)
while True:
    GPIO.wait_for_edge(BUTTON_PIN,GPIO.FALLING)
    print("on")
    GPIO.output(LED_PIN,GPIO.HIGH)
    GPIO.wait_for_edge(BUTTON_PIN,GPIO.RISING)
    print("Off")
    GPIO.output(LED_PIN,GPIO.LOW)
GPIO.cleanup()