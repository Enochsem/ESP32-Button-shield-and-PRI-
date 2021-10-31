#using the push button on the expansion board
from machine import Pin
import time

pin = 22
btn = Pin(pin, Pin.IN, Pin.PULL_UP)

def callback(pin):
    print(pin.value())
    print('Button Pressed')
    
btn.irq(trigger=Pin.IRQ_FALLING, handler=callback)