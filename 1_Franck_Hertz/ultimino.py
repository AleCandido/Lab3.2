import pylab
import lab
import scipy.stats

pylab.close("all")


xdata=np.array([1.5,3.0 ,4.0 ,5.0,6.0 ,7.0 ,8.0,9.0 ,10.0])
ydata=np.array([ 20.1,18.2, 18.3, 18.1, 17.8, 18.3, 18.2, 18.6, 18.8])
dydata=0.04#0.01*ydata
dxdata=0.1

pylab.figure(0)
pylab.title("Primo punto di minimo in funzione della tensione $U_E$")
pylab.xlabel("$U_E$ [V]")
pylab.ylabel("$U_A$ [V]")
pylab.errorbar(xdata, ydata, dydata, dxdata, fmt=".")

a, vara = lab.fit_const_yerr(ydata, dydata)

pylab.plot([0, 10], [a, a])

chiq=sum((ydata-a)**2/dydata**2)
p = scipy.stats.chi2(len(ydata)-1).cdf(chiq)



print(a, vara)
print(chiq, p)




xdata=np.array([3.0 ,4.0 ,5.0,6.0 ,7.0 ,8.0,9.0 ,10.0])
ydata=np.array([ 35.5, 35.6, 35.5,  35.6,  35.7, 35.5, 35.9, 35.3])
dydata=0.04#0.005*ydata
dxdata=0.1

pylab.figure(1)
pylab.title("Secondo punto di minimo in funzione della tensione $U_E$")
pylab.xlabel("$U_E$ [V]")
pylab.ylabel("$U_A$ [V]")
pylab.errorbar(xdata, ydata, dydata, dxdata, fmt=".")

a, vara = lab.fit_const_yerr(ydata, dydata)

pylab.plot([0, 10], [a, a])

chiq=sum((ydata-a)**2/dydata**2)
p = scipy.stats.chi2(len(ydata)-1).cdf(chiq)



print(a, vara)
print(chiq, p)




xdata=np.array([5.0, 6.0 ,7.0 ,8.0,9.0 ,10.0])
ydata=np.array([ 58.8, 56.2, 56.4, 55.8, 56.6, 56.7])
dydata=0.04#0.03*ydata
dxdata=0.1
pylab.figure(2)
pylab.title("Terzo punto di minimo in funzione della tensione $U_E$")
pylab.xlabel("$U_E$ [V]")
pylab.ylabel("$U_A$ [V]")
pylab.errorbar(xdata, ydata, dydata, dxdata, fmt=".")

a, vara = lab.fit_const_yerr(ydata, dydata)

pylab.plot([0, 10], [a, a])

chiq=sum((ydata-a)**2/dydata**2)
p = scipy.stats.chi2(len(ydata)-1).cdf(chiq)



print(a, vara)
print(chiq, p)


