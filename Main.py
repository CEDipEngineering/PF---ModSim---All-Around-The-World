import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

##------------Definindo Variáveis-----------#
R_Terra = 6371000
M_Terra = 5.972e24
G = 6.674e-11
Cd = 1.5
ro = 1

##------------Função que calcula derivadas-----------#
def Derivada(lista, t, Ar = True):
    X = lista[0]
    Y = lista[1]
    Vx = lista[2]
    Vy = lista[3]        
    V = (Vx**2 + Vy**2)**(1/2)          
    if V != 0 and Ar:
        cosV = - (Vy/V)                  
        senV = Vx/V
    else: 
        cosV = 0
        senV = 0

    dX = Vx
    dY = Vy
    dVx = (1/m) * (r_ar * V * senV)
    dVy = g + (1/m) * (r_ar * V * cosV)
    return dX, dY, dVx, dVy
