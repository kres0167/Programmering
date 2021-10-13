# Write your code here :-)
from machine import Pin, ADC
import dht
from time import sleep_ms
d = dht.DHT11(Pin(4))
Buz = ADC(Pin(36))
Buz.atten(ADC.ATTN_11DB)
Buz.width(ADC.WIDTH_12BIT)

while True:
    d.measure()
    temp_val = d.temperature()
    Humi_val = d.humidity()
    print("temp: ", temp_val, "C")
    print("humi: ", Humi_val, "%")
    sleep_ms(1000)

if Humi_val > 60:
    Buz(1)
