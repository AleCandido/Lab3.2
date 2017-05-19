import numpy as np
from numpy import *
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


print("==============PRE PRE AMP===========")


pylab.figure(figsnum)
figsnum+=1
pylab.title("pre-pre-amp")


#pylab.close("all")
dir_grph=dir+"grafici/"
dir = dir + "data/"


file="prepreamp.txt"
f, vin, vout = loadtxt(dir+file,unpack=True)


amp=vout/vin
dvout=mme(vout, "volt", "oscil")
dvin=mme(vin, "volt", "oscil")
damp=((dvout/vout)**2+(dvin/vin)**2)**0.5

pylab.loglog()
pylab.errorbar(f, amp, damp, fmt=".")


low_pass=lambda w, A0, w0: A0/(1+(w/w0)**2)**0.5
p0=(14.4, 27e3)
dof=len(f)-2
pars, covs=lab.curve_fit(low_pass, f, amp,p0, damp)
A0, w0=uncertainties.correlated_values(pars, covs)




domain = pylab.logspace(math.log10(min(f)),math.log10(max(f)), 1000)
pylab.plot(domain, low_pass(domain, *pars))
pylab.savefig(dir_grph+"prepreamp.pdf")
pylab.show()




R1=uncertainties.ufloat(989, mme(989, "ohm"))

amp_exp=1+50e3/R1
print("exp_amp=", amp_exp)

for i, j in enumerate(pars):
    print(i, pars[i], covs[i, i]**0.5)

chisq=np.sum((amp-low_pass(f, *pars))**2/damp**2)
prob=chisqprob(chisq,dof)
print(chisq, dof, chisqprob(chisq,dof))

print("Parametri fittati: A={} w0={} chisq={} prob={}".format(A0, w0, chisq, prob))


#####stima autonoma...

primi=amp[f<8e3]
dprimi=damp[f<8e3]
NN=len(primi)


amp_mean=np.sum(primi/dprimi)/np.sum(1/dprimi)
amp_var=np.sqrt(np.sum((primi-amp_mean)**2/dprimi**2)/np.sum(1/dprimi**2))

print("fit fino a 8 KHz= ", amp_mean, amp_var)

A2=A0

#ergo il chiq non torna manco per il cazzo!!!....

#pylab.errorbar()