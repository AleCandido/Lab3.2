from pylab import *

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
dir= path + "Esercitazione11/"

from BuzzLightyear import * 
from uncertainties import *
###########################################################################

from Oscillografo import *

A = OscilloscopeData(dir + "data\\monostabile.csv")
VC = OscilloscopeData(dir + "data\\monostabileVC.csv")


figure(1)

plot(A.T1, A.CH1, ",-", label="input1")
plot(A.T2, A.CH2, ",--", label="input2")
ylim(-1,5)
# ax.set_yticklabels([])
# ax.set_xticklabels([])
# legend(loc=6)
grid()

figure(2)
# marker = ".", linestyle = "",
plot(VC.T1, VC.CH1, marker = ".", linestyle = "", label="input1")
plot(VC.T2, VC.CH2, ",--", label="input2")

# ax.set_yticklabels([])
# ax.set_xticklabels([])
# legend(loc=6)
grid()

show()


a = int(len(VC.T1)/3)

min1 = VC.CH1[0]
dmin1 = VC.dCH1[0]
min2 = VC.CH1[0]
dmin2 = VC.dCH1[0]
min3 = VC.CH1[0]
dmin3 = VC.dCH1[0]


for i in range(0,a):
    if (VC.CH1[i] < min1)  and (VC.CH1[i] != -1.12) :
        min1 = VC.CH1[i]
        dmin1 = VC.dCH1[i]
    if (VC.CH1[a+i] < min2) and (VC.CH1[a+i] != -1.04) :
        min2 = VC.CH1[a+i]
        dmin2 = VC.dCH1[a+i]
    if (VC.CH1[2*a+i] < min3):
        min3 = VC.CH1[2*a+i]
        dmin3 = VC.dCH1[2*a+i]
        
print(min1,min2,min3)
print(dmin1,dmin2,dmin3)
MIN = (min1+min2+min3)/3
dMIN = sqrt( ((min1-MIN)**2 + (min2-MIN)**2 + (min3-MIN)**2)/2)
print(MIN,dMIN,"\n\n")


max1 = VC.CH1[0]
dmax1 = VC.dCH1[0]
max2 = VC.CH1[0]
dmax2 = VC.dCH1[0]
max3 = VC.CH1[0]
dmax3 = VC.dCH1[0]
tmax1 = 0
tmax2 = 0
tmax3 = 0

for i in range(0,a):
    if (VC.CH1[i] > max1):
        max1 = VC.CH1[i]
        dmax1 = VC.dCH1[i]
        tmax1 = VC.T1[i]
    if (VC.CH1[a+i] > max2):
        max2 = VC.CH1[a+i]
        dmax2 = VC.dCH1[a+i]
        tmax2 = VC.T1[a+i]
    if (VC.CH1[2*a+i] > max3)  and (VC.CH1[2*a+i] != 3.04) :
        max3 = VC.CH1[2*a+i]
        dmax3 = VC.dCH1[2*a+i]
        tmax3 = VC.T1[2*a+i]
        
print(max1,max2,max3)
print(dmax1,dmax2,dmax3)

MAX = (max1+max2+max3)/3
dMAX = sqrt( ((max1-MAX)**2 + (max2-MAX)**2 + (max3-MAX)**2)/2)
print(MAX,dMAX)


com1 = 1.44
com2 = 1.48
com3 = 1.40

COM = (com1+com2+com3)/3
dCOM = sqrt( ((com1-COM)**2 + (com2-COM)**2 + (com3-COM)**2)/2)
print(COM,dCOM,"\n\n")


print(tmax1,tmax2,tmax3)








tcom1 = VC.T1[0]
tcom2 = VC.T1[0]
tcom3 = VC.T1[0]

for i in range(0,a):
    if ((VC.CH1[i] == 1.44) and (VC.CH1[i+1] <0)):
        tcom1 = VC.T1[i] 
for i in range(a,2*a):
    if ((VC.CH1[i] == 1.48) and (VC.CH1[i+1] <0)):
        tcom2 = VC.T1[i]
for i in range(2*a,3*a):
    if ((VC.CH1[i] == 1.40) and (VC.CH1[i+1] == 0.12)):
        tcom3 = VC.T1[i]

print(tcom1,tcom2,tcom3)


deltat1 = tcom1-tmax1
deltat2 = tcom2-tmax2
deltat3 = tcom3-tmax3
print(deltat1,deltat2,deltat3)

DELTAT = (deltat1+deltat2+deltat3)/3
dDELTAT = sqrt( ((deltat1-DELTAT)**2 + (deltat2-DELTAT)**2 + (deltat3-DELTAT)**2)/2)
print(DELTAT,dDELTAT, "\n\n")


###########################################################################

file = "monostabileRes"
data = load_data(dir,file)
# data_err = [mme(data[0], 'ohm'), mme(data[1], 'time', 'oscil')]
data_err = [mme(data[0], 'ohm'), sqrt(((mme(data[1], 'time', 'oscil'))**2)+(3*data[1]/100)**2)]
tab=["$R_1$ [$\Omega$]","Impulso OUT-M [s]"]

latex_table(dir, file, data, data_err, tab)

par, cov = fit_linear(data[0], data[1], dx=data_err[0], dy=data_err[1])
m, q = correlated_values(par, cov)

figure(3)
line = lambda x, m, q: m*x + q

x = linspace(min(data[0])*0.9, max(data[0])*1.05, 1000)
y = line(x, m.nominal_value, q.nominal_value)

chi2 = sum(((data[1] - line(data[0], m.nominal_value, q.nominal_value))/data_err[1])**2)

errorbar(data[0], data[1], xerr=data_err[0], yerr=data_err[1], fmt=',')
plot(x, y)

print(chi2)
print(m)
print(q)
print(cov[0,1]/(sqrt(cov[0,0]*cov[1,1])))

xlim(min(data[0])*0.95, max(data[0])*1.03)
ylim(min(data[1])*0.95, max(data[1])*1.10)
xlabel(tab[0], fontsize = 24)
ylabel(tab[1], fontsize = 24)
ticklabel_format(style='sci', axis='both', scilimits=(0,0))
grid()
# show()
savefig(dir + "./grafici/FITmonostabile.pdf")

