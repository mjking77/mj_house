#!/usr/bin/env python
# author: Powen Ko 
import time, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

while True:
        LEDon = GPIO.output(4, 0)
        time.sleep(1)
        LEDoff = GPIO.output(4, 1)
        time.sleep(1)

