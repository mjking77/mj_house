#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
count=0
while (count<4):
    GPIO.output(4, 1)
    time.sleep(1)
    GPIO.output(4, 0)
    time.sleep(1)
    count=count+1

print "Good bye powenko.com"
