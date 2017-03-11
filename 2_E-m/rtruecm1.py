import os
import lab
import pylab
import numpy as np
import uncertainties
import sys
import scipy.stats
import scipy.integrate
from uncertainties import *
from scipy.integrate import quad
import math

#prima di esegiure questo esegui BRcal
pylab.close("all")

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




ids = [i for i in range(11,29)] + [30,32,33,35,37,39,41,44,45,46,48,50]

preprevacc = [299, 294, 288, 281, 273, 267, 258, 250, 243, 237, 230, 221, 216, 210, 204, 195, 188, 180, 239, 239, 192, 192, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252]

prepreicoil = [1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.28, 1.28, 1.35, 1.35, 1.40, 1.40, 1.46, 1.46, 1.52, 1.52, 1.61, 1.61, 1.71, 1.71, 1.81, 1.81, 1.90, 1.90]


AAA=-2048+3344
BBB=-1925+3507
fact1=BBB/AAA

BBBP=-2096+3344
AAAP=-2199+3309
fact2=BBBP/AAAP

factm=fact1#(fact1+fact2)/2
facter=0.68*(fact1-fact2)/2

fact=uncertainties.ufloat(factm, facter)

#R0 = 15
D = ufloat(52.5, 0.2)
d = ufloat(45.0, 0.4)
#D=1
#d=1

prevacc = [preprevacc[i-11] for i in ids]
preicoil = [prepreicoil[i-11] for i in ids]

# per ottenere rls lanciare fitcircle.py nella shell, per calibrazionels lanciare calibrazione.py
rtls = [0 for i in range(0,len(rls))]

for i in range(0,len(rls)):
    rtls[i] = rls[i]/calibrazionels[i]
    
vacc = [ufloat(0,0) for i in range(0,len(prevacc))]

for i in range(0,len(prevacc)):
    vacc[i] = ufloat(prevacc[i],1)

icoil = [ufloat(0,0) for i in range(0,len(preicoil))]

for i in range(0,len(preicoil)):
    icoil[i] = ufloat(preicoil[i],0.01)

    
## Correzione prospettica
    
rtt = [0 for i in range(0,len(rtls))]

for i in range(0,len(rtls)):
    rtt[i] = (rtls[i]*d/D)*(fact)

## Campo  magnetico


rtt=np.array(rtt)*1e-2
iB = [ufloat(0,0) for i in range(0,len(icoil))]

for i in range(0,len(preicoil)):
   iB[i] = BBR(rtt[i], icoil[i])*1e-4  #in tesla!!!!
   print(iB[i], rtt[i], icoil[i])
   print(BB0field(rtt[i].n))
    
## Calcolo di e/m
    
em =[] #[ufloat(0,0) for i in range(0,len(iB))]
emn=[]#[0 for i in range(0,len(iB))]
ems=[]#[0 for i in range(0,len(iB))]
for i in range(0,len(preicoil)):
    if(rtt[i].s/rtt[i].n<0.20):
        em.append(2*vacc[i]/((iB[i]*rtt[i])**2))
        print(iB[i])
        print(7.8e-4*icoil[i])
        print(i)
        emn.append(em[len(em)-1].n)
        ems.append(em[len(em)-1].s)
    else:
        print("tolto")

def PN(l):
    ret=[]
    for ll in l:
        ret.append(ll.n)
    return ret

def PS(l):
    ret=[]
    for ll in l:
        ret.append(ll.n)
    return ret



pylab.errorbar(range(len(em)), emn, ems)
pylab.figure(2)
pylab.errorbar(range(len(iB)), PN(iB))
print(em)
print(np.array(ems)/np.array(emn))
EM, EEM=lab.fit_const_yerr(emn, ems)
print(uncertainties.ufloat(EM, EEM**0.5))

#scusate, stò fittano una cosa sbagliata....m/e , mica e/m!!!!!!!!!!!

pylab.figure(200)
out=[((iB[i]*rtt[i])**2).n for i in range(len(rtt)) if rtt[i].s/rtt[i].n<0.20]
outs=[((iB[i]*rtt[i])**2).s for i in range(len(rtt)) if rtt[i].s/rtt[i].n<0.20]
vacca=[vacc[i].n for i in range(len(rtt)) if rtt[i].s/rtt[i].n<0.20]
vaccas=[vacc[i].s for i in range(len(rtt))if rtt[i].s/rtt[i].n<0.20]
pylab.errorbar(vacca, out,outs, vaccas, fmt='.') 
em, emq=lab.curve_fit(lambda x, a, b: a*x+b, vacca, out,sigma=outs)
print(em)
pylab.plot(vacca, [em[0]*vacca[i]+em[1] for i in range(len(rtt)) if rtt[i].s/rtt[i].n<0.20])

EMH, EMI = uncertainties.correlated_values(em, emq)






#iiB=uncertainties.unumpy.uarray(iB)
pylab.figure(201)
pylab.title("$V_{acc}$ vs $(Br)^2$")
pylab.xlabel("$V_{acc}$ [V]")
pylab.ylabel("$(BR)^2$ [$T^2m^2$]")
out=[((iB[i]*rtt[i])**2).n for i in range(len(rtt)) if rtt[i].s/rtt[i].n<0.20]
outs=[((iB[i]*rtt[i])**2).s for i in range(len(rtt)) if rtt[i].s/rtt[i].n<0.20]
vacca=[vacc[i].n for i in range(len(rtt)) if rtt[i].s/rtt[i].n<0.20]
vaccas=[vacc[i].s for i in range(len(rtt)) if rtt[i].s/rtt[i].n<0.20]
pylab.errorbar(vacca, out,outs, vaccas, fmt='.') 
em, emq=lab.curve_fit(lambda x, a: a*x, vacca, out,sigma=outs)
print(em)
pylab.plot(vacca, [em[0]*vacca[i] for i in range(len(rtt)) if rtt[i].s/rtt[i].n<0.20])
pylab.savefig(dir+"\\grafici\\VaccBRq.pdf")
ME=uncertainties.ufloat(em, emq**0.5)
print(2/ME)
