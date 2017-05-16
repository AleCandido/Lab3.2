#amplificazioni, appena possibile diventano con errore


#V_out=AV1-BV2

from lab import *
import uncertainties
import numpy as np
import pylab
import sys

import getpass
users={"candi": "C:\\Users\\candi\\Documents\\GitHub\\Lab3.2\\",
"silvanamorreale":"C:\\Users\\silvanamorreale\\Documents\\GitHub\\Lab3.2\\" ,
"Studenti": "C:\\Users\\Studenti\\Desktop\\Lab3\\",
"User":"C:\\Users\\User\\Documents\\GitHub\\Lab3.2\\",
"andrea": "/home/andrea/Documenti/Da salvare 12-5-2017/Documenti/GitHub/Lab3.2/"
}
try:
    user=getpass.getuser()
    path=users[user]
    print("buongiorno ", user, "!!!")
except:
    raise Error("unknown user, please specify it and the path in the file Esercitazione*.py")


sys.path = sys.path + [path]
dir= path + "Esercitazione14/"
graph_dir=dir+"grafici/"

pylab.close("all")

def mymme(val,*args, **kwargs):
    return uncertainties.ufloat(val,mme(val, *args, **kwargs))


R23 = mymme(33.3e3, "ohm")
R26 =mymme(33.0e3, "ohm")          
R22 = mymme(38.4e3, "ohm") 
R24 = mymme(39.1e3, "ohm")

A=(R24)/(R23)*(R23+R22)/(R26+R24)
B=R22/R23

print(A, B)

AMC=(A-B)/2
AD=(A+B)/2

print(AMC, AD)



R18=mymme(3.28e6,"ohm")
R20=mymme(1.232e6,"ohm")
R21=mymme(1.521e6,"ohm")
C6=mymme(221e-9, "farad")

domain=np.logspace(-4, 4, 1000)

C6 = 45.6e-9 
R20 = 1.232e6
R18 = 3.28e6 
R21 = 1.521e6
C5=221e-9


def Z(w):
    def C(C):
        return -complex(0, 1)/(C*w)
    
    
    def par(a, b):
        return a*b/(a+b)
    
    return par(R21, R20+C(C6))/(1+C(C6)/R20)

def A(w):
    def C(C):
        return -complex(0, 1)/(C*w)
    
    
    def par(a, b):
        return a*b/(a+b)
    
    return C(C6)/R20*par(Z(w), C(C5))/(R21+par(Z(w), C(C5)))
    

def mod(w, f):
    x=f(w)
    return np.sqrt(np.real(x)**2+np.imag(x)**2)

def phase(w, f):
    x=f(w)
    return np.arctan2(np.imag(x), np.real(x))
    


pylab.figure(1)
pylab.title("Plot di Bode del mediatore")

pylab.subplot(311)
pylab.xlabel("frequenza [Hz]")
pylab.ylabel("$A(w)$")
pylab.loglog()
pylab.plot(domain, mod(2*np.pi*domain, A)) #il plot è con la frequenza, mentre le funzioni vogliono omega


pylab.subplot(312)
pylab.xlabel("frequenza [Hz]")
pylab.semilogx()
pylab.ylabel("$\phi (\omega)$")
pylab.plot(domain, phase(2*np.pi*domain, A)) #il plot è con la frequenza, mentre le funzioni vogliono omega


pylab.subplot(313)
pylab.loglog()

pylab.xlabel("frequenza")
pylab.ylabel("$Z(\omega)$[Ohm]")
pylab.plot(domain, mod(2*np.pi*domain, Z))

pylab.savefig(graph_dir+"mediatorefr.pdf")
pylab.show()

