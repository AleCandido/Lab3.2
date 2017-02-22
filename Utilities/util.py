import numpy as np
import lab
import uncertainties
from operator import *

#todo sarebbe meglio avere una sola, è codice identico...ma ci sono problemi con i <=... che in fondo sono solo altre fun...

def oldfindLocalMaxs(data, hwindow):
    '''
    trova i massimi assoluti delle sottofinestre di semilarghezza hwindow
    data:   dati, np array
    hwindow:    intero, semilarghezza della finestra (larghezza finestra = 2*hwindow+1)
    return lista indici massimi
    '''
    maxs=[]
    for i in range(hwindow, len(data)-hwindow):
        if(data[i]>np.amax(data[i-hwindow: i]) and data[i]>=np.amax(data[i+1: i+hwindow+1])):
           maxs.append(i)
    return maxs


def oldfindLocalMins(data, hwindow):
    '''
    trova i minimi assoluti delle sottofinestre di semilarghezza hwindow
    data:   dati, np array
    hwindow:    intero, semilarghezza della finestra (larghezza finestra = 2*hwindow+1)
    return lista indici massimi
    '''
    maxs=[]
    for i in range(hwindow, len(data)-hwindow):
        if(data[i]<np.amin(data[i-hwindow: i]) and data[i]<=np.amin(data[i+1: i+hwindow+1])):
           maxs.append(i)
    return maxs

def findLocal(data, hwindow, f1, f2, f3):
    maxs=[]
    for i in range(hwindow, len(data)-hwindow):
        if(f2(data[i], f1(data[i-hwindow: i])) and f3(data[i],f1(data[i+1: i+hwindow+1]))):
           maxs.append(i)
    return maxs

findLocalMaxs=lambda data, hwindow: findLocal(data, hwindow, np.amax, gt, ge)
findLocalMaxs.__doc__=    '''
    trova i massimi assoluti delle sottofinestre di semilarghezza hwindow
    data:   dati, np array
    hwindow:    intero, semilarghezza della finestra (larghezza finestra = 2*hwindow+1)
    return lista indici massimi
    '''

findLocalMins=lambda data, hwindow: findLocal(data, hwindow, np.amax, lt, le)
findLocalMins.__doc__= '''
    trova i minimi assoluti delle sottofinestre di semilarghezza hwindow
    data:   dati, np array
    hwindow:    intero, semilarghezza della finestra (larghezza finestra = 2*hwindow+1)
    return lista indici massimi
    '''


def BetterFindLocalMax(ydata, dydata, hwindow=5):
    '''approssima i massimi come parabole e con questo cerca il vero massimo. Se fornita degli errori sulle y fa un lavoretto migliore....'''
    massimi=[]
    candidati=findLocalMaxs(ydata, hwindow)
    for i in candidati:
        par, covs = lab.curve_fit(lambda x, A, B, C: A*x**2+B*x+C, np.array(range(-hwindow, hwindow)), ydata[i-hwindow: i+hwindow], sigma=dydata)
        corpar=uncertainties.correlated_values(par, covs)
        A, B, C=corpar
        if(A>0):
            print("Warning!!!")
        massimi.append((i,ydata[i], par, covs, -B/2*A, -B**2/(4*A)+C))
    return massimi


    
    
    