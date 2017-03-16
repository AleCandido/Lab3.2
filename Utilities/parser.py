import numpy as np
import re
import os


def GetBlocks(filename):
    '''
    prende il filename e ritorna la lista [[[pt1.x,pt1.y],...],[blocco2],...]
    '''
    f=open(filename)
    block=False
    lastlist=[]
    listone=[]
    for i in f:
        print(i)
        if(re.match(r"[\d\.]+e[\+\-][\d]+\t[\d\.]+e[\+\-][\d]+", i)):
            print("entrato")
            block=True
            slast=re.findall(r"[\d\.]+e[\+\-][\d]+", i)
            lastlist.append(list(map(float, slast)))
        else:
            if(block):
                listone.append(lastlist)
                lastlist=[]
                block=False
    return listone


print("Test...")

l=GetBlocks(r'C:\Users\silvanamorreale\Documents\GitHub\Lab3.2\parser test.txt')
print(l)
