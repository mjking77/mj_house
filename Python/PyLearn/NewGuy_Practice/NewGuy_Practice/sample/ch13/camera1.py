#!/usr/bin/python
import time
import os
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
while True:
   if GPIO.input(23)==0:
          d1=time.strftime("%Y_%m_%d-%H_%M_%S")
          action="fswebcam -r 960x720 -d /dev/video0 "+d1+".jpg"
          os.system(action)
   time.sleep(0.3)
GPIO.cleanup()
