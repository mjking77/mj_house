'''
--- mstar chip slave i2c usage note
After booting , initialize once to addr_A2 with :
  (1) block write [0x53, 0x45, 0x52, 0x44, 0x42] , then delay 5ms
  (2) Byte write for each of [0x81, 0x83, 0x84, 0x53, 0x7F, 0x35, 0x71]



'''

import smbus as smbus
import time

bus = smbus.SMBus(1)
#device slave addr
addr_1 = 0    

'''
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
'''

print 'start................................................................'

def msi2c_init(addr_1):
    cmd_init1 = [0x53, 0x45, 0x52, 0x44, 0x42]
    cmd_init2 = [0x81, 0x83, 0x84, 0x53, 0x7F, 0x35, 0x71] 
    addr = addr_1 >>1

    bus.write_i2c_block_data(addr, cmd_init1[0], cmd_init1[1:5])
    time.sleep(0.01)

    for i in range(0,len(cmd_init2)):
        bus.write_byte(addr, cmd_init2[i])
        time.sleep(0.001)
        
    time.sleep(0.005)

    bus.write_i2c_block_data(addr, 0x10, [0x00, 0x00, 0x1e, 0x00])
    chk=bus.read_byte(addr)
    
    return chk;

def msi2c_write(addr_1, bkh, bkl, ost, msk, dat):
    addr = addr_1 >>1
    bus.write_i2c_block_data(addr, 0x10, [0x00, bkh, bkl, ost])
    r_dat = bus.read_byte(addr)
    time.sleep(0.001)
    msk_dat = (~msk & r_dat) | dat
    bus.write_i2c_block_data(addr, 0x10, [0x00, bkh, bkl, ost, msk_dat])
    time.sleep(0.001)
    return;

def load_script(str):
    f = open(str,'r')
    flist = f.readlines()
    f.close()
    
    time.sleep(0.3)
    for i in range(0, len(flist)):
        if flist[i].find('wriu')==True:
            str1 = flist[i].split()
            bkh = (int(str1[2],16) >> 16)
            bkl = ((int(str1[2],16) & 0x00ff00) >> 8)
            ost = (int(str1[2],16) & 0x0000ff)
            msk = (int(str1[3],16)) 
            dat = (int(str1[4],16))
            msi2c_write(0xA2, bkh, bkl, ost, msk, dat)
    print '-----load finish-----'
    test = [bkh, bkl, ost, dat]
    return test;


def test(a, b):
    print a+b
    return;
#print 'bk001e_00 = ', hex(msi2c_init(0xA2))
print addr_1

str1 = load_script('TX_ATOP_8bits_1080_60P.txt')
#str1 = load_script('TX_ATOP_8bits_720_60P.txt')
print str1
str2 = load_script('TX_TIMING_1920x1080_60P.txt')
#str2 = load_script('TX_TIMING_1280x720_60P.txt')
print str2


'''
cmd_init1 = [3, 4, 5, 6]
cmd_init2 = [0x81, 0x83, 0x84, 0x53, 0x7F, 0x35, 0x71] 

test(0xA1,8)
#msi2c_init(0xA2)
bus.write_i2c_block_data(0x51, 0x53, [0x45, 0x52, 0x44, 0x42])
time.sleep(0.01)
for i in range(0,len(cmd_init2)):
        bus.write_byte(0x51, cmd_init2[i])
        time.sleep(0.001)



bus.write_i2c_block_data(0x51, 0x10, [0x00, 0x00, 0x1e, 0x00])
chk=bus.read_byte(0x51)
print hex(chk)
bus.write_i2c_block_data(0x51, 0x10, [0x00, 0x00, 0x0b, 0x00])
chk=bus.read_byte(0x51)
print hex(chk)
bus.write_i2c_block_data(0x51, 0x10, [0x00, 0x00, 0x0b, 0x00, 0x00])
time.sleep(0.001)
bus.write_i2c_block_data(0x51, 0x10, [0x00, 0x00, 0x0b, 0x00])
chk=bus.read_byte(0x51)
print hex(chk)
'''




'''
time.sleep(0.003)
bus.write_byte(0x51, 0x53)
time.sleep(0.005)
bus.write_i2c_block_data(0x51, 0x53, cmd_init1)
'''
cmd_init3 = [0x10, 0x00, 0x00, 0x1e, 0x00]
#bus.write_i2c_block_data(0x51, cmd_init3[0], cmd_init3[1:5])
#chk = bus.read_byte(0x51)





    

'''
for i in range(0,24):
    for j in range (0,16):
        print "{}".format(hex(bus.read_byte_data(DEV_ADDR, (i*16)+j))),
    print (" ")
print ("----------------")


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
