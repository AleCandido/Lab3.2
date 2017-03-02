from uncertainties import *
from scipy.integrate import quad

ids = [i for i in range(11,29)] + [30,32,33,35,37,39,41,44,45,46,48,50]

preprevacc = [299, 294, 288, 281, 273, 267, 258, 250, 243, 237, 230, 221, 216, 210, 204, 195, 188, 180, 239, 239, 192, 192, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252, 252]

prepreicoil = [1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.30, 1.28, 1.28, 1.35, 1.35, 1.40, 1.40, 1.46, 1.46, 1.52, 1.52, 1.61, 1.61, 1.71, 1.71, 1.81, 1.81, 1.90, 1.90]

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
    
def field(r, R, z0, I):
    r=np.abs(r)+epsilon
    A=(R**2+r**2+z0**2)
    fun=lambda teta: R*(R-r*np.cos(teta))/(A-2*R*r*np.cos(teta))**3/2
    return I*scipy.integrate.quad(fun,0 ,2*np.pi)[0] 
    
B = [ufloat(0,0) for i in range(0,len(icoil))]

for i in range(0,len(preicoil)):
    B[i] = ufloat(field(), )
    
em = [ufloat(0,0) for i in range(0,len(B))]

for i in range(0,len(preicoil)):
    em[i] = 2*vacc[i]/((B[i]*rtls[i])**2)
