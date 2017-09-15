import matplotlib.pyplot as plt
import numpy as np


###CLASS   ??

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return("Point1 at [%f  %f]" % (self.x, self.y))

pt1 = Point1(2, 0.7)
print pt1
pt1.translate(1, 3.3)
print pt1            ##??


#"list", "dictionary"
###CONTROL FLOW_ "if", "for"
state1 = True
list1 = ["AAA", "BB", "CCC"]
dict1 = {"para1": 1.0, "para2":2.0, "para3":3.0}
k=0

if state1:
    print 'positive'
else:
    print 'negative'

for i in range(-3,3,1):
    print(i)

for i in list1:
    print(i)

for para, val in dict1.items():
    print para + " = " + str(val)   #str() 
    
list2 = [x**2 for x in range(0,5)]  #init list as loop
print (list2)                       #py2.7 has pythonw runtime error

while k<5:
    print str(k) + ', done'
    k=k+1

    

###FUNCTION    
def powers(x):
    return x**3, x**4, x**5
p1, p2, p3=powers(3)
print p1,p2

def myfunc(x, p=2, dbg=False):
    if dbg:
        print '1st ='+str(x)+'and ^p = '+str(p)
    return x**p
print myfunc(5)
print myfunc(3,dbg=True)

##_MAP, pass a simple func as an argu to another func (lambda)
list2 = map(lambda x: x**2, range(-3,4))
print list2


### TRY-EXCEPTION
try:
    print 'try test....'
    print test_try
except Exception as e:
    print 'Caught a exception => :' + str(e)



###NUMPY
data1 = np.genfromtxt('test_data1.txt')
data1.shap
ax = plt.subplots(figsize=(14,4))



##_matplotlib (I)
x=np.arange(0,270)
y1=np.sin(x*np.pi/180)
y2=np.cos(x*np.pi/180)
y3=np.tan(x*np.pi/180)

plt.subplot(231)
plt.plot(x,y1,lw=3)
plt.title("1st")
plt.xticks(range(0,190,60))

plt.subplot(233)
plt.plot(x,y2,"ro")
plt.xlim(-10,300)
plt.ylim(-1.5,1.5)
          
plt.subplot(235)
plt.plot(x,y3,"y--",lw=5)          

#plt.show()



