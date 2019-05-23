import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

##------------Definindo Variáveis-----------#
l0 = 30 * 1e-2
m = 200 * 1e-3
k = 10
g = 10
r = 10 * 1e-2
Cd = 1.5
ro = 1
A = np.pi * r**2
r_ar = ro * Cd * A / 2

##------------Função que calcula derivadas-----------#
def Derivada(lista, t, Ar = True):
    X = lista[0]
    Y = lista[1]
    Vx = lista[2]
    Vy = lista[3]
    l = (Y**2 + X**2) ** (1/2)         
    V = (Vx**2 + Vy**2)**(1/2)          
    cosL = Y/l                       
    senL = X/l
    if V != 0 and Ar:
        cosV = - (Vy/V)                  
        senV = Vx/V
    else: 
        cosV = 0
        senV = 0
    Fel = -k * (l - l0)

    dX = Vx
    dY = Vy
    dVx = (1/m) * (Fel * senL + r_ar * V * senV)
    dVy = g + (1/m) * (Fel * cosL + r_ar * V * cosV)
    return dX, dY, dVx, dVy
