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
dir= path + "Esercitazione11\\"

from BuzzLightyear import * 
from uncertainties import *
###########################################################################

from Oscillografo import *

AB = OscilloscopeData(dir+"data\\AB.csv")
andAO = OscilloscopeData(dir+"data\\andAO.csv")
orAO = OscilloscopeData(dir+"data\\orAO.csv")
xorAO = OscilloscopeData(dir+"data\\xorAO.csv")

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

########################################################################### parte astabile-stabile in serie...

#grafici...
O1 = OscilloscopeData(dir+"data\\4OutM.csv")
O2 = OscilloscopeData(dir+"data\\410030.csv")


figure(123)

plot(O1.T1, O1.CH1)
plot(O1.T2, O1.CH2)

figure(1234)

plot(O2.T1, O2.CH1)
plot(O2.T2, O2.CH2)



#analisi tempi...




myprint_dict={}

def printufloat(X):
    x=X.n
    y=X.s
    return str(x)+" \\pm "+str(y) 

myprint_dict[uncertainties.ufloat]=printufloat

def printArray(x):
    s="array(["
    for i in x:
        s+=myprint(i)+","
    return s+"])"

myprint_dict[np.array]=printArray


def myprint(x):
    if type(x) in myprint_dict:
        print(type(x))
        return myprint_dict[type(x)](x)
    return str(x)


def my_latex_table(directory, file_, data, tab):
    """
        Parameters
        ----------    

        Returns
        -------

    """
    with open(directory+"tabelle/tab_"+file_+".txt", "w") as text_file:
        print(data)
        text_file.write("\\begin{tabular}{c")
        for z in range (1,len(tab)):
            text_file.write("|c")
        text_file.write("} \n")
        text_file.write("%s" % tab[0])
        for z in range (1,len(tab)):
            text_file.write(" & %s" % tab[z])
        text_file.write("\\\\\n\hline\n")
        for i in range (len(data[0])):
            text_file.write("%s" % myprint(data[0][i]))
            for j in range (1,len(tab)):
                print(i, j)
                print(data[j][i])
                text_file.write(" & %s" % myprint(data[j][i]))
            text_file.write("\\\\\n")
        text_file.write("\\end{tabular}")
        text_file.close()






file="bothRes.txt"
data=np.loadtxt(dir+"\\data\\bothRes.txt")
R1=data[:,0]
dR1=mme(R1, "ohm")
R2=data[:,1]
dR2=mme(R2, "ohm")
T1=data[:,2]*1e-6
dT1=np.ones(T1.shape)*1e-6
T2=data[:,3]*1e-6
dT2=np.ones(T2.shape)*1e-6
#approccio fit multipli...


print("Fit per righe...")

figure(2)


se={}
for i,j in zip(R2, dR2):
    if(not (i in se)):
        se[i]=j


results=[]
cond=[]

for i in se:
    mask=R2==i
    r1=R1[mask]
    dr1=dR1[mask]
    t1=T1[mask]
    dt1=dT1[mask]
    t2=T2[mask]
    dt2=dT2[mask]
    print(i)
    print(r1)
    par, cov = fit_linear(r1, t2, dx=dr1, dy=dt2)
    m, q = correlated_values(par, cov)
    chisq = sum((t2-line(r1, *par))**2/(dr1**2+dt2**2))
    cond.append(ufloat(i, se[i]))
    results.append([par, cov, m, q, chisq])
    print("m={} , q={}".format(m, q))
    print("chiq={} su {} dof".format(chisq, len(r1)))
    domain=np.linspace(np.min(r1), np.max(r1))
    pylab.plot(domain, line(domain, *par))
    pylab.errorbar(r1, t2, dt2, dr1)
    print("==============")

results=np.array(results)
ms=results[:,2]
qs=results[:,3]
chisqs=results[:,4]
nomi=["R_2", "T/R", "T_0", "\\chi^2"]
f=uncertainties.unumpy.nominal_values
ff=uncertainties.unumpy.std_devs
my_latex_table(dir, "fit per righe.txt", [cond, ms, qs, chisqs], nomi)


