import sys
import pylab
from scipy.optimize import curve_fit
from scipy.stats import chisqprob
import numpy as np
from numpy import *
from pylab import *
import lab
from lab import *


import getpass
users={"candi": "C:\\Users\\candi\\Documents\\GitHub\\Lab3.2\\",
"silvanamorreale":"C:\\Users\\silvanamorreale\\Documents\\GitHub\\Lab3.2\\" ,
"Studenti": "C:\\Users\\Studenti\\Desktop\\Lab3\\",
"User":"C:\\Users\\User\\Documents\\GitHub\\Lab3.2\\",
"andrea": "/home/andrea/Documenti/Da salvare 12-5-2017/Documenti/GitHub/Lab3.2/"
}
try:
    user=getpass.getuser()
    path=users[user]
    print("buongiorno ", user, "!!!")
except:
    raise Error("unknown user, please specify it and the path in the file Esercitazione*.py")


sys.path = sys.path + [path]
mydir= path + "Esercitazione15/"


todos=["postpreamp.py", "prepreamp.py", "passabanda.py", "calibrazioneRMS.py","amp_alternativa.py","lastfit.py"]
Results=[]

figsnum=0

for i in todos:
    file=open(mydir+i)
    exec(file.read())
    print("\n\n\n\n")
    


print("\n\n\n\n Grazie a tutti per la magnifica scoperta!!!")
    



