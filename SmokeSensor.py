import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
import AnalogIn from adafruit_ads1x15.analog_in
i2c=busio.I2C(board.SCL,board.SDA)
ads=ADS.ADS1015(i2c)
ads.gain=8
chan=AnalogIn(ads,ADS.P0)
print("{:>5}\t{:>5}".format('raw','v'))
while True:
    print("{:>5}\t{:>5.5f}".format(chan.value,chan.voltage))
    time.sleep(0.5)