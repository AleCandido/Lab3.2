from numpy import *
import math
import scipy.special
import scipy.optimize
from uncertainties import unumpy,umath,ufloat
import lab
import pylab
import scipy.stats

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
ord0H = ufloat(34+45/60,2/60) -  alpha0 #+0.7

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

figure(123)
plot(range(len(unumpy.nominal_values(lambdaH))), unumpy.nominal_values(1/lambdaH))
figure(0)



########plot della tabella...non mi convincono i numerini delle serie e dei valori iniziali...
def mycoso(self):
    a0, a1=Angle(self.n)
    b0, b1=Angle(self.s)
    return str(math.floor(np.round(a0)))+"\degree "+str(np.floor(a1))+"' \pm "+str(np.round(b1))+" '"

for i,j in enumerate(lambdaH):
    print(colori[i], "&  $", mycoso(ord1H[i]+360),"$  &  $",mycoso((180 - theta0H - ord1H)[i]-180),"$  &  $", int(ordine[i].n),"$ & $" ,lambdaH[i],"$ & $" ,attese[i],"$ & $", int(n1[i]) ,r"$ \\")


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
x=n2s[mask]
y=1/lambdaH[mask]
Y=unumpy.nominal_values(y)
dY=unumpy.std_devs(y)
fun=lambda x, R: R*(1/2**2-1/x**2)

pars, pcov=lab.curve_fit(fun, x, Y, sigma=dY, absolute_sigma=True)
RyS=ufloat(pars, pcov**0.5)
print(RyS*1e2)
print(sum((Y-fun(x, pars))**2/dY**2))

pylab.errorbar(x, Y, dY)

pylab.errorbar(x, fun(x, pars))



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

# ## fit per trovare costante di Rydberg
# #metto 1 come errore su n1 stimato prima perchè n è intero. bisogna stare attenti quando n = 1, perchè n non può essere 0, quindi in quel caso l'errore sarebbe asimmetrico
# # dn1 = ones(num)
# 
# 
# yy = unumpy.uarray(ones(num),zeros(num))
# x = ones(num)
# y = ones(num)
# dy = ones(num)
# dx = zeros(num)
# 
# for i in range (0,num):
#     x[i] = (1/pow(n1[i],2))-(1/pow(n2[i],2))
#     yy[i] = 1/lambdaH[i] 
#     y[i] = yy[i].nominal_value 
#     dy[i] = yy[i].std_dev
#     dx[i] = 2*dn1[i]*x[i]/n1[i]
# 
# #meglio non mettere errori sulle x..
# 
# # graphic to view data
# figure(1)
# # subplot(2,1,1)
# errorbar(x,y,dy,dx, linestyle = '' , color = 'black', marker = '.')
# rc('font',size=16)
# xlabel('$1/n_1^{2}-1/n_2^{2}$', labelpad = -7)
# ylabel('$1/\lambda [nm^{-1}$]')
# title('Misura della costante di Rydberg')
# # xlim(-0.2,5)
# # ylim(,)
# minorticks_on()
# grid()
# # legend()
# show()
# 
# 
# # definitions used in both fit:
# # define the linear function
# def func(x,a,b):
#     return a*x + b
#     
# # estimated values of the parameters
# inval=array([1,1])
# 
# A=inval[0]
# B=inval[1]
# a0=0.
# b0=0.
# while abs(A-a0)>10**(-5) and abs(B-b0)>10**(-5):
#     
#     # Override the step n-2
#     A=a0
#     B=b0
# 
# 
# 
#     
# #statistical error (dx not negligible, or use 'A' in the formula or calculate before 'a' and then insert and recalculate)
# sigma = sqrt(dy**2+(A*dx)**2)
# 
# "peso statistico"
# w = 1/sigma**2
# 
# #best-fit and chi square
# 'al posto di sigma va err a seconda dei casi'
# pars,covm = scipy.optimize.curve_fit(func,x,y,inval,sigma)
# # Calculate chi square with n DOF
# chi2 = ((w*(y-func(x,pars[0],pars[1]))**2)).sum()
# ndof = len(x)-len(inval)
# sigmachi2 = sqrt(2*ndof)
# 
# 
# # Results (linear correlation coefficient = normalized covariance)
# print('Risultati Best-fit Numerico:')
# print('a0 = ', pars[0], '+/-', sqrt(covm[0,0]))
# print('b0 = ', pars[1], '+/-', sqrt(covm[1,1]))
# print('norm_cov = ', covm[0,1]/(sqrt(covm[0,0]*covm[1,1])))
# print('chi2/ndof = %f/%d' %(chi2, ndof))
# print('sigmachi2 = %f' % sigmachi2)
# 
# 
# # prepare a dummy array and plot the fitting curve 
# xx=linspace(min(x),max(x),100)
# plot(xx,func(xx,pars[0],pars[1]), color='black')
# # savefig(’figure1.pdf’)
# show()

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

