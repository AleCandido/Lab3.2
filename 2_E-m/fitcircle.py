import numpy
import pylab
import math
from scipy.optimize import curve_fit

#per le notazioni guardare il file pdf 'circle fit'
x,y= pylab.loadtxt( 'C:\\Users\\candi\\Documents\\GitHub\\Lab3.2\\2_E-m\\data\\12.txt' , unpack = True)

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
suv = sum(u*v)
svv = sum(v**2)
suuu = sum(u**3)
suvv = sum(u*(v**2))
suuv = sum(v*(u**2))
svvv = sum(v**3)

# risolvo sistema per trovare coordinate centro circonferenza
det = suv**2 - suu*svv
det1 = ((svvv+suuv)*suv - (suuu+suvv)*svv)/2
det2 = ((suuu+suvv)*suv - (svvv+suuv)*suu)/2
uc = det1/det
vc= det2/det
xc= uc + mx
yc= (vc + my)
print('xc =', xc)
print('yc =', yc)
r = math.sqrt((uc**2) + (vc**2) + (suu+svv)/len(x))
pylab.plot(xc,yc, marker = 'o')
print('r=', r)

x = numpy.linspace(xc - r + 1, xc + r -1, 1000)
y = numpy.sqrt(r**2-(x-xc)**2) +yc
pylab.plot(x,y, color = 'black')

x1 = numpy.linspace(xc - r + 1, xc + r -1, 1000)
y1 = - numpy.sqrt(r**2-(x-xc)**2) +yc
pylab.plot(x1,y1, color = 'black')

pylab.show()
