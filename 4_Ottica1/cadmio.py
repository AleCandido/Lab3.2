from lab import *
from pylab import *
from uncertainties import *

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
dir= path + "4_Ottica1\\"

##

alphar = loadtxt(dir + "data\\cadmio.txt", unpack=True)

lamda = array([ 467.8, 480.0, 508.6, 643.8])*10**(-9)
nu = 1/lamda

alpha0 = ufloat(10.895, 0.026)

alpha = []
dalpha = []

alpha += [0]