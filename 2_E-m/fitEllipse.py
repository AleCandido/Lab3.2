#Fit ad un ellisse
import numpy as np
import pylab
#per calcolare autovalori/autovettori e per fare l'inversa di una matrice
from numpy.linalg import eig, inv
import sys
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
dir= path + "2_E-m\\"

ids = [i for i in range(11,29)] + [30,32,33,35,37,39,41,44,45,46,48,50]
for id in ids:
    a,b =pylab.loadtxt(dir + 'data\\{}.txt'.format(id), unpack=True)
#     pylab.figure(id)
    #per le notazioni guardare il file pdf 'circle fit'
    # a,b = pylab.loadtxt( 'C:\\Users\\User\\Documents\\GitHub\\Lab3.2\\2_E-m\\data\\46.txt' , unpack = True)

    # estraggo le righe pari
    a0 = pylab.array([a[i] for i in range(0,len(a),2)]) 
    b0 = pylab.array([b[i] for i in range(0,len(b),2)])
    
    # estraggo le righe dispari
    a1 = pylab.array([a[i] for i in range(1,len(a),2)]) 
    b1 = pylab.array([b[i] for i in range(1,len(b),2)])
    
    # compongo l'array dei punti (x1,x2,y1,y2)
    P = pylab.array([a0,a1,b0,b1])
    
    x = (P[0] + P[1])/2
    y = (P[2] + P[3])/2
    dx = abs((P[0] - P[1])/2)   #devo inserire un minimo --> se l'elemento è minore di una soglia applica la soglia
    dy = abs((P[2] - P[3])/2)
    
    
    # x,y= pylab.loadtxt( 'C:\\Users\\User\\Documents\\GitHub\\Lab3.2\\2_E-m\\data\\46.txt' , unpack = True) 
        
    def fitEllipse(x,y):
        x = x[:,np.newaxis]
        y = y[:,np.newaxis]
    #creo un unico array unendo vari array,separandoli con uno stack
        D =  np.hstack((x*x, x*y, y*y, x, y, np.ones_like(x)))
        S = np.dot(D.T,D)
    #matrice che mi serve per imporre la condizione 'cerco un'ellisse'
        C = np.zeros([6,6])
        C[0,2] = C[2,0] = 2; C[1,1] = -1
    #autovalori e autovettori
        E, V =  eig(np.dot(inv(S), C))
        n = np.argmax(np.abs(E))
    #array parametri conica
        a = V[:,n]
        return a
    
    def ellipse_center(a):
        b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
        num = b*b-a*c
        x0=(c*d-b*f)/num
        y0=(a*f-b*d)/num
        return np.array([x0,y0])
    
    
    # def ellipse_angle_of_rotation( a ):
    #     b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
    #     return 0.5*np.arctan(2*b/(a-c))
    
    
    def ellipse_axis_length( a ):
        b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
        up = 2*(a*f*f+c*d*d+g*b*b-2*b*d*f-a*c*g)
        down1=(b*b-a*c)*( (c-a)*np.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
        down2=(b*b-a*c)*( (a-c)*np.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
        res1=np.sqrt(up/down1)
        res2=np.sqrt(up/down2)
        return np.array([res1, res2])
    
    # def ellipse_angle_of_rotation2( a ): 
    #     b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
    #     if b == 0:
    #         if a > c:
    #             return 0
    #         else:
    #             return np.pi/2
    #     else: 
    #         if a > c:
    #             return np.arctan(2*b/(a-c))/2
    #         else:
    #             return np.pi/2 + np.arctan(2*b/(a-c))/2
    
    
    
    
    # arc = 0.8
    # R = np.arange(0,arc*np.pi, 0.01)
    # x = 1.5*np.cos(R) + 2 + 0.1*np.random.rand(len(R))
    # y = np.sin(R) + 1. + 0.1*np.random.rand(len(R))
    
    a = fitEllipse(x,y)
    center = ellipse_center(a)
    # phi = ellipse_angle_of_rotation(a)
    # phi = ellipse_angle_of_rotation2(a)
    axes = ellipse_axis_length(a)
    
#     print("center = ",  center)
    # print("angle of rotation = ",  phi)
#     print("axes = ", axes)
    print((axes[0]+axes[1])/2)
#     print('\n')
    
    # a, b = axes
    # xx = center[0] + a*np.cos(R)*np.cos(phi) - b*np.sin(R)*np.sin(phi)
    # yy = center[1] + a*np.cos(R)*np.sin(phi) + b*np.sin(R)*np.cos(phi)
    
    #plot
    pylab.plot(x,y,color = 'black',linestyle = 'None', marker = 'o')
    # pylab.plot(xx,yy, color = 'red')
#     pylab.show()
