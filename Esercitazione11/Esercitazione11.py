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

AB = OscilloscopeData("C:\\Users\candi\Documents\GitHub\Lab3.2\Esercitazione11\data\\AB.csv")
andAO = OscilloscopeData("C:\\Users\candi\Documents\GitHub\Lab3.2\Esercitazione11\data\\andAO.csv")
orAO = OscilloscopeData("C:\\Users\candi\Documents\GitHub\Lab3.2\Esercitazione11\data\\orAO.csv")
xorAO = OscilloscopeData("C:\\Users\candi\Documents\GitHub\Lab3.2\Esercitazione11\data\\xorAO.csv")

figure(1)
fig,ax = subplots(1)

plot(AB.T1, AB.CH1, ",--", label="input1")
plot(AB.T2, AB.CH2, ",--", label="input2")
plot(andAO.T2, andAO.CH2, ",-", label="AND")


ax.set_yticklabels([])
ax.set_xticklabels([])
legend(loc=6)

savefig(dir + "grafici\\ANDard.pdf")

figure(2)
fig,ax = subplots(1)

plot(AB.T1, AB.CH1, ",--", label="input1")
plot(AB.T2, AB.CH2, ",--", label="input2")
plot(orAO.T2, orAO.CH2, ",-", label="OR")


ax.set_yticklabels([])
ax.set_xticklabels([])
legend(loc=6)

savefig(dir + "grafici\\ORard.pdf")

figure(3)
fig,ax = subplots(1)

plot(AB.T1, AB.CH1, ",--", label="input1")
plot(AB.T2, AB.CH2, ",--", label="input2")
plot(xorAO.T2, xorAO.CH2, ",-", label="XOR")


ax.set_yticklabels([])
ax.set_xticklabels([])
legend(loc=6)

savefig(dir + "grafici\\XORard.pdf")

figure(4)
fig,ax = subplots(1)

plot(AB.T1, AB.CH1, ",:", label="input1")
plot(AB.T2, AB.CH2, ",:", label="input2")
plot(xorAO.T2, xorAO.CH2, ",--", label="SUM")
plot(andAO.T2, andAO.CH2, ",-", label="CARRY")


ax.set_yticklabels([])
ax.set_xticklabels([])
legend(loc=6)

savefig(dir + "grafici\\ADDERard.pdf")

# show()
close('all')

###########################################################################

file = "astabileRes"
data = load_data(dir,file)
data_err = [mme(data[0], 'ohm'), mme(data[1], 'time', 'oscil')]
tab=["$R_2$ [$\Omega$]","Period [s]"]

latex_table(dir, file, data, data_err, tab)

par, cov = fit_linear(data[0], data[1], dx=data_err[0], dy=data_err[1])
m, q = correlated_values(par, cov)

line = lambda x, m, q: m*x + q

x = linspace(min(data[0])*0.9, max(data[0])*1.05, 1000)
y = line(x, m.nominal_value, q.nominal_value)

chi2 = sum(((data[1] - line(data[0], m.nominal_value, q.nominal_value))/data_err[1])**2)

errorbar(data[0], data[1], xerr=data_err[0], yerr=data_err[1], fmt=',')
plot(x, y)

xlim(min(data[0])*0.88, max(data[0])*1.06)
ylim(min(data[1])*0.88, max(data[1])*1.06)
xlabel(tab[0], fontsize = 24)
ylabel(tab[1], fontsize = 24)
ticklabel_format(style='sci', axis='both', scilimits=(0,0))

savefig(dir + "./grafici/FITastabile.pdf")

