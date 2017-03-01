import os
import lab
import pylab
import numpy as np



xdata, ydata=np.loadtxt(r'C:\Users\silvanamorreale\Documents\GitHub\Lab3.2\2_E-m\dati_1.txt')
dydata=lab.mme(ydata,"volt")#np.ones(xdata.size)
dxdata=lab.mme(xdata, "ampere")
retta=lambda x, m, q: m*x+q
a, b=lab.fit_generic_xyerr(lambda x, m, q: m*x+q, xdata, ydata, dxdata, dydata)
dom=np.linspace(min(xdata), max(xdata), 100)
pylab.plot(dom, retta(dom, a, b))
pylab.errorbar(xdata, ydata, dydata, dxdata)