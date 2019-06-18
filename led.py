import RPi.GPIO as GPIO
import time
def lock():
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(23,GPIO.OUT)
   GPIO.output(23,GPIO.LOW)
   print ("LED on")
   GPIO.output(23,GPIO.HIGH)
   time.sleep(10)
   GPIO.output(23,GPIO.LOW)





