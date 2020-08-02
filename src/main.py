￼import RPi.GPIO as GPIO
import time
from gpiozero import Servo

s2 = 26
s3 = 27
signal = 17
NUM_CYCLES = 10

correction = 0.45
maxpw = (2.0+correction)/1000
minpw = (1.0-correction)/1000

btm = Servo(17, min_pulse_width=minpw, max_pulse_width=maxpw)
top = Servo(26, min_pulse_width=minpw, max_pulse_width=maxpw)





def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")
  




def loop():
  temp = 1
  while(1):  

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    red  = NUM_CYCLES / duration   #in Hz
    print("red value - ",red)

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    print("blue value - ",blue)

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    print("green value - ",green)
    time.sleep(2)
    
    if green > 12500:
        print("Green")
        print("Box 2")
        time.sleep(1)
        top.mid()
        print("Dropping into Box")
        time.sleep(1)
        top.min()
        print("going back")
        time.sleep(1)
        btm.mid()
        
    elif red > 12500:
        print("Red")
        top.min()
        btm.min()
        print("Box 1")
        time.sleep(1)
        top.mid()
        print("Dropping into Box")
        time.sleep(1)
        top.min()
        print("going back")
        time.sleep(1)
        btm.mid()
        
    elif blue > 12500:
        print("Blue")
        print("Box 3")
        time.sleep(1)
        top.mid()
        print("Dropping into Box")
        time.sleep(1)
        top.min()
        print("going back")
        time.sleep(1)


def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()

 