#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from time import sleep
from subprocess import call
en = 19
en1 = 26
en2 = 16
en3 = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.IN)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
p = GPIO.PWM(en,1000)
p.start(50)
TRIG=18 
ECHO=17 

print"controls" 
print"w: move forward" 
print"s: move reverse" 
print"p: stop robot"
print"e: stop the code"
print"4:take picture with user defined name" 
print"5: move forward with speed control" 
print"6: Rotate the Robot" 
print"7: Turn the Robot" 
print"8: for servo control please" 
print"11 : welcome to autonomous control" 

print"press enter to send command" 
def takestillpic(inp):
    print" please enter photo character"
    inp = raw_input()
    call ( ["raspistill -vf -hf -o " + str(inp) + ".jpg" ],shell=True )
    
def fwd():
    GPIO.output(19,False)
    GPIO.output(26,True)
    GPIO.output(16,False)
    GPIO.output(20,True)

def rev():
    GPIO.output(19,True)
    GPIO.output(26,False)
    GPIO.output(16,True)
    GPIO.output(20,False)

def stop():
    GPIO.output(19,False)
    GPIO.output(26,False)
    GPIO.output(16,False)
    GPIO.output(20,False)

def distmeas():
    print" Distance measurement in progress"
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print" waiting for sensor to settle please"
    time.sleep(2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)
    print " Distance ", distance, "cm"
    if distance < 250 :
           GPIO.output(19,False)
           GPIO.output(26,False)
           GPIO.output(16,False)
           GPIO.output(20,False)
           time.sleep(1)
           print " robot stopped as distance is less"
           print " Now Robot going Backward"
           GPIO.output(19,True)
           GPIO.output(26,False)
           GPIO.output(16,True)
           GPIO.output(20,False)

           time.sleep(1)
           GPIO.output(19,False)
           GPIO.output(26,False)
           GPIO.output(16,False)
           GPIO.output(20,False)
           TLr()
           time.sleep(4)
           fwd()
           distmeas()

    else:
         distmeas()

def TL():
    GPIO.output(19,True)
    GPIO.output(26,False)
    GPIO.output(16,False)
    GPIO.output(20,False)

def TLr():
    GPIO.output(19,True)
    GPIO.output(26,False)
    time.sleep(0.75)
    GPIO.output(19,False)
    GPIO.output(26,False)
while True:
    inp= raw_input()
    if inp =="w":
        fwd()
        print"robot moving in fwd direction"
    elif inp =="s":
        rev()
        print"robot moving in rev direction"
    elif inp=="p":
        stop()
        print"robot stopped"
    elif inp == "e":
        GPIO.cleanup()
        break
    elif inp =="4":
          takestillpic(inp)
          print " photo please"

    elif inp =="5":
        GPIO.output(7,False)
        GPIO.output(8,False)
    elif inp =="6":
         TL()
    elif inp =="7":
         TLr()
    elif inp =="8":
         servo = PWM.Servo()
         servo.set_servo(27,1000)
         time.sleep(2)
         servo.stop_servo(27)
    elif inp =="9":
         servo = PWM.Servo()
         servo.set_servo(27,1500)
         time.sleep(2)
         servo.stop_servo(27)
    elif inp =="10":
         servo = PWM.Servo()
         servo.set_servo(27,2000)
         time.sleep(2)
         servo.stop_servo(27)
    elif inp == "11":

         fwd()
         distmeas()

GPIO.cleanup()
