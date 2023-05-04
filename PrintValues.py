import board
import adafruit_dht
import time
dhtDevice=adafruit_dht.DHT22(board.D4,use_pulseio=False)
while True:
    temperature_c=dhtDevice.temperature
    temperature_f=(9/5)*temperature_c+32
    humidity=dhtDevice.humidity
    print(temperature_f,humidity)
    time.sleep(2.0)