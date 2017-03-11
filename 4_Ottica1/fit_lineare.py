import pylab
import scipy.optimize
import numpy
import scipy.special
import math

# bisogna sicuramente cambiare i nomi e gli indirizzi quaggiù
# definisco gli utenti abilitati a maneggiare il programma e il percorso in cui andranno a finire gli elaborati

# import getpass
# users={"alessandro": "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/",
# "silvanamorreale":"C:\\Users\\silvanamorreale\\Documents\\GitHub\\Lab3.2\\" ,
# "Studenti": "C:\\Users\\Studenti\\Desktop\\Lab3\\",
# "User":"C:\\Users\\User\\Documents\\GitHub\\Lab3.2\\"
# }
# try:
#     user=getpass.getuser()
#     path=users[user]
#     print("buongiono ", user, "!!!")
# except:
#     raise Error("unknown user, please specify it and the path in the file Esercitazione*.py")
# 
# 
# sys.path = sys.path + [path]
# dir= path + "dati"

# load data
# x,dx,y,dy = pylab.loadtxt('C:\\Users\\User\\Desktop\\datifit\\data06.txt', unpack = True)
verde=60+1/60*sum([0, 0, 0])/3
rosso=58+1/60*sum([43, 41, 44])/3
azzurro=60+1/60*sum([29, 26, 28])/3
blu=60+1/60*sum([39, 40, 41])/3
viola= 61+1/60*sum([15,16,11])/3
alpha0 = (10+1/60*sum([52,55,54])/3)
y = numpy.array([1/508.6,1/643.8,1/480.0,1/467.8])

x = numpy.array([verde,rosso,azzurro,blu])- alpha0*numpy.ones(4)

dx=0.00000001
dy=0.00000001


giallaS= 59+1/60*sum([10,6,6])/3 - alpha0
print(giallaS)

# graphic to view data
pylab.figure(1)
# pylab.subplot(2,1,1)
pylab.errorbar(x,y,dy,dx, linestyle = '' , color = 'black', marker = '.')
pylab.rc('font',size=16)
pylab.xlabel('', labelpad = -7)
pylab.ylabel('')
pylab.title('')
# pylab.xlim(-0.2,5)
# pylab.ylim(,)
pylab.minorticks_on()
pylab.grid()
pylab.legend()
pylab.show()






'''



# definitions used in both fit:
# define the linear function
def func(x,a,b):
    return a+b*x



## Numerical Best-fit (in this case linear, but of course it can also be extended to cases not linear)

# estimated values of the parameters
inval=numpy.array([0,2])

A=inval[0]
B=inval[1]
a0=0.
b0=0.
while abs(A-a0)>10**(-5) and abs(B-b0)>10**(-5):
    
    # Override the step n-2
    A=a0
    B=b0

# error (neglect dx)
sigma = dy

#strumental error (dx not negligible, or use 'A' in the formula or calculate before 'a' and then insert and recalculate)
# sigma = numpy.sqrt(dy+abs(A)*dx)
    
#statistical error (dx not negligible, or use 'A' in the formula or calculate before 'a' and then insert and recalculate)
# sigma = numpy.sqrt(dy**2+(A*dx)**2)

"peso statistico"
w = 1/sigma**2

#best-fit and chi square
'al posto di sigma va err a seconda dei casi'
pars,covm = scipy.optimize.curve_fit(func,x,y,inval,sigma)
# Calculate chi square with n DOF
chi2 = ((w*(y-func(x,pars[0],pars[1]))**2)).sum()
ndof = len(x)-len(inval)
sigmachi2 = numpy.sqrt(2*ndof)
# significance level
# liv_sign = scipy.special.chdtrc(ndof, chi2)

# Results (linear correlation coefficient = normalized covariance)
print('Risultati Best-fit Numerico:')
print('a0 = ', pars[0], '+/-', numpy.sqrt(covm[0,0]))
print('b0 = ', pars[1], '+/-', numpy.sqrt(covm[1,1]))
print('norm_cov = ', covm[0,1]/(numpy.sqrt(covm[0,0]*covm[1,1])))
print('chi2/ndof = %f/%d' %(chi2, ndof))
print('sigmachi2 = %f' % sigmachi2)
# print('liv_sign = %f' %p)


# prepare a dummy array and plot the fitting curve 
xx=numpy.linspace(min(x),max(x),100)
pylab.plot(xx,func(xx,pars[0],pars[1]), color='black')
# pylab.savefig(’figure1.pdf’)
pylab.show()

## Residue

#define the array of residue
r = (y-func(x,pars[0],pars[1]))/sigma

pylab.figure(2)
# pylab.subplot(2,1,2)
pylab.rc('font',size=18)
pylab.xlabel('')
pylab.ylabel('Norm. res')
pylab.title('')
# pylab.xlim(,)
pylab.ylim(-0.9,0.9)
pylab.minorticks_on()
pylab.grid()
pylab.legend()
pylab.plot(x,r,linestyle="--",color='black',marker='.')
# pylab.savefig('figure2.pdf')
pylab.show()
'''