import numpy as np

def angle(gradi, primi):
    return gradi+1/60*primi
    
def degree(gradi, primi):
    return angle(gradi, primi)*np.pi/360

def Angle(decimal):
    return (np.floor(decimal),60*(decimal-np.floor(decimal)))

A1=angle(348,40)
A2=angle(348, 41)
A3=angle(348, 45)

l=[A1, A2, A3]
mean=(A1+A2+A3)/3
stddev=sqrt(sum((ll - mean)**2 for ll in l)/len(l))
print(Angle(mean), "+-", Angle(stddev))



A1=angle(8,56)
A2=angle(8, 55)
A3=angle(8, 56)



l=[A1, A2, A3]
mean=(A1+A2+A3)/3
stddev=sqrt(sum((ll - mean)**2 for ll in l)/len(l))
print(Angle(mean), "+-", Angle(stddev))


A1=angle(69,30)
A2=angle(69, 28)
A3=angle(69, 30)





l=[A1, A2, A3]
mean=(A1+A2+A3)/3
stddev=sqrt(sum((ll - mean)**2 for ll in l)/len(l))
print(Angle(mean), "+-", Angle(stddev))


