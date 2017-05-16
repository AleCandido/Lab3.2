from pylab import *
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
dir= path + "Esercitazione14/"

from BuzzLightyear import * 
from lab import *
import uncertainties
import uncertainties.unumpy
###########################################################################

close("all")
dir_grph=dir+"grafici/"
dir = dir + "data/"

#y1=[[],[],[]]

YS=[]
XS=[]
Bs=[]
ErrBs=[]

# for i in range(1, 4):
#     print("=====run{}======".format(i))
#     file = "Mylar{}.txt".format(i)
#     
#     
#     
#     y, x = loadtxt(dir+file,unpack=True)
#     
#     dy = mme(y,"volt",sqerr=True)
#     dy = sqrt(dy**2 + (0.02/sqrt(2))**2)
#     
#     Y=uncertainties.unumpy.uarray(y, dy)
#     X=x
#     YS.append(Y)
#     XS.append(X)
#     
#     
#     
#     f = lambda x,a,b: a*exp(-x/b)
#     p0 = [1,1]
#     
#     par, cov = curve_fit(f,x,y,p0=p0,sigma=dy)
#     
#     figure(i)
#     
#     errorbar(x,y,yerr=dy,fmt=".")
#     
#     xfit = linspace(min(x),max(x),1000)
#     yfit = f(xfit, *par)
#     plot(xfit,yfit)
#     
#     chi2 = sum((y-f(x,*par))**2/dy**2)
#     ndof = len(x) - 2
#     prob = chisqprob(chi2,ndof)
#     print(chi2,ndof,"\n",prob,"\n")
#     
#     
#     figure(10+i)
#     plot(x, (y-f(x,*par))/dy)
#     #show()
#     
#     print(par,"\n",cov)



print("======================CON A ==============")

for i in range(1, 4):
    print("=====run{}======".format(i))
    file = "Mylar{}.txt".format(i)
    
    y, x = loadtxt(dir+file,unpack=True)
    dy = mme(y,"volt",sqerr=True)
    dy = sqrt(dy**2 + (0.02/sqrt(2))**2)
    
    Y=uncertainties.unumpy.uarray(y, dy)
    X=x
    YS.append(Y)
    XS.append(X)
    
    
    
    f = lambda x,a,b,c: a*exp(-x/b)+c
    p0 = [1,1,0]
    
    par, cov = curve_fit(f,x,y,p0=p0,sigma=dy)
    
    figure(i)
    subplot(211)
    title("V(N) Run{}".format(i))
    xlabel("N lastre")
    ylabel("V [Volt]")
    
    
    errorbar(x,y,yerr=dy,fmt=".")
    
    xfit = linspace(min(x),max(x),1000)
    yfit = f(xfit, *par)
    plot(xfit,yfit)
    
    chi2 = sum((y-f(x,*par))**2/dy**2)
    ndof = len(x) - 3
    prob = chisqprob(chi2,ndof)
    print(chi2,ndof,"\n",prob,"\n")
    
    
    subplot(212)
    xlabel("N lastre")
    ylabel("Scati normalizzati [Volt]")
    plot(x, (y-f(x,*par))/dy)
    #show()
    savefig(dir_grph+"fit{}.pdf".format(i))
    print(par,"\n",cov)
    print([cov[j,j]**0.5 for j in range(3)])
    
    Bs.append(par[1])
    ErrBs.append(cov[1, 1]**0.5)

for i in range(max(len(XS[0]), len(XS[1]), len(XS[2]))):
    top=[i, "None", "None", "None"]
    for j in range(3):
        try:
            top[j+1]=YS[j][i]
        except Exception as e:
            pass
            #print(e)
    print("{} & {} & {} & {}\\\\".format(*top))




show()


final_result=lab.fit_const_yerr(Bs,ErrBs)
print(final_result[0], final_result[1]**0.5)

###########################################################################


