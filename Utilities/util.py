import numpy as np
import lab
import uncertainties
from operator import *

defoult_hwindow=30


def findLocal(data, hwindow, f1, f2, f3):
    maxs=[]
    for i in range(hwindow, len(data)-hwindow):
        if(f2(data[i], f1(data[i-hwindow: i])) and f3(data[i],f1(data[i+1: i+hwindow+1]))):
           maxs.append(i)
    return maxs

findLocalMaxs=(lambda x: lambda data, hwindow: x(data, hwindow, np.amax, gt, ge))(findLocal) #si mi piace supercazzolare, e si, è diverso...
findLocalMaxs.__doc__=    '''
    trova i massimi assoluti delle sottofinestre di semilarghezza hwindow
    data:   dati, np array
    hwindow:    intero, semilarghezza della finestra (larghezza finestra = 2*hwindow+1)
    return lista indici massimi
    '''

findLocalMins=(lambda x: lambda data, hwindow: x(data, hwindow, np.amin, lt, le))(findLocal) 
findLocalMins.__doc__= '''
    trova i minimi assoluti delle sottofinestre di semilarghezza hwindow
    data:   dati, np array
    hwindow:    intero, semilarghezza della finestra (larghezza finestra = 2*hwindow+1)
    return lista indici massimi
    '''


def BetterFindLocal(ydata, dydata, hwindow, f1, f2):
    '''approssima i massimi come parabole e con questo cerca il vero massimo. Se fornita degli errori sulle y fa un lavoretto migliore....'''
    massimi=[]
    candidati=f1(ydata, hwindow)
    p=lambda x, A, B, C: A*x**2+B*x+C
    for i in candidati:
        par, covs = lab.curve_fit(p, np.array(range(-hwindow, hwindow)), ydata[i-hwindow: i+hwindow], sigma=dydata)
        corpar=uncertainties.correlated_values(par, covs)
        A, B, C=corpar
        if(f2(A, 0)):
            print("Warning!!!")
        massimi.append((i,ydata[i], par, covs, -B/2*A, -B**2/(4*A)+C))
    return massimi


#be, così non ci si capisce più nulla no!!!
BetterFindLocalMaxs=(lambda x, y:lambda ydata, dydata, hwindow=defoult_hwindow: y(ydata, dydata, hwindow, x, ge))(findLocalMaxs, BetterFindLocal)
BetterFindLocalMins=(lambda x, y:lambda ydata, dydata, hwindow=defoult_hwindow: y(ydata, dydata, hwindow, x, le))(findLocalMins, BetterFindLocal)

