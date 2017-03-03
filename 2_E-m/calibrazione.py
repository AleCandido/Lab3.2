from pylab import *
from scipy.optimize import curve_fit
from uncertainties import *
from uncertainties import unumpy
import sys
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
dir= path + "2_E-m\\"

ids = [i for i in range(11,29)] + [30,32,33,35,37,39,41,44,45,46,48,50]
calibrazionels = []
offsetls = []

for id in ids:
    a13,b13=loadtxt(dir+"data\\{}r.txt".format(id), unpack=True)
    dx = 4
    dy = 3
    
    x = array([ufloat(0,0) for i in range(0,len(a13))])
    y = array([ufloat(0,0) for i in range(0,len(b13))])
    
    for i in range(0,len(a13)):
        x[i] = ufloat(a13[i], dx)
        y[i] = ufloat(b13[i], dy)
    
    # graphic to view data
    # figure(id)
    # subplot(2,1,1)
    # errorbar(a13,b13,dy,dx, linestyle = '' , color = 'black', marker = '.')
    rc('font',size=16)
    xlabel('', labelpad = -7)
    ylabel('')
    title('')
    # xlim(-0.2,5)
    # ylim(,)
    # minorticks_on()
    grid()
    legend()
    
    def func(x,a,b):
        return a+b*x
    
    # estimated values of the parameters
    inval=array([1,2])
    
    A=inval[0]
    B=inval[1]
    a0=0.
    b0=0.
    while abs(A-a0)>10**(-5) and abs(B-b0)>10**(-5):
        
        # Override the step n-2
        A=a0
        B=b0
    
    # error (neglect dx)
    # sigma = dy
    
    #strumental error (dx not negligible, or use 'A' in the formula or calculate before 'a' and then insert and recalculate)
    # sigma = sqrt(dy+abs(A)*dx)
        
    #statistical error (dx not negligible, or use 'A' in the formula or calculate before 'a' and then insert and recalculate)
    sigma = sqrt(dy**2+(A*dx)**2)
    
    "peso statistico"
    w = 1/sigma**2
    
    #best-fit and chi square
    'al posto di sigma va err a seconda dei casi'
    pars,covm = curve_fit(func,a13,b13,inval,sigma)
    # Calculate chi square with n DOF
    chi2 = ((w*(b13-func(a13,pars[0],pars[1]))**2)).sum()
    ndof = len(a13)-len(inval)
    sigmachi2 = sqrt(2*ndof)
    # significance level
    # liv_sign = scipy.special.chdtrc(ndof, chi2)
    
    # Results (linear correlation coefficient = normalized covariance)
#     print('Risultati Best-fit Numerico:')
#     print('a0 = ', pars[0], '+/-', sqrt(covm[0,0]))
#     print('b0 = ', pars[1], '+/-', sqrt(covm[1,1]))
#     print('norm_cov = ', covm[0,1]/(sqrt(covm[0,0]*covm[1,1])))
#     print('chi2/ndof = %f/%d' %(chi2, ndof))
#     print('sigmachi2 = %f' % sigmachi2)
    
    # print('liv_sign = %f' %p)
    
    
    # prepare a dummy array and plot the fitting curve 
    xx=linspace(min(a13),max(a13),100)
    # plot(xx,func(xx,pars[0],pars[1]))
    # savefig(’figure1.pdf’)
    a = ufloat(pars[0],sqrt(covm[0,0]))
    b = ufloat(pars[1],sqrt(covm[1,1]))
    px = array([ufloat(0,0) for i in range(0,len(x))])
    py = array([ufloat(0,0) for i in range(0,len(y))])
    d = array([ufloat(0,0) for i in range(0,len(x))])
    
    for i in range (0,len(x)):
        px[i] = ((b*y[i]) + x[i] - (a*b))/(1+b**2)
        py[i] = ((b*x[i])+ a- (y[i]*(b**2)))/(1+b**2)
        
    
    d = unumpy.sqrt( (px-px[0])**2 + (py-py[0])**2   )
    
    
    # dpx = sqrt(dx**2+ (b*dy)**2)/(1+b**2)
    # dpy = sqrt((b*dx)**2+ (dy*b**2)**2)/(1+b**2)
    # 
    # print(dpx,dpy)
    
    dnom = array([0. for i in range(1,len(d))])
    dstd = array([0. for i in range(1,len(d))])
    
    for i in range(1,len(d)):
        dnom[i-1] = d[i].nominal_value
        dstd[i-1] = d[i].std_dev
    
    a14 = array([i/2 for i in range(1,len(d))])
    
    
    # figure(100 + id)
    from lab import fit_linear
    par,cov = fit_linear(a14,dnom, dy=dstd)
#     print("calibrazione:", par[0], "+/-", sqrt(cov[0,0]), "pixel/cm")
#     print("offset:", par[1], "+/-", sqrt(cov[1,1]), "pixel")
    # plot(a14,dnom,"ko")
    
    calibrazionels = calibrazionels + [ufloat(par[0],sqrt(cov[0,0]))]
    offsetls = offsetls + [ufloat(par[1],sqrt(cov[1,1]))]