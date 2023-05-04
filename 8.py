import RPi.GPIO as GPIO
import time
import sqlite3

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

conn=sqlite3.connect('sensor.db')
c=conn.cursor()

trig=5
echo=12

while True:
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.02)
    GPIO.output(trig,GPIO.HIGH)
    while GPIO.input(echo)==0:
        start_time=time.time()
    while GPIO.input(echo)==1:
        bounce_time=time.time()
    pulse_dur=bounce_time-start_time
    distance=round(pulse_dur*17150/2)
    c.execute(f"Insert into distance(dist) values({distance})")
    conn.commit()
    time.sleep(2)
    i=i+1

