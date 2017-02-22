import numpy as np
import lab



#todo sarebbe meglio avere una sola, è codice identico...ma ci sono problemi con i <=... che in fondo sono solo altre fun...

def findLocalMaxs(data, hwindow):
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


def findLocalMins(data, hwindow):
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


def BetterFindLocalMax(ydata, dydata, hwindow=5):
    '''approssima i massimi come parabole e con questo cerca il vero massimo. Se fornita degli errori sulle y fa un lavoretto migliore....'''
    massimi=[]
    candidati=findLocalMaxs(ydata, hwindow)
    for i in candidati:
        par, covs = lab.curve_fit(lambda x, A, B, C: A*x**2+B*x+C, np.array(range(-hwindow, hwindow)), ydata[i-hwindow: i+hwindow], sigma=dydata)
        A, B, C=par
        massimi.append((i,ydata[i], par, covs, -B/2*A, -B**2/(4*A)+C))
    return massimi
    
    
    