import numpy as np
from numpy.lib.stride_tricks import as_strided
import pylab
from scipy.optimize import curve_fit
from scipy.stats import chisqprob

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
dir= path + "Esercitazione15/"



from BuzzLightyear import * 
from lab import *
import uncertainties
import uncertainties.unumpy
###########################################################################





close("all")
dir_grph=dir+"grafici/"
dir = dir + "data/"


file="lastfit.txt"
data = loadtxt(dir+file,unpack=True)
R=data[0]
VS=data[1:]
Vmedio=np.mean(VS, 0)
N=np.shape(VS)[0]
M=np.shape(VS)[1]
Vmediop=as_strided(Vmedio, (N, M), (Vmedio.strides[0],0))
VStd=np.sqrt(np.sum((VS-Vmedio)**2, 0)/(N-1))


foo=lambda R, V0, RT, RS: V0*np.sqrt(1+R/RT+(R/RS)**2)

pars, covs=curve_fit(foo, R, Vmedio, sigma=VStd/N)

pylab.errorbar(R, Vmedio, VStd/N, fmt=".")
domain=np.linspace(min(R), max(R), 1000)
pylab.plot(domain, foo(domain, *pars))

pylab.show()


