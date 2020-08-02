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
    duration = time.time() - start 
    red  = NUM_CYCLES / duration   
   
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    
      
    if green<7000 and blue<7000 and red>12000:
      print("Red")
      temp=1
    elif red<12000 and  blue<12000 and green>12000:
      print("Green")
      temp=1
    elif green<7000 and red<7000 and blue>12000:
      print("Blue")
      temp=1
    elif red>10000 and green>10000 and blue>10000 and temp==1:
      print("Waiting for Brick.....")
      temp=0


def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
