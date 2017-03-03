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


ids = [i for i in range(11,29)] + [30,32,33,35,37,39,41,44,45,46,48,50]

preprevacc = [299, 294, 288, 281, 273, 267, 258, 250, 243, 237, 230, 221, 216, 210, 204, 195, 188, 180, 239, 239, 192, 192, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252]

prepreicoil = [1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.28, 1.28, 1.35, 1.35, 1.40, 1.40, 1.46, 1.46, 1.52, 1.52, 1.61, 1.61, 1.71, 1.71, 1.81, 1.81, 1.90, 1.90]


AAA=-2048+3344
BBB=-1925+3507

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
    rtt[i] = (rtls[i]*d/D)*(BBB/AAA)

## Campo  magnetico


rtt=np.array(rtt)*1e-2
iB = [ufloat(0,0) for i in range(0,len(icoil))]

for i in range(0,len(preicoil)):
   iB[i] = BBR(rtt[i], icoil[i])*1e-4  #in tesla!!!!
   print(iB[i], rtt[i], icoil[i])
   print(BB0field(rtt[i].n))
    
## Calcolo di e/m
    
em = [ufloat(0,0) for i in range(0,len(iB))]
emn=[0 for i in range(0,len(iB))]
ems=[0 for i in range(0,len(iB))]
for i in range(0,len(preicoil)):
    em[i] = 2*vacc[i]/((iB[i]*rtt[i])**2)
    print(iB[i])
    print(7.8e-4*icoil[i])
    print(i)
    emn[i]=em[i].n
    ems[i]=em[i].s

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
out=[((iB[i]*rtt[i])**2).n for i in range(len(rtt))]
outs=[((iB[i]*rtt[i])**2).s for i in range(len(rtt))]
vacca=[vacc[i].n for i in range(len(rtt))]
vaccas=[vacc[i].s for i in range(len(rtt))]
pylab.errorbar(vacca, out,outs, vaccas, fmt='.') 
em, emq=lab.curve_fit(lambda x, a, b: a*x+b, vacca, out,sigma=outs)
print(em)
pylab.plot(vacca, [em[0]*vacca[i]+em[1] for i in range(len(rtt))])

EMH, EMI = uncertainties.correlated_values(em, emq)




#iiB=uncertainties.unumpy.uarray(iB)
pylab.figure(201)
out=[((iB[i]*rtt[i])**2).n for i in range(len(rtt))]
outs=[((iB[i]*rtt[i])**2).s for i in range(len(rtt))]
vacca=[vacc[i].n for i in range(len(rtt))]
vaccas=[vacc[i].s for i in range(len(rtt))]
pylab.errorbar(vacca, out,outs, vaccas, fmt='.') 
em, emq=lab.curve_fit(lambda x, a: a*x, vacca, out,sigma=outs)
print(em)
pylab.plot(vacca, [em[0]*vacca[i] for i in range(len(rtt))])

