#!/usr/bin/python
import time
import os
import datetime
while True:
   d1=time.strftime("%Y_%m_%d-%H_%M_%S")
   action="fswebcam -r 960x720 -d /dev/video0 "+d1+".jpg"
   os.system(action)
   time.sleep(1*60)
GPIO.cleanup()
