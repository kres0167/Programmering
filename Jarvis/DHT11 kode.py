from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(14))
while True:
    # try og except bruges for at fortsætte eksekvering selvom fejl opstår
    # det forhindre ESP32 i at crashe hvis sensoren ikke læses korrekt
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        # %3.1f er formatering strengen med antal af decimaler angivet af tallet 1
        print("Temperatur: %3.1f C" % temp)
        sleep(1)
        print("Humidity:", hum, "%")
        sleep(1)
        # Hvis sensor ikke læses printes en fejlmeddelse
        # i stedet for at stoppe programmet
    except OSError as e:
        print("Failed to read sensor.")
