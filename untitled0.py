# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:11:29 2019

@author: Carlos Dip
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada
#import json



r = 12e-2                
Cm = 0.23  #Adimensiona
ro = 1.23     #Kg/m3
A = (r**2)*3.14   #m2
Cd = 0.47   #Adimensional
g = 9.81   #m/s2
m = 6.239   #Kg
I = 2/3 * m * r ** 2 

r_ar_d = ro*A*Cd/2
r_ar_m = ro*A*Cm/2

 
tmax = 100
deltat = 1e-3
lista_tempo = np.arange(0, tmax, deltat)



#-----------------------#
#--Condições Iniciais:--#

x0 = 0    #m
y0 = 260       #m                                                                                                                   
vx0 = 0
vy0 = 0
w = 100  #rad/s                                                                                                          
                                                                                                                          
CI = [x0, y0, vx0, vy0, w]


#----------------------#
                                                                                                                          
k_ar = 0.09                                                                                                                                                       
solucao_ar = odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I, k_ar,))
print(solucao_ar[:,0][-1])
                                                                                                                          
plt.plot(solucao_ar[:,0], solucao_ar[:,1], 'r')
plt.title('Queda Livre {0}'.format(k_ar))
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid(True)                                                                                                                          
plt.show()