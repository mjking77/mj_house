#!/usr/bin/python
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
os.system('modprobe snd_bcm2835')
os.system('amixer cset numid=3 1')
#os.system('mplayer -playlist http://bbc.co.uk/radio/listen/live/r1.asx   &')
while True:
     if GPIO.input(23)==1:
         os.system('sudo killall mplayer')
         os.system('mplayer -playlist http://bbc.co.uk/radio/listen/live/r2.asx   &')
     if GPIO.input(24)==1:
         os.system('sudo killall mplayer')
         os.system('mplayer -playlist http://bbc.co.uk/radio/listen/live/r3.asx   &')
     time.sleep(0.1);
GPIO.cleanup()