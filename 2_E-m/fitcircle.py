import numpy
import pylab
import math
from scipy.optimize import curve_fit

#per le notazioni guardare il file pdf 'circle fit'
x,y= pylab.loadtxt( 'C:\\Users\\User\\Documents\\GitHub\\Lab3.2\\2_E-m\\data\\12.txt' , unpack = True)

dx = 1
dy = 1
pylab.grid()

pylab.xlim(0,max(x)*1.2)
pylab.ylim(0,max(y)*1.2)
pylab.xlabel('x')
pylab.ylabel('y')
pylab.errorbar(x,y,dy,dx, marker= 'o' , linestyle = 'None' , )

mx = sum(x)/len(x)
my = sum(y)/len(y)
u = x-mx
v = y-my
suu = sum(u**2)
suuu = sum(u**3)
suv = sum(u*v)
suvv = sum(u*(v**2))
svv = sum(v**2)
svvv = sum(v**3)
svuu = sum(v*(u**2))

# risolvo sistema per trovare coordinate centro circonferenza
det = suu*svv - suv**2
det1 = (0.5*(suuu+suvv)*svv)-(0.5*suv*(svvv+svuu))
det2 = (0.5*suu*(svvv+svuu))-(0.5*(suuu+suvv)*suv)
uc = det1/det
vc= det2/det
xc= uc + mx
yc= (vc + my)
print('xc =', xc)
print('yc =', yc)
R = math.sqrt((uc**2) + (vc**2) + (suu+svv)/len(x))
pylab.plot(xc,yc, marker = 'o')
print('R=', R)
x = numpy.linspace(min(x)-10, max(x)+10,1000)
y = numpy.sqrt(R**2-(x-xc)**2) +yc
pylab.plot(x,y, color = 'black')
pylab.show()
