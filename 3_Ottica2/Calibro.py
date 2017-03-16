from pylab import *
from lab import *
from uncertainties import *
from uncertainties import unumpy

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
dir= path + "3_Ottica2\\"

##

ys, dys = loadtxt(dir + "data\\Calibro.txt", unpack=True)

L = ufloat(210,0.1)
Ydirect = ufloat(10,0.05)

Yst = unumpy.uarray(ys,0.1)
Y0 = (Yst[0] + Ydirect)/2
Ys = Yst - Y0.n

tans = Ys/L
sins = unumpy.sin(pi/2 - unumpy.arctan(tans))

m = array([i for i in range(0, len(sins))])
par, cov = fit_linear(m, unumpy.nominal_values(sins), dy=unumpy.std_devs(sins))

n, q = correlated_values(par, cov)
chi2 = sum((unumpy.nominal_values(sins) - (n.nominal_value*m + q.nominal_value))**2/unumpy.std_devs(sins)**2)

lamda = - n * 0.1

errorbar(m,unumpy.nominal_values(sins), yerr=unumpy.std_devs(sins), fmt = 'r,')

x = linspace(0,max(m),1000)
y = n*x + q
plot(x,unumpy.nominal_values(y))

print(lamda, '\nchi2/ndof =', chi2, '/', len(sins)-2)


