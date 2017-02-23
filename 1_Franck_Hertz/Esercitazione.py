from pylab import *

import getpass
users={"candi": "C:\\Users\\alessandro\\Documents\\GitHub\\Lab3.2\\",
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
    maxs=util.BetterFindLocalMaxs(o.CH2[((o.CH1>0) * (o.CH1<60))], o.dCH2[((o.CH1>0) * (o.CH1<60))])
    diffe1=list(diffe(maxs))
    #print(diffe1)
    #mins=util.BetterFindLocalMins(o.CH2, o.dCH2)
    #print(mins)
    #diffe2=list(diffe(mins))
    #print("maxsl={}, minl={}".format(len(maxs), len(mins)))
    for i in range(4):
        print("\n\r")
