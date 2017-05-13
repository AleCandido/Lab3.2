from pylab import *
from scipy.optimize import curve_fit
from scipy.stats import chisqprob

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
dir= path + "Esercitazione14/"

from BuzzLightyear import * 
from lab import *
import uncertainties
###########################################################################


file = "Mylar.txt"
dir = dir + "data/"

y, x = loadtxt(dir+file,unpack=True)
dy = mme(y,"volt",sqerr=True)
dy = sqrt(dy**2 + (0.02/sqrt(2))**2)

f = lambda x,a,b: a*exp(-x/b)
p0 = [1,1]

par, cov = curve_fit(f,x,y,p0=p0,sigma=dy)

errorbar(x,y,yerr=dy,fmt=".")

xfit = linspace(min(x),max(x),1000)
yfit = f(xfit, *par)
plot(xfit,yfit)

chi2 = sum((y-f(x,*par))**2/dy**2)
ndof = len(x) - 2
prob = chisqprob(chi2,ndof)
print(chi2,ndof,"\n",prob,"\n")

show()

print(par,"\n",cov)

###########################################################################
