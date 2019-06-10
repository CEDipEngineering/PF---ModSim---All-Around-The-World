# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:48:31 2019

@author: Carlos Dip
"""
#, M_Terra, m, ro, A, Cd
def Derivada(lista, t, r_ar_d, r_ar_m, w, g, m, k_w = 0.411):
    
    x = lista[0]              
    y = lista[1]
    vx = lista[2]
    vy = lista[3]
    w = lista [4]
    
    V = (vx**2 + vy**2) ** 0.5
    sena= -vy  # Seria -Vy/V, mas o V foi dividido nas linhas onde o sen e cos aparecem, 
    cosa = vx  # com intuito de evitar divisões por zero.
    
#    Fm = r_ar_m * w * V
    
    dwdt = -(k_w * w)
    magx = (r_ar_m * w * sena)  # Haveria um fator V, contudo, sen seria dividido por V,
    magy = (r_ar_m * w * cosa)  # então simplificou-se como constante*w*sen/cos
        

    dxdt = vx
    dydt = vy
    dvxdt = - (r_ar_d * V  * cosa) + magx
    dvydt = -g*m + (r_ar_d * V  * sena) + magy
    dvxdt /= m
    dvydt /= m

    return dxdt, dydt, dvxdt, dvydt, dwdt