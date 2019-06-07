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
    
    
    lista_reach = []
    lista_w = []
    for w in np.arange(lowbnd, upbnd, step):
        CI = [x0, 1000, vx0, vy0, w]
        solved = scy.odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I, k_ar,))
        lista_reach.append(solved[:,0][-1])
        lista_w.append(w)
#        plt.plot(solved[:,0], solved[:,1])
#        plt.title('varying w, current = {0}'.format(w))
#        plt.show()
    
    plt.show()
    plt.plot(lista_w, lista_reach)
        
    #plt.title('Alcances')
    plt.xlabel('Velocidade angular (rad/s)')
    plt.ylabel('Alcance (m)')
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
    y0 = 0       #m                                                                                                                   
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
    

WporR(100,1000,1)

HporR(200,2000,5)


