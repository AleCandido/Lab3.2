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
dir= path + "Esercitazione12\\"

from BuzzLightyear import * 
from uncertainties import *
import uncertainties
###########################################################################

from Oscillografo import *
from statistics import mean

counter2 = OscilloscopeData(dir+"data\\counter2.csv")
counter4 = OscilloscopeData(dir+"data\\counter4.csv")
counter8 = OscilloscopeData(dir+"data\\counter8.csv")
counter16 = OscilloscopeData(dir+"data\\counter16.csv")
csv81 = OscilloscopeData(dir+"data\\81.csv")

counter16aT = (counter2.T1 + counter4.T1 + counter8.T1 + counter16.T1)/4
counter16aV =  (counter2.CH1 + counter4.CH1 + counter8.CH1 + counter16.CH1)/4

fig = figure(1)
axes = [fig.add_subplot(5, 1, r ) for r in range(0, 5)]

subplot(511)
plot(counter16aT, counter16aV, ",--", label="divided by 16")
axes[1].locator_params(axis='y', tight=True, nbins=5)
axes[1].set_xticks([])
legend(loc=1)

subplot(512)
plot(counter2.T2, counter2.CH2, ",--", label="divided by 8")
axes[2].locator_params(axis='y', tight=True, nbins=5)
axes[2].set_xticks([])
legend(loc=1)

subplot(513)
plot(counter4.T2, counter4.CH2, ",--", label="divided by 4")
axes[3].locator_params(axis='y', tight=True, nbins=5)
axes[3].set_xticks([])
legend(loc=1)

subplot(514)
plot(counter8.T2, counter8.CH2, ",--", label="divided by 2")
axes[4].locator_params(axis='y', tight=True, nbins=5)
axes[4].set_xticks([])
legend(loc=1)
    
subplot(515)
plot(counter16.T2, counter16.CH2, ",--", label="clock")
# axes[5].locator_params(axis='y', tight=True, nbins=5)
legend(loc=1)
# grid()
#  meglio niente griglia, la figura è piccola e diventa troppo affollata

savefig(dir + "grafici\\counter.pdf")

figure(2)

plot(csv81.T1, csv81.CH1, ",--", label="bit 1-0")
plot(csv81.T2, csv81.CH2, ",--", label="bit 8-0")

legend(loc=6)
grid()
savefig(dir + "grafici\\counter10.pdf")


show()
# close('all')

###########################################################################