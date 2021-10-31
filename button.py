#using the push button on the expansion board
from machine import Pin
import time

pin = 22
button = Pin(pin, Pin.IN, Pin.PULL_UP)


def btn ():
    while True:
        btnState = button.value()
        if btnState == 0:
            print('button pressed @ pin state {}'.format(btnState))
            #break 
        else:
            print(btnState)
            time.sleep_ms(100)

        
try:
    btn()
except KeyboardInterrupt:
    print('Ended')