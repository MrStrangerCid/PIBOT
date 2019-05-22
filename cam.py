import RPi.GPIO as GPIO
import time
from picamera import PiCamera
GPIO.setmode(GPIO.BCM)

pirPin = 23
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
camera = PiCamera()
counter = 1
while True:
    if GPIO.input(pirPin) == GPIO.HIGH:
        try:
            print("Motion Detected...")
            print("Recording video for 10 second...")
            camera.start_preview()
            camera.start_recording('/home/pi/video%s.h264' % counter)
            counter = counter + 1
            time.sleep(10)
            camera.stop_recording()
            camera.stop_preview()
        except KeyboardInterrupt:
            camera.stop_preview()
            
    else:
        print("No Motion...")
        time.sleep(1)

