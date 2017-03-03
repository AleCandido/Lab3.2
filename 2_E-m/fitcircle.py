import numpy
from pylab import *
from scipy.optimize import curve_fit
import os
import lab
from uncertainties import *
import sys
import scipy.stats


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
rls = []
Nigmals = []
chi2ls = []

for id in ids:
    #per le notazioni guardare il file pdf 'circle fit'
    a,b = loadtxt(dir + 'data\\{}.txt'.format(id), unpack = True)
    
    # estraggo le righe pari
    a0 = array([a[i] for i in range(0,len(a),2)]) 
    b0 = array([b[i] for i in range(0,len(b),2)])
    
    # estraggo le righe dispari
    a1 = array([a[i] for i in range(1,len(a),2)]) 
    b1 = array([b[i] for i in range(1,len(b),2)])
    
    # compongo l'array dei punti (x1,x2,y1,y2)
    P = array([a0,a1,b0,b1])
    
    eerr = 5
    
    x = (P[0] + P[1])/2
    y = (P[2] + P[3])/2
    dx = abs((P[0] - P[1])/2)/eerr   #devo inserire un minimo --> se l'elemento è minore di una soglia applica la soglia
    dy = abs((P[2] - P[3])/2)/eerr
    
    mx = sum(x)/len(x)
    my = sum(y)/len(y)
    
    # dx = array([dx[i] for i in range(0,len(x)) if x[i]>mx])
    # dy = array([dy[i] for i in range(0,len(x)) if x[i]>mx])
    # y = array([y[i] for i in range(0,len(x)) if x[i]>mx])
    # x = array([e for e in x if e>mx])
    # mx = sum(x)/len(x)
    # my = sum(y)/len(y)
    
    u = x-mx
    v = y-my
    du = dx
    dv = dy
    
    ## fit analitico
    
    suu = sum(u**2)
    suv = sum(u*v)
    svv = sum(v**2)
    suuu = sum(u**3)
    suvv = sum(u*(v**2))
    suuv = sum(v*(u**2))
    svvv = sum(v**3)
    
    # risolvo sistema per trovare coordinate centro circonferenza
    det = suv**2 - suu*svv
    det1 = ((svvv+suuv)*suv - (suuu+suvv)*svv)/2
    det2 = ((suuu+suvv)*suv - (svvv+suuv)*suu)/2
    u0 = det1/det
    v0 = det2/det

    
    x0 = u0 + mx
    y0 = (v0 + my)
    r = sqrt((u0**2) + (v0**2) + (suu+svv)/len(x))
    
    ## calcolo degli errori
    
    # derivate preliminari
    du0du = (1/(2*det**2))*(((svvv + suuv)*v + 2*u*v*suv - (3*u**2 + v**2)*svv)*det - (2*suv*v - 2*svv*u)*2*det1)
    dv0dv = (1/(2*det**2))*(((suuu + suvv)*u + (2*v*u)*suv - (3*v**2 + u**2)*suu)*det - (2*suv*u - 2*suu*v)*2*det2)
    
    du0dv = (1/(2*det**2))*(((svvv + suuv)*u + (3*v**2 + u**2)*suv - (suuu + suvv)*2*v**2 - 2*u*v*svv)*det - (2*suv*u - 2*suu*v)*2*det1)
    dv0du = (1/(2*det**2))*(((suuu + suvv)*v + (3*u**2 + v**2)*suv - (svvv + suuv)*2*u**2 - 2*v*u*suu)*det - (2*suv*v - 2*svv*u)*2*det2)
    
    drdu = (u0*du0du + v0*dv0du + u/len(x))/r
    drdv = (u0*du0dv + v0*dv0dv + v/len(x))/r
    
    # matrice di covarianza
    
    sigmau2 = sum((du0du**2)*(du**2) + (du0dv**2)*(dv**2))
    sigmav2 = sum((dv0du**2)*(du**2) + (dv0dv**2)*(dv**2))
    sigmar2 = sum((drdu**2)*(du**2) + (drdv**2)*(dv**2))
    
    sigmauv = sum((du0du*dv0du)*(du**2) + (du0dv*dv0dv)*(dv**2))
    sigmaur = sum((du0du*drdu)*(du**2) + (du0dv*drdv)*(dv**2))
    sigmavr = sum((dv0du*drdu)*(du**2) + (dv0dv*drdv)*(dv**2))
    
    Sigma = array([ [sigmau2, sigmauv, sigmaur], [sigmauv, sigmav2, sigmavr], [sigmaur, sigmavr, sigmar2]])
    Nigma = zeros((3,3))
    
    for i in (0,1,2):
        for j in (0,1,2):
            Nigma[i,j] = Sigma[i,j] / sqrt(Sigma[i,i]*Sigma[j,j])
    
    # print(Nigma)
    
    Nigmals = Nigmals + [Nigma]
    
    ## calcolo del chi2
    
    # geometria preliminare
    
    i1 = [x0 + r*(x - x0)/sqrt((y - y0)**2 + (x - x0)**2), y0 + r*(y -y0)/sqrt((y - y0)**2 + (x - x0)**2)]
    i2 = [x0 - r*(x - x0)/sqrt((y - y0)**2 + (x - x0)**2), y0 - r*(y -y0)/sqrt((y - y0)**2 + (x - x0)**2)]
    
    #plot(i1[0],i1[1], 'go')
    #plot(i2[0],i2[1], 'ro')
    
    d1 = sqrt((x - i1[0])**2 + (y -i1[1])**2)
    d2 = sqrt((x - i2[0])**2 + (y -i2[1])**2)
    d = minimum(d1,d2)
    
    # chi2
    
    chi2 = sum(d**2/(dx**2 + dy**2))
    # print('chi2 =', chi2/len(x))
    chi2ls = chi2ls + [chi2/len(x)]
    
    # figure(id)
    
    grid()
    xlabel('x')
    ylabel('y')
    # errorbar(x,y,dy,dx, marker= ',' , linestyle = 'None' , )
    
    # print('x0 =', x0)
    # print('y0 =', y0)
    # plot(x0,y0, marker = 'o')
    # print('r  =', r, '+/-', sqrt(sigmar2)/r*100, '%\n')
    
    rls = rls + [ufloat(r, sqrt(sigmar2))]
    
    x1 = numpy.linspace(x0 - r + 1/10**10, x0 + r - 1/10**10, 1000)
    y1 = numpy.sqrt(r**2-(x1-x0)**2) + y0
    
    xlim(0,max(x1)*1.2)
    ylim(0,max(y1)*1.2)
    # plot(x1,y1, color = 'black')
    
    x2 = numpy.linspace(x0 - r + 1/10**10, x0 + r -1/10**10, 1000)
    y2 = - numpy.sqrt(r**2-(x2-x0)**2) + y0
    # plot(x2,y2, color = 'black')
    
    # savefig(dir+"grafici\\"+str(id)+".pdf")