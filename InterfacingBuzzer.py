import RPi.GPIO as GPIO
import board
import adafruit_dht
import time
import sqlite3
buz=16
conn=sqlite3.connect('Sensor.db')
c=conn.cursor()
dhtDevice=adafruit_dht.DHT22(board.D4,use_pulseio=False)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(buz,GPIO.OUT)
GPIO.output(buz,GPIO.LOW)
buz.start(50)
time.sleep(2.0)
while True:
    temperature_c=dhtDevice.temperature
    temperature_f=(9/5)*temperature_c+32
    humidity=dhtDevice.humidity
    print(temperature_f,humidity)
    if temperature_f > 86:
        buz.start(50)
        for x in range(0,100,5):
            buz.ChangeDutyCycle(x)
    buz.stop()
    c.execute("Insert into temphum(temperature_f,humidity) values (?,?)",(temperature_f,humidity))
    conn.commit()
    time.sleep(2.0)