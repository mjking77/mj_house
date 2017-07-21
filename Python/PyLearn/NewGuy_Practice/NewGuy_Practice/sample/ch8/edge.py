#!/usr/bin/python
#Author: Powen Ko
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(17,GPIO.IN)
def my_callback(channel):
    print('This is a edge event callback function!')

GPIO.add_event_detect(17, GPIO.FALLING)
GPIO.add_event_callback(17,my_callback)

GPIO.add_event_detect(4, GPIO.RISING)
while True:
    if GPIO.event_detected(4):
        print('Button pressed')

