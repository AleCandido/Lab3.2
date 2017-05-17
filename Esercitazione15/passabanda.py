import sys
import pylab
from scipy.optimize import curve_fit
from scipy.stats import chisqprob

import getpass
users={"candi": "C:\\Users\\candi\\Documents\\GitHub\\Lab3.2\\",
"silvanamorreale":"C:\\Users\\silvanamorreale\\Documents\\GitHub\\Lab3.2\\" ,
"Studenti": "C:\\Users\\Studenti\\Desktop\\Lab3\\",
"User":"C:\\Users\\User\\Documents\\GitHub\\Lab3.2\\",
"andrea": "/home/andrea/Documenti/Da salvare 12-5-2017/Documenti/GitHub/Lab3.2/"
}
try:
    user=getpass.getuser()
    path=users[user]
    print("buongiorno ", user, "!!!")
except:
    raise Error("unknown user, please specify it and the path in the file Esercitazione*.py")


sys.path = sys.path + [path]
dir= path + "Esercitazione15/"

from BuzzLightyear import * 
from lab import *
import uncertainties
import uncertainties.unumpy
###########################################################################


print("===========PASSABANDA==============")


pylab.figure(figsnum)
figsnum+=1


#pylab.close("all")
dir_grph=dir+"grafici/"
dir = dir + "data/"


file="passabanda.txt"
f, vin, vout = loadtxt(dir+file,unpack=True)

f=f*1e3

amp=vout/vin
dvout=mme(vout, "volt", "oscil")
dvin=mme(vout, "volt", "oscil")
damp=((dvout/vout)**2+(dvin/vin)**2)**0.5

pylab.loglog()
pylab.errorbar(f, amp, damp, fmt=".")

g=lambda w, A, Q, w0: A*w/((w**2-w0**2)**2+w**2*w0**2/Q)**0.5

p0=(185, 10, 6.1e3)
dof=len(f)-3
pars, covs=lab.curve_fit(g, f, amp,p0, damp, maxfev=10000)
A, Q, w0=uncertainties.correlated_values(pars, covs)



domain = pylab.logspace(math.log10(min(f)),math.log10(max(f)), 1000)
pylab.plot(domain, g(domain, *pars))
pylab.savefig(dir_grph+"passabanda.pdf")
pylab.show()

for i, j in enumerate(pars):
    print(i, pars[i], covs[i, i]**0.5)

chisq=np.sum((amp-g(f, *pars))**2/damp**2)
print(chisq, dof, chisqprob(chisq,dof))

A, Q, w0=uncertainties.correlated_values(pars, covs)
print("guadagno centro banda=", g(w0, A, Q, w0))

Dw=w0/Q
AMPE=g(w0, A, Q, w0)**2*(2*np.pi)**2*Dw

print("Risultati A={} Q={} w0={} Dw={} f0={} Df={} AMPE={}".format(A, Q, w0, Dw, 2*np.pi*w0, 2*np.pi*Dw, AMPE))

A3=g(w0, A, Q, w0)

EPB=(2*np.pi)**2*Dw