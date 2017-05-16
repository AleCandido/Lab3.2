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





close("all")
dir_grph=dir+"grafici/"
dir = dir + "data/"


file="postpreamp.txt"
f, vin, vout = loadtxt(dir+file,unpack=True)


amp=vout/vin
dvout=mme(vout, "volt", "oscil")
dvin=mme(vin, "volt", "oscil")
damp=((dvout/vout)**2+(dvin/vin)**2)**0.5

pylab.loglog()
pylab.errorbar(f, amp, damp, fmt=".")


low_pass=lambda w, A0, w0: A0/(1+w/w0)
p0=(14.4, 27e3)
dof=len(f)-2
pars, covs=lab.curve_fit(low_pass, f, amp,p0, damp)



pylab.plot()



domain = pylab.logspace(math.log10(min(f)),math.log10(max(f)), 1000)
pylab.plot(domain, low_pass(domain, *pars))
pylab.show()




R2=uncertainties.ufloat(4.71e3, mme(4.71e3, "ohm"))
R3=uncertainties.ufloat(67.9e3, mme(67.9e3, "ohm"))

amp_exp=R3/R2
print("exp_amp=", amp_exp)

for i, j in enumerate(pars):
    print(i, pars[i], covs[i, i]**0.5)

chisq=np.sum((amp-low_pass(f, *pars))**2/damp**2)
print(chisq, dof, chisqprob(chisq,dof))


#ergo il chiq non torna manco per il cazzo!!!....

#pylab.errorbar()