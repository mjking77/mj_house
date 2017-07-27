f = open('script_test.txt','r')
flist = f.readlines()
f.close()
print flist

print '--------------------'
for i in range(0,len(flist)):
    if flist[i].find('wriu')==True:
        print flist[i]
    #print "{}".format(flist[i])




