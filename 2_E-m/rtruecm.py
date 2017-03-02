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

ids = [i for i in range(11,29)] + [30,32,33,35,37,39,41,44,45,46,48,50]

preprevacc = [299, 294, 288, 281, 273, 267, 258, 250, 243, 237, 230, 221, 216, 210, 204, 195, 188, 180, 239, 239, 192, 192, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252]

prepreicoil = [1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.28, 1.28, 1.35, 1.35, 1.40, 1.40, 1.46, 1.46, 1.52, 1.52, 1.61, 1.61, 1.71, 1.71, 1.81, 1.81, 1.90, 1.90]

R0 = 15
D = ufloat(52.5, 0.2)
d = ufloat(45.0, 0.4)

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
    rtt[i] = rtls[i]*d/D

## Campo  magnetico

def field(r, R, z0, I):
    r=np.abs(r)+epsilon
    A=(R**2+r**2+z0**2)
    fun=lambda teta: R*(R-r*np.cos(teta))/(A-2*R*r*np.cos(teta))**3/2
    return I*scipy.integrate.quad(fun,0 ,2*np.pi)[0] 
    
# derivate

epsilon=1e-4
def DfieldDr(r, I, a, z, R, O, errorscale=epsilon):
    return (field(r+espilon, I, a, z, R, O)-field(r, I, a, z, R, O))/epsilon

def DfieldDI(r, I, a, z, R, O, errorscale=epsilon):
    return (field(r, I+epsilon, a, z, R, O)-field(r, I, a, z, R, O))/epsilon
    
def DfieldDa(r, I, a, z, R, O, errorscale=epsilon):
    return (field(r, I, a+epsilon, z, R, O)-field(r, I, a, z, R, O))/epsilon
    
def DfieldDz(r, I, a, z, R, O, errorscale=epsilon):
    return (field(r, I, a, z+epsilon, R, O)-field(r, I, a, z, R, O))/epsilon
    
def DfieldDR(r, I, a, z, R, O, errorscale=epsilon):
    return (field(r, I, a, z, R+epsilon, O)-field(r, I, a, z, R, O))/epsilon
    
def DfieldDO(r, I, a, z, R, O, errorscale=epsilon):
    return (field(r, I, a, z, R, O+epsilon)-field(r, I, a, z, R, O))/epsilon

def Derive(f, i, epsilon=1e-6):
    def derivata(*pars):
        mypars=list(pars)
        mypars[i]+=epsilon
        return (f(*mypars)-f(*pars))/epsilon
    return derivata
    
# errore sul campo magnetico
    
def fieldErrorSq(x, dx, pars, dpars):
    return (dx**2)*Derive(field, 0)(x,*pars)**2+sum(dpars[i]*(Derive(field, 1+i)(r,*pars))**2 for i in range(0, len(pars))) 

B = [ufloat(0,0) for i in range(0,len(icoil))]

for i in range(0,len(preicoil)):
    B[i] = ufloat(field(rtt, R0, R0/2, icoil), dfield())
    
## Calcolo di e/m
    
em = [ufloat(0,0) for i in range(0,len(B))]

for i in range(0,len(preicoil)):
    em[i] = 2*vacc[i]/((B[i]*rtt[i])**2)
