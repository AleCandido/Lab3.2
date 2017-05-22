import sys
import pylab
from scipy.optimize import curve_fit
from scipy.stats import chisqprob
import numpy as np
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


print("===========PASSABANDA==============")

print("valori attesi...")

def myres(r):
    return uncertainties.ufloat(r, mme(r, "ohm"))

R2=myres(119.1)
C1=10.78e-9
C2=10.67e-9
R1=myres(2.68e3)
R3=myres(46.6e3)

Rp=R1*R2/(R1+R2)
C=C1
w0_exp=(1/(C*(Rp*R3)**0.5))#/(2*np.pi)
f0_exp=(1/(C*(Rp*R3)**0.5))/(2*np.pi)

Q_exp=0.5*(R3/Rp)**0.5
Dw_exp=w0_exp/Q_exp
Df_exp=f0_exp/Q_exp


R1p=myres(9.92e2) #questa resistenza è sbagliata... non so se è grave o meno, ma si spiega perchè la nostra amplificazione è minore...è compatibile con quanto ottenuto dal fit
R2p=myres(33.2e3)
R3p=myres(3.91e3)

g00=1/(R1*C*Dw_exp)*(R2p/R1p+1)

print("f0_exp={}    Q_exp={}    g00={}".format(f0_exp, Q_exp, g00))


pylab.figure(figsnum)


figsnum+=1
pylab.title("amplificazione passa-banda")
pylab.xlabel("frequenza [Hz]")
pylab.ylabel("A($f$)")

###############Acquisizione dati

dir_grph=dir+"grafici/"
dir = dir + "data/"

file="passabanda.txt"
f, vin, vout = loadtxt(dir+file,unpack=True)
f=f*1e3
Df=51/1e6*f

amp=vout/vin
dvout=mme(vout, "volt", "oscil")
dvin=mme(vin, "volt", "oscil")
damp=amp*((dvout/vout)**2+(dvin/vin)**2)**0.5



##############Fit...

#attenzione...A non è adimensionale...se passo dalle frequenze alle pulsazioni A dovrebbe scalare di 2*pi

g=lambda w, A, Q, w0: A*w/((w**2-w0**2)**2+w**2*w0**2/Q)**0.5
p0=(185, 10, 6.1e3)
dof=len(f)-3
pars, covs = curve_fit(g, f, amp,p0, damp, maxfev=10000)
A, Q, w0=uncertainties.correlated_values(pars, covs)


#############plot...
pylab.loglog()
pylab.errorbar(f, amp, damp,Df,fmt=".")
domain = pylab.logspace(math.log10(min(f)),math.log10(max(f)), 1000)
gdomain = g(domain, *pars)
pylab.plot(domain, gdomain)
pylab.xlim(min(domain)*0.9,max(domain)*1.1)
vint = pylab.vectorize(int)
pylab.xticks(vint((pylab.logspace(log10(min(domain)*0.9),log10(max(domain)*1.1), 5)//100)*100),vint((pylab.logspace(log10(min(domain)*0.9),log10(max(domain)*1.1), 5)//100)*100))
pylab.ylim(min(gdomain)*0.9, max(gdomain)*1.1)
pylab.yticks(vint((pylab.logspace(log10(min(gdomain)*0.9),log10(max(gdomain)*1.1), 5)//10)*10),vint((pylab.logspace(log10(min(gdomain)*0.9),log10(max(gdomain)*1.1), 5)//10)*10))
pylab.savefig(dir_grph+"passabanda.pdf")


############output parametri...

print("A={} w0={} Q_true={}".format(A, w0, Q**0.5))

for i, j in enumerate(pars):
    print(i, pars[i], covs[i, i]**0.5)

chisq=np.sum((amp-g(f, *pars))**2/damp**2)
print("chisq=", chisq, dof, chisqprob(chisq,dof))

Dw=w0/Q**0.5 #larghezza di banda (si chiama w, ma è una frequenza...)...


#controllo sui parametri
print("controllo di essere davvero a -3dB")

print("2**0.5  - g(w0, A, Q, w0)/g(w0+Dw/2, A, Q, w0) =  ",sqrt(2)-g(w0, A, Q, w0)/g(w0+Dw/2, A, Q, w0))

print("2**0.5  - g(w0, A, Q, w0)/g(w0-Dw/2, A, Q, w0) =  ",sqrt(2)-g(w0, A, Q, w0)/g(w0-Dw/2, A, Q, w0))

A3=g(w0, A, Q, w0) #amplificazione di centrobanda (con errori...)

#A, Q, w0=uncertainties.correlated_values(pars, covs)
print("guadagno centro banda=", g(w0, A, Q, w0))


print("Risultati A={} Q={} w0={}  Dw={}".format(A, Q**0.5, w0, Dw))

print("Il Q value non è compatibile con quanto atteso...")



dom=np.linspace(min(f), max(f), 1000)
integrale=np.sum(g(dom, A, Q, w0)**2)*(max(f)-min(f))/1000/A3**2
print("-----------", integrale, np.pi/2*Dw)

Df_true=integrale


