from pylab import *
from lab import *
from uncertainties import *
from uncertainties import unumpy

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
dir= path + "3_Ottica2\\"

##

lamb = 632.8
m =  ufloat(70,1)

dX = 0.5 * m * lamb
r = dX/10**4

print(r)

mv = ufloat(,)

lambdav = 2*dX* mv

print(lambdav)