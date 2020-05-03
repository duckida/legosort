from gpiozero import Servo
import time


correction = 0.45
maxpw = (2.0+correction)/1000
minpw = (1.0-correction)/1000

btm = Servo(17, min_pulse_width=minpw, max_pulse_width=maxpw)
top = Servo(26, min_pulse_width=minpw, max_pulse_width=maxpw)

#The Full demo

print("Full Demo")
top.min()
btm.min()
#print(btm.min())
print("Box 1")
time.sleep(1)
top.mid()
print("Dropping into Box")
time.sleep(1)
top.min()
print("going back")
time.sleep(1)
btm.mid()
print("Box 2")
time.sleep(1)
top.mid()
print("Dropping into Box")
time.sleep(1)
top.min()
print("going back")
time.sleep(1)
btm.max()
print("Box 3")
time.sleep(1)
top.mid()
print("Dropping into Box")
time.sleep(1)
top.min()
print("going back")
time.sleep(1)
            
