from pylab import *

# bisogna sicuramente cambiare i nomi e gli indirizzi quaggiù

import getpass
if getpass.getuser() == "alessandro"
    path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
elif getpass.getuser() == "Roberto"
    path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
elif getpass.getuser() == "Studenti"
    path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
else
    raise Error("unknown user, please specify it and the path in the file Esercitazione*.py")
sys.path = sys.path + [path]
dir= path + "Esercitazione/"

from analyzer import *
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
