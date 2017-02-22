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

for i in range(0, 10):
    file=dir+"csv\\Task9.{}.csv".format(i)
    o=OscilloscopeData(file)
    o.plot()
    maxs=util.BetterFindLocalMaxs(o.CH2, o.dCH2)
    mins=util.BetterFindLocalMins(o.CH2, o.dCH2)
    print("maxsl={}, minl={}".format(len(maxs), len(mins)))
