#!/usr/bin/env python
# author: Powen Ko
import serial
import time

def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch=='\r' or ch=='':
            return rv

port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)

while True:
    rcv = readlineCR(port)
    print(rcv)