mnvs=uncertainties.unumpy.nominal_values(ms)
mstds=uncertainties.unumpy.std_devs(ms)
mfin, varmfin=fit_const_yerr(mnvs, mstds)

qnvs=uncertainties.unumpy.nominal_values(qs)
qstds=uncertainties.unumpy.std_devs(qs)
qfin, varqfin=fit_const_yerr(qnvs, qstds)

chifin1=sum((mfin-mnvs)**2/mstds**2)
chifin2=sum((qfin-qnvs)**2/qstds**2)



figure(3)
pylab.subplot(311)
pylab.plot(range(len(mnvs)),(mfin-mnvs)/mstds, 'b.')
pylab.subplot(312)
pylab.plot(range(len(qnvs)), (qfin-qnvs)/qstds, 'b.')


mfin=uncertainties.ufloat(mfin, varmfin**0.5)
qfin=uncertainties.ufloat(qfin, varqfin**0.5)

print("------>>>>   m={} , q={}, chisq1={},  chisq2={}".format(mfin, qfin, chifin1, chifin2))
print("c'è qualche problema...")


print("=======================")
print("=======================")

print("Fit per colonne...")

figure(4)

results=[]
cond=[]

se={}
for i,j in zip(R1, dR1):
    if(not (i in se)):
        se[i]=j


for i in se:
    mask=R1==i
    r2=R2[mask]
    if(len(r2)>2):
        dr2=dR2[mask]
        t1=T1[mask]
        dt1=dT1[mask]
        t2=T2[mask]
        dt2=dT2[mask]
        print(i)
        print(r2)
        par, cov = fit_linear(r2, t1, dx=dr2, dy=dt1)
        m, q = correlated_values(par, cov)
        chisq = sum((t1-line(r2, *par))**2/(dr2**2+dt1**2))
        cond.append(ufloat(i, se[i]))
        results.append([par, cov, m, q, chisq])
        print("m={} , q={}".format(m, q))
        print("chiq={} su {} dof".format(chisq, len(r2)))
        domain=np.linspace(np.min(r2), np.max(r2))
        pylab.plot(domain, line(domain, *par))
        pylab.errorbar(r2, t1, dt1, dr2)
        print("==============")




results=np.array(results)
ms=results[:,2]
qs=results[:,3]
chisqs=results[:,4]
nomi=["R_2", "T/R", "T_0", "\\chi^2"]
f=uncertainties.unumpy.nominal_values
ff=uncertainties.unumpy.std_devs
my_latex_table(dir, "fit per righe.txt", [cond, ms, qs, chisqs], nomi)


mnvs=uncertainties.unumpy.nominal_values(ms)
mstds=uncertainties.unumpy.std_devs(ms)
mfin, varmfin=fit_const_yerr(mnvs, mstds)

qnvs=uncertainties.unumpy.nominal_values(qs)
qstds=uncertainties.unumpy.std_devs(qs)
qfin, varqfin=fit_const_yerr(qnvs, qstds)

chifin1=sum((mfin-mnvs)**2/mstds**2)
chifin2=sum((qfin-qnvs)**2/qstds**2)



figure(5)
pylab.subplot(511)
pylab.plot(range(len(mnvs)),(mfin-mnvs)/mstds, 'b.')
pylab.subplot(512)
pylab.plot(range(len(qnvs)), (qfin-qnvs)/qstds, 'b.')


mfin=uncertainties.ufloat(mfin, varmfin**0.5)
qfin=uncertainties.ufloat(qfin, varqfin**0.5)

print("------>>>>   m={} , q={}, chisq1={},  chisq2={}".format(mfin, qfin, chifin1, chifin2))
print("E' effettivamente lineare e non dipende da nulla...")





#un approccio bidimensionale non ha troppo senso....







