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



#-----------------------#
#--Condições Iniciais:--#

x0 = 0    #m
y0 = 0       #m                                                                                                                   
vx0 = 0
vy0 = 0
w = 62    #rad/s    

k_ar = 0.089 
#%%
lista_reach = []
lista_w = []
lowbnd = 50
upbnd = 1500
step = 0.5
for w in np.arange(lowbnd, upbnd, step):
    CI = [x0, 1000, vx0, vy0, w]
    solved = scy.odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I,))
    lista_reach.append(solved[:,0][-1])
    lista_w.append(w)

plt.plot(lista_w, lista_reach)
    
#plt.title('Alcances')
plt.xlabel('Velocidade angular (rad/s)')
plt.ylabel('Alcance (m)')
plt.grid(True)
plt.xlim((lowbnd + step*2,upbnd))
plt.savefig('graphwreach.pdf')
plt.show()    

#%%









