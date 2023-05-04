import board
import adafruit_dht
import time
import sqlite3
conn=sqlite3.connect('Sensor.db')
c=conn.cursor()
dhtDevice=adafruit_dht.DHT22(board.D4,use_pulseio=False)
while True:
    temperature_c=dhtDevice.temperature
    temperature_f=(9/5)*temperature_c+32
    humidity=dhtDevice.humidity
    print(temperature_f,humidity)
    c.execute("Insert into temphum(temperature_f,humidity) values (?,?)",(temperature_f,humidity))
    conn.commit()
    time.sleep(2.0)