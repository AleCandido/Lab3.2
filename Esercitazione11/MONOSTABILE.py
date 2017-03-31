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
import uncertainties
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
print(dmax1,dmax2,dmax3,"\n\n")
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