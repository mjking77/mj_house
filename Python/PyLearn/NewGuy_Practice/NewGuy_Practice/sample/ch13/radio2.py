#!/usr/bin/python
import time
import os
import RPi.GPIO as GPIO
words=[]
words.append("http://bbc.co.uk/radio/listen/live/r1.asx")
words.append("http://bbc.co.uk/radio/listen/live/r2.asx")
words.append("http://bbc.co.uk/radio/listen/live/r3.asx")
words.append("http://bbc.co.uk/radio/listen/live/r4.asx")
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
os.system('modprobe snd_bcm2835')
os.system('amixer cset numid=3 1')
i=0
action=1
wordlen=len(words)
while True:
     if GPIO.input(23)==1:
         i=i+1
         action=1;
     if GPIO.input(24)==1:
         i=i-1
         action=1


     if action==1:
        if i<0:
           i=wordlen-1
        if i>=wordlen:
           i=0
        print "--------------------------------"
        print i
        print words[i]
        action=0
        os.system('sudo killall mplayer')
        os.system('mplayer -playlist '+words[i]+'   &')
     time.sleep(0.1);
GPIO.cleanup()