#using the push button to put on the onboard led
from machine import Pin
import time

pin = 22
btn = Pin(pin, Pin.IN, Pin.PULL_UP)
led = Pin(19,Pin.OUT)
#for an external led i used pin 21 and GND

def oncallback(pin):
    print(pin.value())
    pinstate = pin.value()
    print(pinstate)
    if pinstate == 0:
        led.on()
        print('Button Pressed for on')
    else:
        led.off()
    
def offcallback(pin):
    print(pin.value())
    led.off()
    print('Button Pressed for off')
        
    



try:
    btn.irq(trigger=Pin.IRQ_FALLING, handler=oncallback)
    #btn.irq(trigger=Pin.IRQ_RISING, handler=offcallback)
except KeyboardInterrupt:
    led.off()
    print('Ended')
    