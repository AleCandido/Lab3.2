import numpy as np
import uncertainties
from uncertainties import *
import sys
import scipy.stats
import scipy.integrate
import pylab
import os



def B(V):
    '''Volt to gauss B field'''
    return V*1e3/(ufloat(5.0,0.1)*ufloat(11.09, 0.003))

R=15e-2
z0=15e-2
I=1

epsilon=1e-6
def field(r):
    r=np.abs(r)+epsilon
    A=(R**2+r**2+z0**2)
    fun=lambda teta: R*(R-r*np.cos(teta))/(A-2*R*r*np.cos(teta))**3/2
    return I*scipy.integrate.quad(fun,0 ,2*np.pi)[0]



def BB0field(r):
    return field(r)/field(0)


def dBB0field(r):
    return (BB0field(r+epsilon)-BB0field(r))/epsilon

def UBB0field(r):
    return ufloat(BB0field(r.n), abs((r.s)*dBB0field(r.n)))

pylab.figure(0)
dom=np.linspace(0, 15e-2, 100)
pylab.plot(dom, np.vectorize(BB0field)(dom))

#####################################controllo la linearità I-V

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

xdata, ydata=np.loadtxt(dir+"dati IB.txt", unpack=True)




xdata=xdata[0:len(xdata)-1]
ydata=ydata[0:len(ydata)-1]
#dydata=np.ones(xdata.shape)*lab.mme(np.max(ydata),"volt")
dydata=lab.mme(ydata,"volt")
dxdata=lab.mme(xdata, "ampere")
print("si è stimato che gli errori sugli ampere fossero gli stessi dati dal multimetro digitale...sarà vero? esiste un manuale?")
print("stessa cosa per B")
retta=lambda x, m, q: m*x+q
cost=lambda x, m, q: m
a, b=lab.fit_generic_xyerr(retta, cost, xdata, ydata, dxdata, dydata)
dom=np.linspace(min(xdata), max(xdata), 100)
m, q=a
pylab.plot(dom, retta(dom, m, q), color='b')
pylab.errorbar(xdata, ydata, dydata, dxdata)
M, Q=uncertainties.correlated_values(a, b)
print(M, Q)
chiq=sum((ydata-retta(xdata, m, q))**2/(dxdata**2+dydata**2))
print(chiq ,len(xdata-1),1-scipy.stats.chi2(len(xdata)-1).cdf(chiq))
print("bene, o gli errori sono sbagliati o non è effettivamente una retta!!!!!")




xdata=xdata[0:len(xdata)-1]
ydata=ydata[0:len(ydata)-1]
#dydata=np.ones(xdata.shape)*lab.mme(np.max(ydata),"volt")
dydata=lab.mme(ydata,"volt")
dxdata=lab.mme(xdata, "ampere")
print("si è stimato che gli errori sugli ampere fossero gli stessi dati dal multimetro digitale...sarà vero? esiste un manuale?")
print("stessa cosa per B")
retta=lambda x, m: m*x
cost=lambda x, m: m
a, b=lab.fit_generic_xyerr(retta, cost, xdata, ydata, dxdata, dydata)
dom=np.linspace(min(xdata), max(xdata), 100)
m=a
pylab.plot(dom, retta(dom, m), color='b')
pylab.errorbar(xdata, ydata, dydata, dxdata)
M=uncertainties.ufloat(a, b)
print(M)
chiq=sum((ydata-retta(xdata, m))**2/(dxdata**2+dydata**2))
print(chiq ,len(xdata-1),1-scipy.stats.chi2(len(xdata)-1).cdf(chiq))
print("bene, o gli errori sono sbagliati o non è effettivamente una retta!!!!!")


def BB(I):
    return B(M*I)

def BBR(r, I):
    return UBB0field(r)*BB(I)

def lBBR(r, I):
    for rr, ii in zip(r, I):
        yield BBR(rr, ii)

print("Bene, il campo magnetico è noto al 5%")
    

####################################fitting B(r)




