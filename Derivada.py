# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:48:31 2019

@author: Carlos Dip
"""
#, M_Terra, m, ro, A, Cd
def Derivada(lista, t, r_ar_d, r_ar_m, w, g, m, I, k_w = 0.07):
    
    x = lista[0]              
    y = lista[1]
    vx = lista[2]
    vy = lista[3]
    w = lista [4]
    
    V = (vx**2 + vy**2) ** 0.5
    sena= -vy
    cosa = vx
    
    dwdt = -(k_w * w ** 2)/I
    magx = (r_ar_m * V ** 2 * w * sena)    
    magy = (r_ar_m * V ** 2 * w * cosa)
        

    dxdt = vx
    dydt = vy
    dvxdt = - (r_ar_d * V  * cosa) + magx
    dvydt = -g*m + (r_ar_d * V  * sena) + magy
    dvxdt /= m
    dvydt /= m
    if y <= 0:
        dxdt *= 0.1
        dydt *= 0.1
        dvxdt *= 0.1
        dvydt *= 0.1

    return dxdt, dydt, dvxdt, dvydt, dwdt