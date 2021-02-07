
from machine import Pin
import time


print("IM IN MAIN")

msdelay = 200

la = 19
lb = 21
lc = 22
ld = 23


#A and B are the same coil
left_a = Pin(la, Pin.OUT)    
left_b = Pin(lb, Pin.OUT)   

#C and D are the same coil
left_c = Pin(lc, Pin.OUT)    
left_d = Pin(ld, Pin.OUT)    


def disable_steppers():
    left_a.value(0)
    left_b.value(0)
    left_c.value(0)
    left_d.value(0)
    print("Steppers disabled")
    

run_time = 0
start_time = time.time()
while (run_time < 10):
    run_time = time.time() - start_time
    
    print("1")
    left_a.value(0)
    left_b.value(1)
    time.sleep_ms(msdelay)
    
    print("2")
    left_c.value(0)
    left_d.value(1)
    time.sleep_ms(msdelay)
    
    print("3")
    left_a.value(1)
    left_b.value(0)
    time.sleep_ms(msdelay)
    
    print("4")
    left_c.value(1)
    left_d.value(0)
    time.sleep_ms(msdelay)
    
    
    print("loop6.0")
    
    
    
disable_steppers()
    
    
    
    
    



