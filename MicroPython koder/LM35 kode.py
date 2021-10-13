# Write your code here :-)
from machine import Pin, ADC
from time import sleep_ms

temp = ADC(Pin(36))
temp.atten(ADC.ATTN_11DB)
temp.width(ADC.WIDTH_12BIT)

while True:
 temp_val = temp.read()
 spaending = temp_val * (0.01/3.3 * 4096)
 print("Analog temp vaerdi: ", temp_val)
 print("temp: ", spaending)
 sleep_ms(500)
