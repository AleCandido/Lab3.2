import sys
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
"andrea": "/home/andrea/Documenti/Da salvare 12-5-2017/Documenti/GitHub/Lab3.2/",
"viviana": "C:\\Users\\viviana\\Documents\\GitHub\\Lab3.2\\"
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


print("===============Fit finale=================")



#####stima paramretri....

kbT=1.38e-23*300*4
Df=1e3
v_rum=11e-9 #volt*hertz**0.5
r_rum=v_rum**2/(4*kbT*Df)

i_rum=0.4e-12
r_rum_par=v_rum/i_rum

#####stimati dal datasheet dell'ina...


pylab.figure(figsnum)
figsnum+=1

dir_grph=dir+"grafici/"
dir = dir + "data/"

####Caricamento dati

file="lastfit1.txt"
data = np.loadtxt(dir+file,unpack=True)
R=data[0]
VS=data[1:]*1e-3
Vmedio=np.mean(VS, 0)
N=np.shape(VS)[0]
M=np.shape(VS)[1]
Vmediop=as_strided(Vmedio, (N, M), (Vmedio.strides[0],0))
VStd=np.sqrt(np.sum((VS-Vmedio)**2, 0)/(N-1))

Vmedio=Vmedio[R<20000]
VStd=VStd[R<20000]
R=R[R<20000]
DR=mme(R, "ohm")

#####Fit...

foo=lambda R, V0, RT, RS: V0*np.sqrt(1+R/RT+(R/RS)**2)
p0=(2, r_rum, r_rum_par) 
pars, covs=curve_fit(foo, R, Vmedio, sigma=VStd)
V0, RT, RS=uncertainties.correlated_values(pars, covs)
print("risutati: {} {} {}".format(V0, RT, RS))


#####Fit errori x...

dfoo=lambda R, V0, RT, RS: 0.5*V0*(1/RT+ 2*R/RS**2)/np.sqrt(1+R/RT+(R/RS)**2)
p0=(2, r_rum, r_rum_par) 
pars, covs=lab.fit_generic_xyerr(foo, dfoo, R, Vmedio, DR,VStd)
V0, RT, RS=uncertainties.correlated_values(pars, covs)
print("risutati: {} {} {}".format(V0, RT, RS))





######plot....

pylab.title("Misura della costante di Boltzmann")
pylab.xlabel("R[$\Omega$]")
pylab.ylabel("RMS[V]")
pylab.errorbar(R, Vmedio, VStd, DR,fmt=".")
domain=np.linspace(min(R), max(R), 1000)
pylab.plot(domain, foo(domain,*pars))
pylab.savefig(dir_grph+"lastfit.pdf")

######chiq
chisq=np.sum((Vmedio-foo(R, *pars))**2/(VStd)**2) #versione senza errori sulle x
chisq=np.sum((Vmedio-foo(R, *pars))**2/((VStd)**2+dfoo(R, *pars)**2*DR**2)) #versione con errori sulle x, in pratica non cambia nulla..
prob=chisqprob(chisq,dof)
# chisq1=np.sum((Vmedio-foo(R, *pars))**2/(VStd/N)**2) #versione senza erroris sulle x
# chisq1=np.sum((Vmedio-foo(R, *pars))**2/((VStd/N)**2+DR**2*dfoo(R, *pars)**2)) #versione con errori sulle x, quì cambia parecchio!!!!

chisq1=np.sum((Vmedio-foo(R, *pars))**2/(VStd/sqrt(N))**2) #versione senza erroris sulle x
chisq1=np.sum((Vmedio-foo(R, *pars))**2/((VStd/sqrt(N))**2+DR**2*dfoo(R, *pars)**2)) #versione con errori sulle x, quì cambia parecchio!!!!


print("Gi errori dovrebbero essere quelli sulla media, non quelli delle parent dei dati, quindi il chiq corretto dovrebbe essere il secondo, non il primo. Di fatto il primo torna, il secondo no: qualcuno ha idea del perché il primo portrebbe essere meglio del sencodo?")
print("chisq={} prob={} chiq2/dof={}/{}".format(chisq, prob,chisq1,len(R)-3))

##########stima k_b
print("#####risultati con il prodotto dei guadagni...")



Atot=A1*A2*A3*A4
print("Atot={}".format(Atot))
print("A1={} A2={} A3={} A4={}".format(A1, A2, A3, A4))

Df=np.pi*Dw/2 #larghezza equivalente  
print("Df={}".format(Df))

# Df = Dw

T=uncertainties.ufloat(273+28, 5)
k_b=V0**2/(4*T*Atot**2*Df*RT) 
print("K_b={} vs K_b_exp=1.380e-23".format(k_b))

print('########risultati con il guadagno totale stimato con il partitore 1000:1...')

Atot=A_supp*A4
print("Atot={}".format(Atot))


Df=np.pi*Dw_supp/2
print("Df={}".format(Df))

T=uncertainties.ufloat(273+28, 5)
k_b=V0**2/(4*T*Atot**2*Df*RT) #Df_true è concettualmente più giusto...ma risulta essere più sbagliato...se si voule essere più onesti sostituire Df--->Df_true...
print("K_b={} vs K_b_exp=1.380e-23".format(k_b))


############piccola analisi....

print("rapporto A0=", A1*A2*A3*A4/Atot)
print(Dw/Dw_supp)
print("rapporto K=", (A1*A2*A3*A4/Atot)**2*Dw/Dw_supp)
#fit non torna manco per nulla...domani prendo delle misure sere...
