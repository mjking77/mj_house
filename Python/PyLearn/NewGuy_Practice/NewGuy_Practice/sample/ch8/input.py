#!/usr/bin/python
# aurthor: Powen Ko
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.IN)
while True:
    value01=GPIO.input(17)
    GPIO.output(4,value01)
    time.sleep(0.1)