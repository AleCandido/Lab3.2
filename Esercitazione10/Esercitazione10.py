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
dir= path + "Esercitazione10\\"

from BuzzLightyear import * 
from lab import mme
from uncertainties import *

close("all")

###########################################################################
figure(0)
file="Iin"

vin, iin = loadtxt(dir + "data\\" + file + ".txt", unpack=True)

dvin = mme(vin, 'volt')
diin = mme(iin, 'ampere', 'ice680')

iin *= 1
diin *= 1

xlim(min(vin)*0.9,max(vin)*1.03)
ylim(-max(iin)/20,max(iin)*1.1)
errorbar(vin, iin, xerr=dvin, yerr=diin, fmt=",b")

xlabel("Input voltages [V]")
ylabel("Input currents [mA]")

savefig(dir + "grafici\\" + file + ".pdf")

# ticklabel_format(style='sci', axis='both', scilimits=(0,0))


###########################################################################
figure(1)
file="VinVout"

vin, iin = loadtxt(dir + "data\\" + file + ".txt", unpack=True)

dvin = mme(vin, 'volt')
diin = mme(iin, 'volt')

iin *= 1
diin *= 1

xlim(min(vin)*0.9,max(vin)*1.03)
ylim(-max(iin)/20,max(iin)*1.1)
errorbar(vin, iin, xerr=dvin, yerr=diin, fmt=",b")

title("Tensione di ingresso - tensione di uscita @ $V_{cc}=4.95 \pm 0.03$ V")
xlabel("Input voltages [V]")
ylabel("Output voltages [V]")

savefig(dir + "grafici\\" + file + ".pdf")
print("ginocchio fra i 0.78 - 0.90 V")
print("secondo ginoccho @ 1.060- 1.080 V")


import Oscillografo

CH1=Oscillografo.OscilloscopeData(dir+"data\\CH1.csv")
CH2=Oscillografo.OscilloscopeData(dir+"data\\CH2.csv")

#1285 1435
figure(2)

#x_data=CH1.CH1[((CH1.T1>0.00073) and (CH1.T1<0.0020))]
title("Tensione di ingresso e uscita @ $V_{cc}=4.95 \pm 0.03$ V, oscilloscopio")
xlabel("time [s]")
ylabel("voltages [V]")
plot(CH1.T1, CH1.CH1)
plot(CH2.T1, CH2.CH1)
savefig(dir+ "grafici\\oscRaw.pdf")


figure(3)

plot(CH1.CH1[1285:1435], CH2.CH1[1285:1435])

figure(4)
errorbar(CH1.CH1, CH2.CH1, CH1.dCH1, CH2.dCH1,fmt=None)
xlim(0, 1.6)
title("Tensione di ingresso - tensione di uscita @ $V_{cc}=4.95 \pm 0.03$ V, oscilloscopio")
xlabel("Input voltages [V]")
ylabel("Input voltages [V]")
savefig(dir+ "grafici\\osc.pdf")
