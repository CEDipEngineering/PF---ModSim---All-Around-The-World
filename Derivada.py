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

    print(X)
    print(Y)
    print(Vx)
    print(Vy)
    
     
    dX = Vx
    dY = Vy
    D = (X**2+Y**2)**0.5
    P = G*M_Terra*m/D**2
    V = (Vy**2 + Vx**2)**0.5
    R_ar = (ro*A*Cd*V**2)/2
    senP = Y / D
    cosP = X / D
    senAr = Vy / V
    cosAr = Vx / V
    dVx = -P*senP -R_ar*senAr
    dVy = -P*cosP + R_ar*cosAr
    
    
    
    
    return dX, dVx, dY, dVy