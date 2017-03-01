import os
import lab
import pylab
import numpy as np
import uncertainties
import sys
import scipy.stats
import scipy.integrate

import getpass
users={"candi": "C:\\Users\\candi\\Documents\\GitHub\\Lab3.2\\",
"silvanamorreale":"C:\\Users\\silvanamorreale\\Documents\\GitHub\\Lab3.2\\" ,
"Studenti": "C:\\Users\\Studenti\\Desktop\\Lab3\\",
"User":"C:\\Users\\User\\Documents\\GitHub\\Lab3.2\\"
}
try:
    user=getpass.getuser()
    path=users[user]
    print("buongiorno ", user, "!!!")
except:
    raise Error("unknown user, please specify it and the path in the file Esercitazione*.py")


sys.path = sys.path + [path]
dir= path + "2_E-m\\"

xdata, ydata=np.loadtxt(dir+"B in r.txt", unpack=True)
dydata=lab.mme(ydata, "volt")
dxdata=np.ones(xdata.shape)*0.001




pylab.errorbar(xdata, ydata, dydata, dxdata)


epsilon=1e-5
def field(r, R, z0, I):
    r=np.abs(r)+epsilon
    A=(R**2+r**2+z0**2)
    fun=lambda teta: R*(R-r*np.cos(teta))/(A-2*R*r*np.cos(teta))**3/2
    return I*scipy.integrate.quad(fun,0 ,2*np.pi)  #scusate per l'integrazione numerica, ma che si può fare altrimenti???



def myfield(r, R, z0, I):
    for i in r:
        yield field(i, R, z0, I)



pylab.figure(1)
pylab.title("singola spira")
domain=np.linspace(-1, 1)
for z in np.linspace(0.5, 2, 10):
    pylab.plot(domain, list(myfield(domain, 1, z, 1)))

pylab.figure(2)
pylab.title("doppia")
for z in np.linspace(0.5, 1.5, 10):
    pylab.plot(domain, np.array(list(myfield(domain, 3, z, 1)))+np.array(list(myfield(domain, 3, 2-z, 1))))
    






