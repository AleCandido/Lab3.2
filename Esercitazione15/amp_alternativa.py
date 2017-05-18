import sys
import numpy as np
from numpy.lib.stride_tricks import as_strided
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


print("===============Stima strna=================")



#####partitore....

R1=uncertainties.ufloat(9.91e3, mme(9.91e3, "ohm"))
R2=uncertainties.ufloat(10.1, mme(10.1, "ohm"))



pylab.figure(figsnum)
figsnum+=1


#pylab.close("all")
dir_grph=dir+"grafici/"
dir = dir + "data/"


file="totamp.txt"
f, Vin, Vout, Vrms = np.loadtxt(dir+file,unpack=True)
Vin=Vin*1e-3
dVin=mme(Vin, "volt", "oscil")
dVout=mme(Vout, "volt", "oscil")

UVin=uncertainties.unumpy.uarray(Vin, dVin)*R2/(R1+R2)
UVout=uncertainties.unumpy.uarray(Vout, dVout)
Uamp=UVout/UVin

amp=uncertainties.unumpy.nominal_values(Uamp)
damp=uncertainties.unumpy.std_devs(Uamp)


pylab.errorbar(f, amp, damp, fmt='.')


g=lambda w, A, Q, w0: A*w/((w**2-w0**2)**2+w**2*w0**2/Q)**0.5

p0=(1e8, 10, 6.5e3)
dof=len(f)-3
pars, covs=lab.curve_fit(g, f, amp,p0, damp, maxfev=10000)
A, Q, w0=uncertainties.correlated_values(pars, covs)
print("A= {} \n Q={}\n w0={}\n".format(A, Q, w0))

domain=np.linspace(min(f), max(f), 1000)
pylab.plot(domain, g(domain, *pars))
pylab.savefig(dir_grph+"lastfit.pdf")



A_supp=g(w0, A, Q, w0)
Dw_supp=w0/Q




pylab.show()







