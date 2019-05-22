#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

try:
   time.sleep(2)
   while True:
       if GPIO.input(23):
           print("Motion Detected!")
           execfile("/home/pi/smsconfig.py")
           execfile("/home/pi/cam.sh")
           time.sleep(2)

       else:
           print("No Motion Detected . . ")
       time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    pass
