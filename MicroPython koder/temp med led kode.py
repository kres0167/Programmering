# importere Pin, ADC and PWM klasserne
from machine import Pin, ADC, PWM
# Importere sleep klassen fra time modulet
from time import sleep
led = PWM(Pin(4), 5000)
# Instantiere ADC objekt kaldet potentiometer
temp = ADC(Pin(36))
temp.width(ADC.WIDTH_10BIT)
temp.atten(ADC.ATTN_11DB)
while True:
    temp_val = temp.read()
    # Gemmer analog pin værdi i variabel
    # Sætter duty cycle value til potentiometer value
    led.duty(temp_val)
    print("Duty: ", led.duty())
    sleep(0.1)
