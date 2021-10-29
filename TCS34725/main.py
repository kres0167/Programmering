from TCS34725 import *
from machine import Pin, I2C
from time import sleep

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)

while True:
    if i2c.scan() !=[]:
        sensor = TCS34725(i2c)
        sensor.gain(60)
        data = sensor.read(True)
        #print(html_rgb(data))
        sleep(1)
        #print("red", html_rgb(data)[0])
    elif html_rgb(data)[0] >= 100:
        print("red")
    elif html_rgb(data)[1] >= 100:
        print("green")
    elif html_rgb(data)[2] >= 100:
        print("blue")
    else:
        print ("No colour detected")
    
