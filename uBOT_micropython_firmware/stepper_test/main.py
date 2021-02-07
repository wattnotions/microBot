
from machine import Pin
import time


print("IM IN MAIN")



la = 19
lb = 21
lc = 22
ld = 23

ra = 25
rb = 26
rc = 27
rd = 32


#Left side
#A and B are the same coil
left_a = Pin(la, Pin.OUT)    
left_b = Pin(lb, Pin.OUT)   

#C and D are the same coil
left_c = Pin(lc, Pin.OUT)    
left_d = Pin(ld, Pin.OUT)  

#Right side
#A and B are the same coil
right_a = Pin(ra, Pin.OUT)    
right_b = Pin(rb, Pin.OUT)   

#C and D are the same coil
right_c = Pin(rc, Pin.OUT)    
right_d = Pin(rd, Pin.OUT)   




def disable_steppers():
    left_a.value(0)
    left_b.value(0)
    left_c.value(0)
    left_d.value(0)
    
    right_a.value(0)
    right_b.value(0)
    right_c.value(0)
    right_d.value(0)
    print("Steppers disabled")
    
    
r_step_state = 1; 
def right_steppers(dir, msdelay): ##meant to be called in low latency loop
 
  if (r_step_state == 1):
    right_a.value(0)
    right_b.value(1)
    time.sleep_ms(msdelay)
    
  if (r_step_state == 2):
    right_c.value(0)
    right_d.value(1)
    time.sleep_ms(msdelay)
    
  if (r_step_state == 3):
    right_a.value(1)
    right_b.value(0)
    time.sleep_ms(msdelay)
  
  if (r_step_state == 4):
    right_c.value(1)
    right_d.value(0)
    time.sleep_ms(msdelay)
    
  if  (dir == 1) : r_step_state +=1 #going forward
  elif(dir == 0) : r_step_state -=1 #going backwards

l_step_state = 1 
def left_stepper(dir, msdelay):
  
  if (l_step_state == 1):
    left_a.value(0)
    left_b.value(1)
    time.sleep_ms(msdelay)
    
  if (l_step_state == 2):
    left_c.value(0)
    left_d.value(1)
    time.sleep_ms(msdelay)
    
  if (l_step_state == 3):
    left_a.value(1)
    left_b.value(0)
    time.sleep_ms(msdelay)
  
  if (l_step_state == 4):
    left_c.value(1)
    left_d.value(0)
    time.sleep_ms(msdelay)
    
  if  (dir == 1) : l_step_state +=1 #going forward
  elif(dir == 0) : l_step_state -=1 #going backwards

run_time = 0
start_time = time.time()
while (run_time < 10):
    run_time = time.time() - start_time
    left_stepper(1, 200)
    right_stepper(1,200)
from machine import Pin
import time


print("IM IN MAIN")

l_step_state = 1 
r_step_state = 1


la = 19
lb = 21
lc = 22
ld = 23

ra = 25
rb = 26
rc = 27
rd = 32


#Left side
#A and B are the same coil
left_a = Pin(la, Pin.OUT)    
left_b = Pin(lb, Pin.OUT)   

#C and D are the same coil
left_c = Pin(lc, Pin.OUT)    
left_d = Pin(ld, Pin.OUT)  

#Right side
#A and B are the same coil
right_a = Pin(ra, Pin.OUT)    
right_b = Pin(rb, Pin.OUT)   

#C and D are the same coil
right_c = Pin(rc, Pin.OUT)    
right_d = Pin(rd, Pin.OUT)   




def disable_steppers():
    left_a.value(0)
    left_b.value(0)
    left_c.value(0)
    left_d.value(0)
    
    right_a.value(0)
    right_b.value(0)
    right_c.value(0)
    right_d.value(0)
    print("Steppers disabled")
    
    
r_step_state = 1
def right_steppers(dir, msdelay): ##meant to be called in low latency loop
  global r_step_state
  if (r_step_state == 1):
    right_a.value(0)
    right_b.value(1)
    time.sleep_ms(msdelay)
    
  if (r_step_state == 2):
    right_c.value(0)
    right_d.value(1)
    time.sleep_ms(msdelay)
    
  if (r_step_state == 3):
    right_a.value(1)
    right_b.value(0)
    time.sleep_ms(msdelay)
  
  if (r_step_state == 4):
    right_c.value(1)
    right_d.value(0)
    time.sleep_ms(msdelay)
    
  if  (dir == 1) : r_step_state +=1 #going forward
  elif(dir == 0) : r_step_state -=1 #going backwards


def left_steppers(dir, msdelay):
  global l_step_state
  print(l_step_state)
  if (l_step_state == 1):
    
    left_a.value(0)
    left_b.value(1)
    time.sleep_ms(msdelay)
    
  if (l_step_state == 2):
    left_c.value(0)
    left_d.value(1)
    time.sleep_ms(msdelay)
    
  if (l_step_state == 3):
    left_a.value(1)
    left_b.value(0)
    time.sleep_ms(msdelay)
  
  if (l_step_state == 4):
    left_c.value(1)
    left_d.value(0)
    time.sleep_ms(msdelay)
    
  if  (dir == 1) : l_step_state +=1 #going forward
  elif(dir == 0) : l_step_state -=1 #going backwards

run_time = 0
start_time = time.time()
while (run_time < 10):
    run_time = time.time() - start_time
    left_steppers(1, 200)
   # right_steppers(1,200)
   
    
    
    
disable_steppers()
    
    
    
    
    




   
    
    
    
disable_steppers()
    
    
    
    
    



