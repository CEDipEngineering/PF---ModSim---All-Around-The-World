# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:48:31 2019

@author: Carlos Dip
"""

def Derivada(lista, t, G, M_Terra, m, ro, A, Cd):
    X = lista[0]
    Y = lista[1]
    Vx = lista[2]
    Vy = lista[3]   
     
    
    D = (X**2+Y**2)**0.5
#    V = (Vy**2 + Vx**2)**0.5
#    R_ar = (ro*A*Cd*V**2)/2
#    R_ar = 0
#    senAr = Vy / V
#    cosAr = Vx / V
    dX = Vx
    dY = Vy
    dVx = -G*M_Terra*X/(D**(3/2)) # -R_ar*senAr
    dVy = -G*M_Terra*Y/(D**(3/2)) # + R_ar*cosAr
#    print((dVx,t))
    
    
    
    return dX, dVx, dY, dVy