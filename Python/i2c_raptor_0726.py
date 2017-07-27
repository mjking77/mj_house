import smbus as smbus
import time

bus = smbus.SMBus(1)

DEV_ADDR = 0x50
DEV_REG_TEST = 0x40
#DAT_VAL = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
DAT_VAL = range (0,16)
DAT_VAL1 = range (0,16)
toEEP = range (0,16)

#Byte/word -- W/R
bus.write_byte_data(DEV_ADDR, 0x30, 0x0a)
time.sleep(0.1)
#bus.write_word_data(DEV_ADDR, 0x50, 0x1234)
time.sleep(1)

fb_i2c = bus.read_byte_data(DEV_ADDR, 0x30) + 1
f = open('script_test.txt','r')
flist = f.readlines()
f.close()

str1 = flist[2].split()
bkh = (int(str1[2],16) >> 16)
bkl = ((int(str1[2],16) & 0x00ff00) >> 8)
ost = (int(str1[2],16) & 0x0000ff)
msk = (int(str1[3],16)) 
data = (int(str1[4],16))

toEEP = [bkh, bkl, ost, msk, data]
bus.write_i2c_block_data(DEV_ADDR, 0x90,toEEP)
          
time.sleep(0.5)


R_DAT = bus.read_i2c_block_data(DEV_ADDR, 0x90, 8)

for i in range(0,8):
    print hex(R_DAT[i]),
print '-------------------'
'''
'''
print ("Here is 1st check %s ." %(fb_i2c))
print ("Here is 2nd check {} .".format(fb_i2c+1))
print 'Here is 2nd check =', (fb_i2c+2), '<-'


def msi2c_init(dev_addr):
    print dev_addr
    addr = hex(int(dev_addr) >>1)
    print addr
    cmd_init1 = [0x53, 0x45, 0x52, 0x44, 0x42, 0x00]
    cmd_init2 = [0x81, 0x83, 0x84, 0x53, 0x7F, 0x35, 0x71] 
    bus.write_i2c_block_data(addr, cmd_init1[0], cmd_init1[1:6])
    time.sleep(0.3)
    for i in range(0,len(cmd_init2)):
        bus.write_byte(addr>>1, cmd_init2[i])
        time.sleep(0.3)
        
    time.sleep(0.8)
    print 'finish msi2c init'
    return;

def test(a, b):
    print a+b
    return;
test(0xA1,8)
msi2c_init(0xA0)    
    


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

'''
