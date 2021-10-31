#using the PIR SENSOR to detect
from machine import Pin
import time

pin = 18
pir = Pin(pin, Pin.IN, Pin.PULL_UP)

def pirsensor():
    while True:    
        pirState = pir.value()
        print(pirState)
        time.sleep_ms(200)
        if pirState == 1:
            print('Heat signature detected')


try:
    pirsensor()
except KeyboardInterrupt:
    print('Ended')
    
