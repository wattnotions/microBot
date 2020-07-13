
from machine import Pin
import time


print("IM IN MAIN")

msdelay = 25


#A and B are the same coil
left_a = Pin(19, Pin.OUT)    # create output pin on GPIO0
left_b = Pin(21, Pin.OUT)    # create output pin on GPIO0

#C and D are the same coil
left_c = Pin(22, Pin.OUT)    # create output pin on GPIO0
left_d = Pin(23, Pin.OUT)    # create output pin on GPIO0


while(True):
    left_a.value(1)
    left_b.value(0)
    time.sleep_ms(msdelay)
    
    left_c.value(0)
    left_d.value(1)
    time.sleep_ms(msdelay)
    
    left_a.value(0)
    left_b.value(1)
    time.sleep_ms(msdelay)
    
    left_c.value(1)
    left_d.value(0)
    time.sleep_ms(msdelay)
    
    print("loop2.0")
    
    
    
    
    

