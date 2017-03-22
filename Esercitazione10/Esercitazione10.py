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
dir= path + "Esercitazione10\\"

from BuzzLightyear import * 
from lab import mme
from uncertainties import *
###########################################################################

file="Iin"

vin, iin = loadtxt(dir + "data\\" + file + ".txt", unpack=True)

dvin = mme(vin, 'volt')
diin = mme(iin, 'ampere', 'ice680')

iin *= 1
diin *= 1

xlim(min(vin)*0.9,max(vin)*1.03)
ylim(-max(iin)/20,max(iin)*1.1)
errorbar(vin, iin, xerr=dvin, yerr=diin, fmt=",b")

xlabel("Input voltages [V]")
ylabel("Input currents [mA]")

savefig(dir + "grafici\\" + file + ".pdf")

# ticklabel_format(style='sci', axis='both', scilimits=(0,0))


###########################################################################
