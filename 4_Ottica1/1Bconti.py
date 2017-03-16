from numpy import *
import math
import scipy.special
import scipy.optimize
from uncertainties import unumpy,umath,ufloat
import lab
import pylab
import scipy.stats
import sys
import numpy as np



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









## passo reticolare, misura con Hg

# zero del nonio
zero = unumpy.uarray(348*ones(3)+array([40,41,45])/60,ones(3)/60)
alpha0 = (zero[0]+zero[1]+zero[2])/3

#lunghezza d'onda nominale Hg
lambd = 546.074

# riga ordine 0
ord0 = unumpy.uarray(8*ones(3)+array([56,55,56])/60,ones(3)/60)
ord0Hg = (ord0[0]+ord0[1]+ord0[2])/3 - alpha0


theta0Hg = (0.5*(180 - ord0Hg))


ord1 = unumpy.uarray(69*ones(3)+array([30,28,30])/60,ones(3)/60)
ord1Hg = (ord1[0]+ord1[1]+ord1[2])/3 - alpha0

#riga ordine 1
thetavHg = (180 - theta0Hg - ord1Hg)

#passo reticolare (E QUESTO TORNA..)
d = lambd/(umath.sin(thetavHg*math.pi/180)-umath.sin(theta0Hg*math.pi/180))
print(d,"\n",(10**6)/d)

## misura lunghezze d'onda righe di H
#coppie n1 n2
num = 7


#costante di ry nominale
Ryexp = 1.097373156 * 10**(-2)  #in nm*-1

#alpha0+=360

# ricalcolo riga ordine 0 per H perchè si è spostato il reticolo.
ord0H = ufloat(34+35/60,2/60) -  alpha0 #+0.7

theta0H = 0.5*(180 - ord0H)

# righe ordine 1 e 2
ord1H = unumpy.uarray([  array([81+49/60,93+58.5/60,115+55/60,71+49/60,85,91+11/60,108]),array([4,4,4,2,3,2,3])/60])-alpha0

# ordine della riga
ordine = unumpy.uarray(array([1,1,2,1,1,1,2]),zeros(7))

#argomenti del seno nella formula
arg1 = theta0H*ones(7)*math.pi/180

arg2 = (180 - theta0H - ord1H)*math.pi/180

#calcolo della lunghezza d'onda OTTENGO COSE SENSATE SE IN ARG2 CI METTO THETA0HG AL POSTO DI THETA0H

lambdaH = unumpy.uarray(ones(7),zeros(7))


for i in range(0,7):
    lambdaH[i] = (d*(umath.sin(arg2[i])-umath.sin(arg1[i])))/ordine[i]


print(lambdaH)

colori=["azzurro", "rosso", "azzurro", "d-viola", "d-verde","rosso", "viola"]
attese=[0, 0, 0, 0, 0, 0, 0]

pylab.figure(123)
pylab.plot(range(len(unumpy.nominal_values(lambdaH))), unumpy.nominal_values(1/lambdaH))
pylab.figure(0)



########plot della tabella...non mi convincono i numerini delle serie e dei valori iniziali...
def mycoso(self):
    a0, a1=Angle(self.n)
    b0, b1=Angle(self.s)
    return str(math.floor(np.round(a0)))+"\degree "+str(np.floor(a1))+"' \pm "+str(np.round(b1))+" '"

# for i,j in enumerate(lambdaH):
#     print(colori[i], "&  $", mycoso(ord1H[i]+360),"$  &  $",mycoso((180 - theta0H - ord1H)[i]-180),"$  &  $", int(ordine[i].n),"$ & $" ,lambdaH[i],"$ & $" ,attese[i],"$ & $", int(n1[i]) ,r"$ \\")


######mia stima numeri quantici...


n1s=np.array([2, 2, 2, 2, 2, 2, 2]) #giuste 0, 1, 2...
n2s=np.array([4, 3, 4, 6, 5, 3, 5])
stimata=1/(Ryexp*(1/n1s**2-1/n2s**2))


