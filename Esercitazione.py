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
dir= path + "Esercitazione/"

from BuzzLightyear import * 
import uncertainties
###########################################################################

file=""

def f(x, a, b):
    return a+b*x

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=[("",""),("","")]

titolo=""
Xlab=""
Ylab=""

tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun)

###########################################################################
