import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

##------------Definindo Variáveis-----------#
R_Terra = 6371000
M_Terra = 5.972e24
G = 6.674e-11
Cd = 1.5
ro = 1
m = 1
A = 0.01
r_ar = Cd * A/2
print(G)
print(M_Terra)

##------------Função que calcula derivadas-----------#

x0 = R_Terra + 1
y0 = 0
V0 = 1000
Angulo = 45
Vx0 = V0 * np.sin(Angulo)
Vy0 = V0 * np.cos(Angulo)

def EqDif(lista,t):
    X = lista[0]
    Y = lista[1]
    Vx = lista[2]
    Vy = lista[3]  

    print(X)
    print(Y)
    print(Vx)
    print(Vy)
    #print(dX)
    #print(dY)
    #print(D)
    #print(P)
    
     
    dX = Vx
    dY = Vy
    D = (X**2+Y**2)**0.5
    P = G*M_Terra*m/D**2
    V = (Vy**2 + Vx**2)**0.5
    R_ar = 1 * r_ar * V**2
    senP = Y / D
    cosP = X / D
    senAr = Vy / V
    cosAr = Vx / V
    dVx = -P*senP -R_ar*senAr
    dVy = -P*cosP + R_ar*cosAr
    
    
    
    
    return dX, dVx, dY, dVy

Timerange = np.arange(0,0.1,0.01)

CI = [x0, Vx0, y0, Vy0] 
solved = odeint(EqDif, CI, Timerange)
plt.plot(solved[:,0],solved[:,1], 'ro')