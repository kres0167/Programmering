from machine import Pin, PWM
from time import sleep_ms
frequency = 5000
start_duty = 1023
r = PWM(Pin(18), frequency, start_duty)
g = PWM(Pin(5), frequency, start_duty)
b = PWM(Pin(19), frequency, start_duty)
while True:
    for duty_cycle in range(1024):
        r.duty(duty_cycle)
        print("r ", duty_cycle)
        sleep_ms(1)

    for duty_cycle in range(1024):
        g.duty(duty_cycle)
        print("g ", duty_cycle)
        sleep_ms(1)

    for duty_cycle in range(1024):
        b.duty(duty_cycle)
        print("b ", duty_cycle)
        sleep_ms(0.1)

    for duty_cycle in range(1024):
        b.duty(duty_cycle)
        print("b ", duty_cycle)
        sleep_ms(1)

    for duty_cycle in range(1024):
        b.duty(duty_cycle)
        print("b ", duty_cycle)
        sleep_ms(1)

    for duty_cycle in range(1024):
        b.duty(duty_cycle)
        print("b ", duty_cycle)
        sleep_ms(1)
