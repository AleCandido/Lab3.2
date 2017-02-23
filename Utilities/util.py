import numpy as np
import lab
import uncertainties
from operator import *
import pylab
import math

__all__=["defoult_hwindow", "debug", "BetterFindLocalMaxs", "BetterFindLocalMins", "baseplot"]

defoult_hwindow=50
debug=1

baseplot=1000
plotnum=[0]



def findLocalLX(data, hwindow, f1, f2, f3):
    maxs=[]
    for i in range(hwindow, len(data)-hwindow):
        if(f2(data[i], f1(data[i-hwindow: i])) and f3(data[i],f1(data[i+1: i+hwindow+1]))):
           maxs.append(i)
    return maxs

def findLocalDX(data, hwindow, f1, f2, f3):
    maxs=[]
    for i in reversed(range(hwindow, len(data)-hwindow)):
        if(f3(data[i], f1(data[i-hwindow: i])) and f2(data[i],f1(data[i+1: i+hwindow+1]))):
           maxs.append(i)
    return maxs



def findLocal(data, hwindow, f1, f2, f3):
    lmaxs=findLocalLX(data, hwindow, f1, f2, f3)
    rmaxs=list(reversed(findLocalDX(data, hwindow, f1, f2, f3)))
    print(lmaxs)
    print(len(lmaxs))
    print(rmaxs)
    print(len(rmaxs))
    d={}
    for l in lmaxs:
        if(data[l] in d.keys()):
            d[data[l]].append(l)
        else:
            d[data[l]]=[l]
    for l in rmaxs:
        if(data[l] in d.keys()):
            d[data[l]].append(l)
        else:
            d[data[l]]=[l]
    ret=[]
    for l in d.keys():
        if(len(d[l])>1):
            ret.append(math.ceil((d[l][0]+d[l][1])/2))
    return ret



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
        try:
            domain=np.array(range(-hwindow, hwindow))
            par, covs = lab.curve_fit(p, domain, ydata[i-hwindow: i+hwindow], sigma=dydata[i-hwindow: i+hwindow])
            corpar=uncertainties.correlated_values(par, covs)
            A, B, C=corpar
            if(f2(A, 0)):
                print("Warning!!!")
            massimi.append((i,ydata[i], par, covs, -B/2*A, -B**2/(4*A)+C))
            if(debug>=2):
                print("start BetterFindLocal debug...")
                pylab.figure(baseplot+plotnum[0])
                plotnum[0]+=1
                pylab.plot(domain, ydata[i-hwindow: i+hwindow])
                pylab.plot(domain, p(domain, *par))
                pylab.show()
                print("...end BetterFindLocal debug")
        except Exception as e:
            print(e)
            massimi.append(e)
    if(debug>=1):
        pylab.figure(baseplot+plotnum[0])
        plotnum[0]+=1
        pylab.plot(range(len(ydata)), ydata)
        for i in massimi:
            domain=np.array(range(-hwindow, hwindow))
            idomain=np.array(range(-hwindow+i[0], hwindow+i[0]))
            pylab.plot(idomain,p(domain,*i[2]))
        pylab.show()
    return massimi


#be, così non ci si capisce più nulla no!!!
BetterFindLocalMaxs=(lambda x, y:lambda ydata, dydata, hwindow=defoult_hwindow: y(ydata, dydata, hwindow, x, ge))(findLocalMaxs, BetterFindLocal)
BetterFindLocalMins=(lambda x, y:lambda ydata, dydata, hwindow=defoult_hwindow: y(ydata, dydata, hwindow, x, le))(findLocalMins, BetterFindLocal)

