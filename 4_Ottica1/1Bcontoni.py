from numpy import *
import math
import scipy.special
import scipy.optimize
from uncertainties import unumpy,umath,ufloat
import lab
import pylab
import scipy.stats
import uncertainties
#fitto anche l'origine

Ryexp = 1.097373156 * 10**(-2)  #in nm*-1
mask=[True, True ,True, False, False, False,True]
ord1H = unumpy.uarray([array([81+49/60,93+58.5/60,115+55/60,71+49/60,85 , 91+11/60,108]),array([4,4,4,2,3,2,3])/60])-alpha0
ordine = unumpy.uarray(array([1,1,2,1,1,1,2]),zeros(7))
n1s=np.array([2, 2, 2, 2, 2, 2, 2])
n2s=np.array([4, 3, 4, 6, 5, 3, 5])

def fun(i,ord0H ,R):    
    theta0H = 0.5*(180 - ord0H)    
    arg1 = theta0H*ones(7)*math.pi/180    
    arg2 = (180 - theta0H - ord1H[i])*math.pi/180
    lambdaH = (d*(umath.sin(arg2)-umath.sin(arg1)))/ordine[i]
    x=n2s[i]
    y=1/lambdaH
    Y=unumpy.nominal_values(y)
    dY=unumpy.std_devs(y)
    return R*(1/2**2-1/n2s[i]**2)   
    
pars, pcov=lab.curve_fit(fun, [0, 1, 2, 6], ord1H, p0=(ufloat(34+45/60,2/60) -  alpha0, Ryexp), sigma=dY, absolute_sigma=True)
ord0H, RyS=uncertainties.correlated_values(pars, pcov)
print(RyS*1e2)
print(sum((Y-fun(x, pars))**2/dY**2))    
pylab.errorbar(x, Y, dY)    
pylab.errorbar(x, fun(x, pars))