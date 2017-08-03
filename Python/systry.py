import time

'''
f = open('TX_ATOP_8bits_1080_60P.txt','r')
flist = f.readlines()
f.close()
print flist



print '--------------------'
for i in range(0,len(flist)):
    if flist[i].find('wriu')==True:
        print flist[i]
    #print "{}".format(flist[i])
'''


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
            data = (int(str1[4],16))
            print hex(bkh), hex(bkl), hex(ost), hex(data)

    return;

load_script('TX_TIMING_1920x1080_60P.txt')

    
