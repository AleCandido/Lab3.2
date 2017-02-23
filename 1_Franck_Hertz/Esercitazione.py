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
dir= path + "1_Franck_Hertz\\"

from BuzzLightyear import * 
import uncertainties
import util
from Oscillografo import *


#non è proprio la cosa giusta, ma basta mettere il giusto g...
def diffe(l, g=lambda x: x[4]):
    for i in range(1, len(l)):
        try:
            yield g(l[i])-g(l[i-1])
        except:
            return





for i in range(5, 6):
    file=dir+"csv\\Task9.{}.csv".format(i)
    o=OscilloscopeData(file)
    
    #fittiamo la retta...
    rdatas=o.CH1[o.CH1>0]
    ddatas=o.dCH1[o.CH1>0]
    rdatas=rdatas[0: len(rdatas)-1]
    print(ddatas)
    par, covs=lab.fit_affine_xerr(rdatas, range(len(rdatas)),[0.4])    
    print(par, covs)
    m, q=uncertainties.correlated_values(par, covs)
    M=1/m
    Q=-q/m
    
    print(M)
    print(Q)
    mm=M.n
    qq=Q.n
    dom=np.array(range(len(rdatas)))
    pylab.figure(0)
    pylab.plot(dom, rdatas)
    pylab.plot(dom, (lambda x: mm*x+qq)(dom))
    
    
    maxs=util.BetterFindLocalMaxs(o.CH2, o.dCH2)#, o.dCH2)#
    for max in maxs: 
        print((max[4], max[5]))
    
   
   
   #  
   #  diffe1=list(diffe(maxs))
   #  print(diffe1)
   #  mins=util.BetterFindLocalMins(o.CH2, o.dCH2)
   #  print(mins)
   #  diffe2=list(diffe(mins))
   #  print("maxsl={}, minl={}".format(len(maxs), len(mins)))
   #  for i in range(4):
   #      print("\n\r")
