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
dir= path + "Esercitazione15\\"

from BuzzLightyear import * 
import uncertainties
###########################################################################

file = "calibrazioneRMS"
data = load_data(dir,file)
data_err = [mme(data[0], 'volt'), mme(data[1], 'volt', 'oscil')]
tab=["$V_{chip}$ [$\\volt$]","$V_{osc}$ [$\\volt$]"]

latex_table(dir, file, data, data_err, tab)

###########################################################################

file = "passabanda"
data = load_data(dir,file)
data_err = [51/1e6*data[0], mme(data[1], 'volt', 'oscil'), mme(data[2], 'volt', 'oscil')]
tab=["Freq. [$\hertz$]","$V_{in}$ [$\\volt$]", "$V_{out}$ [$\\volt$]"]

latex_table(dir, file, data, data_err, tab)

##########################################################################

file = "prepreamp"
data = load_data(dir,file)
data_err = [51/1e6*data[0], mme(data[1], 'volt', 'oscil'), mme(data[2], 'volt', 'oscil')]
tab=["Freq. [$\hertz$]","$V_{in}$ [$\\volt$]", "$V_{out}$ [$\\volt$]"]

latex_table(dir, file, data, data_err, tab)

##########################################################################

file = "postpreamp"
data = load_data(dir,file)
data_err = [51/1e6*data[0], mme(data[1], 'volt', 'oscil'), mme(data[2], 'volt', 'oscil')]
tab=["Freq. [$\hertz$]","$V_{in}$ [$\\volt$]", "$V_{out}$ [$\\volt$]"]

latex_table(dir, file, data, data_err, tab)

##########################################################################

file = "totamp"
data = load_data(dir,file)
data[1] = data[1]*1e-3
data_err = [51/1e6*data[0], mme(data[1], 'volt', 'oscil'), mme(data[2], 'volt', 'oscil'), mme(data[3], 'volt')]
data[1] = data[1]*1e3
data_err[1] = data_err[1]*1e3
tab=["Freq. [$\hertz$]","$V_{in}$ [$\milli\\volt$]", "$V_{out}$ [$\\volt$]", "$V_{rms}$ [$\\volt$]"]

latex_table(dir, file, data, data_err, tab)

##########################################################################

file = "lastfit"
data = load_data(dir,file)
data_err = [mme(data[0], 'ohm')] + [mme(data[i]*1e-3, 'volt') for i in range(1,8)]
for i in range(1,8):
    data_err[i] = data_err[i]*1e3
tab=["Res. [$\ohm$]"] + ["$V_{rms}$ [$\milli\\volt$]" for i in range(1,8)]

latex_table(dir, file, data, data_err, tab)

##########################################################################

file = "lastfit1"
data = load_data(dir,file)
data_err = [mme(data[0], 'ohm')] + [mme(data[i]*1e-3, 'volt') for i in range(1,7)]
for i in range(1,7):
    data_err[i] = data_err[i]*1e3
tab=["Res. [$\ohm$]"] + ["$V_{rms}$ [$\milli\\volt$]" for i in range(1,7)]

latex_table(dir, file, data, data_err, tab)