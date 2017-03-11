from lab import *
from pylab import *
from uncertainties import *
from uncertainties import unumpy
from statistics import *
from scipy.constants import *

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
dir= path + "4_Ottica1\\"

##

alphar = loadtxt(dir + "data\\cadmio.txt", unpack=True)

alphas = alphar[0] + alphar[1]/60

alpha = []
dalpha = []

for i in range(0, len(alphas), 3):
    alpha += [mean(alphas[i:i+3])]
    err = stdev(alphas[i:i+3])
    if err != 0:
        dalpha += [err]
    else:
        dalpha += [1.5/60]

alphal = unumpy.uarray(alpha,dalpha)

alpha0 = ufloat(10.895, 0.026)
alphai = alphal - alpha0

lamda = array([467.8, 480.0, 508.6, 643.8])*10**(-9)
E = (h/physical_constants['electron volt'][0])*c/lamda

errorbar(unumpy.nominal_values(alphai), E, xerr = unumpy.std_devs(alphai), fmt = 'b,')

par, cov = fit_linear(E, unumpy.nominal_values(alphai), dy = unumpy.std_devs(alphai))

m, q = par

x = linspace(min(E)*0.99, max(E)*1.01)
y = m*x + q

xlim(min(y)*0.998, max(y)*1.002)
xlabel("Deflection angles [°]")
ylabel("Light energies [eV]")

plot(y, x, 'g')

savefig(dir + "grafici\\calcadmio.pdf")
