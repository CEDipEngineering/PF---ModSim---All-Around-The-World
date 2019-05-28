# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:48:31 2019

@author: Carlos Dip
"""
#, M_Terra, m, ro, A, Cd
def Derivada(lista, t, r_ar_d, r_ar_m, w, g, m):
    X = lista[0]
    Y = lista[1]
    Vx = lista[2]
    Vy = lista[3]   

    dX = Vx
    dY = Vy
    
    V = (Vx**2 + Vy**2) ** 0.5
    if V != 0:
        cosV = Vx/V
        senV = Vy/V
    else:
        cosV = 0
        senV = 0
    print(Vx, Vy, X, Y, t)
    r_ar_d = 0
    r_ar_m = 0
        
    dVx = 0#(1/m) * (r_ar_m*(V**2)*w*V*senV - r_ar_d*(V)*cosV)
    dVy = (1/m) * (r_ar_m*(V**2)*w*V*cosV + r_ar_d*(V)*senV) - g
#    print(dVx, dVy, t)
    return dX, dVx, dY, dVy