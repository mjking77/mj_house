#!/usr/bin/python
# Aurthor: Powen Ko
import spidev
import time
import os
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
delay=10
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

# Define sensor channels
while True:
    # Read the light sensor data
    data1 = ReadChannel(0)
    data2 = ReadChannel(1)
    # Print out results
    print("value1: {}  value2:{}".format(data1,data2))
    time.sleep(delay)