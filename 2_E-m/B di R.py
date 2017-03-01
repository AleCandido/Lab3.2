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

def field(r, R, z0, I):
    x=R/r
    y=(R**2+r**2+z0**2)/Rr
    fun=lambda teta: (x-np.cos(teta))/(y-2*np.cos(teta))
    return I*scipy.integrate.quad(fun,0 ,2*np.pi)


pylab.figure(1)
domain=np.linspace(-1, 1)
pylab.plot(domain, field(domain, 1, 1, 1))

