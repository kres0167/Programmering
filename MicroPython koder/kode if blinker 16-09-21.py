from machine import Pin, ADC
from time import sleep_ms
import time

pot = ADC(Pin(36))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)
led1 = Pin(17, Pin.OUT, value=0)
led2 = Pin(16, Pin.OUT, value=0)
led3 = Pin(18, Pin.OUT, value=0)

while True:
    pot_val = pot.read()
    spaending = pot_val * (3.3 / 4096)
    print("Analog potentiometer vaerdi: ", pot_val)
    sleep_ms(200)

    if pot_val < 500:
        led2.value(0)
        led3.value(0)
        led1.value(not led1.value())
        sleep_ms(100)

    if pot_val > 1500 and pot_val < 3000:
        led1.value(0)
        led3.value(0)
        led2.value(not led2.value())
        sleep_ms(100)

    if pot_val > 3000:
        led1.value(0)
        led2.value(0)
        led3.value(not led3.value())
        sleep_ms(100)
