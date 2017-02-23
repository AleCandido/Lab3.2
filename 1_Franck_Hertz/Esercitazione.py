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
import lab


#non è proprio la cosa giusta, ma basta mettere il giusto g...
def diffe(l, g=lambda x: x[4]):
    for i in range(1, len(l)):
        try:
            yield g(l[i])-g(l[i-1])
        except:
            return



def diffe(l):
    j=0
    la=None
    for i in l:
        if(j==0):
            pass
        else:
            yield i-la
        la=i
        j+=1
        
util.defoult_hwindow=20
results={}
for i in range(0, 10):
    results[i]=[None,None, None, None]
    base=300
    fine=2200
    
    file=dir+"csv\\Task9.{}.csv".format(i)
    o=OscilloscopeData(file)
    
    
    retta=lambda x, mm, qq: mm*x+qq
    rdatas=o.CH1[base: fine] #scusate
    dom=np.array(range(len(rdatas)))
    par, covs=lab.curve_fit(retta,dom, rdatas)    
    print(par, covs)
    m, q=uncertainties.correlated_values(par, covs)
    mm=m.n
    qq=q.n
    pylab.figure(0)
    pylab.plot(dom, rdatas)
    pylab.plot(dom, retta(dom, mm, qq))
    
    print("M={}, Q={}".format(m, q))
    print("è da aggiungere unn errore sistematrico di 0.4 volt a Q")
    
    #costruiamo i dati da far mangiare alla routine di trova massimi....   
    util.debug=1 
    maxs=util.BetterFindLocalMaxs(o.CH2[base: fine], o.dCH2[base: fine])
    util.debug=0

    vets=[]
    maxs=sorted(maxs, key=lambda x: x[0])
    for max in maxs: 
        vets.append(retta(max[0]+max[4] ,mm , qq)) #chiaramente quì all'errore su qq non deve essere aggiunto l'errore sistematico....
    #print(vets)
    diffs=list(diffe(vets))
    #se l'amplificatore va in clipping allora l'ultimo massimo è finto...
    if(len(diffs)>0):
        if(rdatas[len(rdatas)-1]>0.4375):
            diffs.pop(len(diffs)-1)
           # vets.pop(len(vets)-1)
    print(diffs)
    results[i][0]=diffs
    results[i][1]=vets
     #attenzione, l'ultima differenza è sempre da buttare...
    
    maxs=util.BetterFindLocalMins(o.CH2[base: fine], o.dCH2[base: fine])
    maxs=sorted(maxs, key=lambda x: x[0])
    vets=[]
    for max in maxs: 
        vets.append(retta(max[0]+max[4] ,mm , qq)) #chiaramente quì all'errore su qq non deve essere aggiunto l'errore sistematico....
    #print(vets)
    diffs=list(diffe(vets))
    print(diffs)
    results[i][2]=diffs
    results[i][3]=vets
     #attenzione, l'ultima differenza è spesso da buttare...
    
f=open(dir+"results.txt", "w")
for i in results:
    f.write(str(i)+"    --->    "+str(results[i])+"    --->    "+ str(m)+" "+str(q) +"\n\r")

f.close()
