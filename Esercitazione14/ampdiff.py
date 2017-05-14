#amplificazioni, appena possibile diventano con errore


#V_out=AV1-BV2

from lab import *
import uncertainties


def mymme(val,*args, **kwargs):
    return uncertainties.ufloat(val,mme(val, *args, **kwargs))


R23 = mymme(33.3e3, "ohm")
R26 =mymme(33.0e3, "ohm")          
R22 = mymme(38.4e3, "ohm") 
R24 = mymme(39.1e3, "ohm")

A=(R24)/(R23)*(R23+R22)/(R26+R24)
B=R22/R23

print(A, B)

AMC=(A-B)/2
AD=(A+B)/2

print(AMC, AD)