print("matching...")
for i, j in enumerate(stimata-lambdaH):
    print(i, ":", j)    


print("linee...")
for c,x, y in zip(colori, stimata, lambdaH):
    print(c,"    ",x, "     ", y)



mask=[True, True ,True, False, False, False,True]
x=np.array([n for i,n in enumerate(n2s) if mask[i]])
y=np.array([1/l for i,l in enumerate(lambdaH) if mask[i]])
Y=unumpy.nominal_values(y)
dY=unumpy.std_devs(y)
fun=lambda x, R: R*(1/2**2-1/x**2)

pars, pcov=lab.curve_fit(fun, x, Y, sigma=dY, absolute_sigma=True)
RyS=ufloat(pars, pcov**0.5)
print(RyS*1e2)
print(sum((Y-fun(x, pars))**2/dY**2))

pylab.title("Fit $n_2$ vs $1/\lambda$")
pylab.xlabel("$n_2$")
pylab.ylabel("$1/\lambda$ [$nm^{-1}$]")
pylab.xlim(2, 6)
pylab.ylim(min(Y)-(max(Y)-min(Y))/3,max(Y)+(max(Y)-min(Y))/3 )
pylab.errorbar(x, Y, dY, fmt=".", color="r")

pylab.plot(x, fun(x, pars), ".", color="b")
#pylab.plot(x, fun(x,0.0109))
pylab.savefig(dir+"grafici\\Ryf.pdf")


print("....", x)

#lambdaH=lambdaH[mask]
#ord1H=ord1H[mask]
attese=1/(Ryexp*(1/4-1/n2s**2))
#n1=n1[mask]
#attese=attese[mask]

def mycoso(self):
    a0, a1=Angle(self.n)
    b0, b1=Angle(self.s)
    return str(math.floor(np.round(a0)))+"\degree "+str(np.floor(a1))+"' \pm "+str(np.round(b1))+" '"

def mucoso(self):
    return str(self.n)+" \pm "+ str(self.s)


for i,j in enumerate(lambdaH):
    if(mask[i]):
        print(colori[i], "&  $", mycoso(ord1H[i]+360),"$  &  $",mycoso((180 - theta0H - ord1H)[i]-180),"$  &  $", int(ordine[i].n),"$ & $" ,lambdaH[i],"$ & $" ,attese[i],"$ & $", int(n2s[i]) ,r"$ \\")



## Residue

# #define the array of residue
# r = (y-func(x,pars[0],pars[1]))/sigma
# 
# figure(2)
# # subplot(2,1,2)
# rc('font',size=18)
# xlabel('$1/n_1^{2}-1/n_2^{2}$')
# ylabel('Norm. res')
# title('Residui Normalizzati')
# # xlim(,)
# # ylim(-0.9,0.9)
# minorticks_on()
# grid()
# # legend()
# plot(x,r,linestyle="--",color='black',marker='.')
# # savefig('figure2.pdf')
# show()

## Lunghezza d'onda doppietto Sodio


# righe ordine 1 e 2
ordS = unumpy.uarray([ array([89+18/60,89+21/60]),array([2,2])/60])-alpha0

# ordine della riga
ordineS = unumpy.uarray(array([1,1]),zeros(2))

#argomenti del seno nella formula
arg11 = theta0H*ones(2)*math.pi/180

arg22 = (180 - theta0H - ordS)*math.pi/180


lambdaS = unumpy.uarray(ones(2),zeros(2))


for i in range(0,2):
    lambdaS[i] = (d*(umath.sin(arg22[i])-umath.sin(arg11[i])))/ordineS[i]

print(lambdaS)

print(lambdaS[1]-lambdaS[0])
lambdaSexp=np.array([589.0, 589.6])

for i,j in enumerate(lambdaS):
    if(mask[i]):
        print("$", mycoso(ordineS[i]+360),"$  &  $",mycoso((180 - theta0H - ordS)[i]-180), "$ & $" ,lambdaS[i],"$ & $", lambdaSexp[i], "r$ \\")
