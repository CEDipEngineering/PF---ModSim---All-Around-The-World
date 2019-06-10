# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 08:36:54 2019

@author: Carlos Dip
"""

## Construindo gráficos conclusivos ##

import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as scy
from Derivada import Derivada


def WporR(lowbnd, upbnd, step):
    
            ## Parâmetros para bola de basquete ##
    r = 8.3e-2                
    Cm = 0.23  #Adimensiona
    ro = 1.23     #Kg/m3
    A = (r**2)*3.14   #m2
    Cd = 0.47   #Adimensional
    g = 9.81   #m/s2
    m = 20   #Kg
    I = 2/3 * m * r ** 2 
    
    r_ar_d = ro*A*Cd/2
    r_ar_m = ro*A*Cm/2
    
    tmax = 120
    deltat = 1e-1
    lista_tempo = np.arange(0, tmax, deltat)
    
    x0 = 0    #m
    y0 = 0       #m                                                                                                                   
    vx0 = 0
    vy0 = 0
    w = 62    #rad/s    
    
    k_ar = 0.089 
    
    for h in range(1000,2001,100):
        lista_reach = []
        lista_w = []
        for w in np.arange(lowbnd, upbnd, step):
            CI = [x0, h, vx0, vy0, w]
            solved = scy.odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I, k_ar,))
            lista_reach.append(solved[:,0][-1])
            lista_w.append(w)

        
        plt.plot(lista_w, lista_reach, label = 'h = {0}m'.format(h))
    plt.title('Alcances')
    plt.xlabel('Velocidade angular (rad/s)')
    plt.ylabel('Alcance (m)')
    plt.legend()
    plt.grid(True)
    plt.xlim((lowbnd + step*2,upbnd))
    plt.savefig('graphwreach.pdf')
    plt.show()    

def HporR(lowbnd, upbnd, step):
    
        ## Parâmetros para bola de basquete ##
    r = 8.3e-2                
    Cm = 0.23  #Adimensiona
    ro = 1.23     #Kg/m3
    A = (r**2)*3.14   #m2
    Cd = 0.47   #Adimensional
    g = 9.81   #m/s2
    m = 20   #Kg
    I = 2/3 * m * r ** 2 
    
    r_ar_d = ro*A*Cd/2
    r_ar_m = ro*A*Cm/2
    
    tmax = 120
    deltat = 1e-1
    lista_tempo = np.arange(0, tmax, deltat)
        
        
    x0 = 0    #m
    y0 = 0       #m  --;;-- É redefinido depois.                                                                                                                 
    vx0 = 0
    vy0 = 0
    w = 150    #rad/s    
    
    k_ar = 0.089 
    
    lista_reach = []
    lista_h = []

    for h in np.arange(lowbnd, upbnd, step):
        CI = [x0, h, vx0, vy0, w]
        solved = scy.odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I, k_ar,))
        lista_reach.append(solved[:,0][-1])
        lista_h.append(h)
    
    plt.plot(lista_h, lista_reach)
        
    plt.title('Alcance(Altura)')
    plt.xlabel('Altura (m)')
    plt.ylabel('Alcance (m)')
    plt.grid(True)
    plt.xlim((lowbnd + step*2,upbnd))
    plt.savefig('graphhreach.pdf')
    plt.show()  
    
    
def trajetoria_w():
    
    r = 8.3e-2                
    Cm = 0.23  #Adimensiona
    ro = 1.23     #Kg/m3
    A = (r**2)*3.14   #m2
    Cd = 0.47   #Adimensional
    g = 9.81   #m/s2
    m = 20   #Kg
    I = 2/3 * m * r ** 2 
    
    r_ar_d = ro*A*Cd/2
    r_ar_m = ro*A*Cm/2
    
    tmax = 120
    deltat = 1e-1
    lista_tempo = np.arange(0, tmax, deltat)
        
        
    x0 = 0    #m
    y0 = 500       #m  --;;-- É redefinido depois.                                                                                                                 
    vx0 = 0
    vy0 = 0
    for w in range(50,501,50):    
        k_ar = 0.12 
        CI = [x0, y0, vx0, vy0, w]    
        solved = scy.odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I, k_ar,))
        plt.plot(solved[:,0],solved[:,1],label = 'w = {0}rad/s'.format(w))    
    plt.title('Trajetória')
    plt.xlabel('Posição em x (m)')
    plt.ylabel('Posição em y (m)')
    plt.grid(True)
    plt.legend()
    plt.savefig('graphtraject.pdf')
    plt.show()      

WporR(100,200,1)

HporR(200,2000,5)

trajetoria_w()

