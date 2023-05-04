import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
BUTTON_PIN=16
LED_PIN1=8
LED_PIN2=10
GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN1,GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)
while True:
    GPIO.wait_for_edge(BUTTON_PIN,GPIO.FALLING)
    print("8:On, 10:Off")
    GPIO.output(LED_PIN1,GPIO.HIGH)
    GPIO.output(LED_PIN2,GPIO.LOW)
    GPIO.wait_for_edge(BUTTON_PIN,GPIO.RISING)
    GPIO.wait_for_edge(BUTTON_PIN,GPIO.FALLING)
    print("8:Off, 10:On")
    GPIO.output(LED_PIN2,GPIO.HIGH)
    GPIO.output(LED_PIN1,GPIO.LOW)
    GPIO.wait_for_edge(BUTTON_PIN,GPIO.RISING)
GPIO.cleanup()