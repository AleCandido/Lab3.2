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

figure(1)

clockT = (counter2.T1 + counter4.T1 + counter8.T1 + counter16.T1)/4
clockV =  (counter2.CH1 + counter4.CH1 + counter8.CH1 + counter16.CH1)/4

plot(clockT, clockV, ",--", label="clock")
plot(counter2.T2, counter2.CH2, ",--", label="divided by 2")
plot(counter4.T2, counter4.CH2, ",--", label="divided by 4")
plot(counter8.T2, counter8.CH2, ",--", label="divided by 8")
plot(counter16.T2, counter16.CH2, ",--", label="divided by 16")

legend(loc=2)
grid()
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