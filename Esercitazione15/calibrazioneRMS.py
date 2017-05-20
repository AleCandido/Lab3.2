#calibrazione rms converter

import sys
import pylab
from scipy.optimize import curve_fit
from scipy.stats import chisqprob

import getpass
users={"candi": "C:\\Users\\candi\\Documents\\GitHub\\Lab3.2\\",
"silvanamorreale":"C:\\Users\\silvanamorreale\\Documents\\GitHub\\Lab3.2\\" ,
"Studenti": "C:\\Users\\Studenti\\Desktop\\Lab3\\",
"User":"C:\\Users\\User\\Documents\\GitHub\\Lab3.2\\",
"andrea": "/home/andrea/Documenti/Da salvare 12-5-2017/Documenti/GitHub/Lab3.2/",
"viviana": "C:\\Users\\viviana\\Documents\\GitHub\\Lab3.2\\"
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

print("================Calibrazione RMS=========")

pylab.figure(figsnum)
figsnum+=1
pylab.title("RMS-oscilloscopio vs RMS-true RMS converter")
pylab.xlabel("RMS oscilloscopio [V]")
pylab.ylabel("RMS true RMS converter")


dir_grph=dir+"grafici/"
dir = dir + "data/"


file="calibrazioneRMS.txt"
vchip, voscil = loadtxt(dir+file,unpack=True)

dvchip=mme(vchip, "volt", "oscil")
dvoscil=mme(voscil, "volt", "oscil")

pylab.errorbar(voscil, vchip, dvchip, dvoscil, fmt=".")
line=lambda x, a, b: a*x+b
pend=lambda x, a, b: a
p0=(1, 0)

pars, covs=lab.fit_generic_xyerr(line, pend, voscil, vchip, dvoscil, dvchip, p0)
a, b=uncertainties.correlated_values(pars, covs)


domain=np.linspace(min(voscil), max(voscil), 1000)
pylab.plot(domain, line(domain, *pars))
pylab.savefig(dir_grph+"calibrazione.pdf")

chisq=np.sum((vchip-line(voscil, *pars))**2/(dvchip**2+(dvoscil*pend(voscil, *pars))**2))
print(chisq, dof, chisqprob(chisq,dof))


A4=a

