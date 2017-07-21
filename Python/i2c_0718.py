import smbus as smbus
import time

bus = smbus.SMBus(1)

DEV_ADDR = 0x50
DEV_REG_TEST = 0x40
#DAT_VAL = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
DAT_VAL = range (0,16)
DAT_VAL1 = range (0,16)

#Byte/word -- W/R
bus.write_byte_data(DEV_ADDR, 0x30, 0x0a)
time.sleep(0.1)
#bus.write_word_data(DEV_ADDR, 0x50, 0x1234)
time.sleep(1)

fb_i2c = bus.read_byte_data(DEV_ADDR, 0x30) + 1
'''fbb_i2c = bus.read_block_data(DEV_ADDR, 0x50)
print ("Here is 1st check %s ." %(fb_i2c))
print ("Here is 2nd check {} .".format(fb_i2c+1))
print ("Here is 2nd check {} .".format(fbb_i2c))
'''

for i in range(8,24):
    for k in range (0,16):
        DAT_VAL1[k]= DAT_VAL[k]+(i-8)*16
    bus.write_i2c_block_data(DEV_ADDR, (i*16), DAT_VAL1)
    time.sleep(0.1)

for i in range(0,24):
    for j in range (0,16):
        print "{}".format(hex(bus.read_byte_data(DEV_ADDR, (i*16)+j))),
    print (" ")


print ("----------------")            
