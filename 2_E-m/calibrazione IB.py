import os
import lab
import pylab
import numpy as np
import uncertainties
import sys
import scipy.stats


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

dydata=lab.mme(ydata,"volt")
dxdata=lab.mme(xdata, "ampere")
print("si è stimato che gli errori sugli ampere fossero gli stessi dati dal multimetro digitale...sarà vero? esiste un manuale?")
print("stessa cosa per B")
retta=lambda x, m, q: m*x+q
cost=lambda x, m, q: m
a, b=lab.fit_generic_xyerr(retta, cost, xdata, ydata, dxdata, dydata)
dom=np.linspace(min(xdata), max(xdata), 100)
m, q=a
pylab.plot(dom, retta(dom, m, q))
pylab.errorbar(xdata, ydata, dydata, dxdata)
M, Q=uncertainties.correlated_values(a, b)
print(M, Q)
chiq=sum((ydata-retta(xdata, m, q))**2/(dxdata**2+dydata**2))
print(chiq ,len(xdata-1),1-scipy.stats.chi2(len(xdata)-1).cdf(chiq))
print("bene, o gli errori sono sbagliati o non è effettivamente una retta!!!!!")

