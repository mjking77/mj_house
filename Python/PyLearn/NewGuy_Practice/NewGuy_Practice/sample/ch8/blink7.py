#!/usr/bin/env python
# author: Powen Ko 
import time, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

while True:
        LEDon = GPIO.output(7, 0)
        time.sleep(1)
        LEDoff = GPIO.output(7, 1)
        time.sleep(1)

