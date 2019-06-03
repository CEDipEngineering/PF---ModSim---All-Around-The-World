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
r = 12e-2                
Cm = 0.23  #Adimensiona
ro = 1.23     #Kg/m3
A = (r**2)*3.14   #m2
Cd = 0.47   #Adimensional
g = 9.81   #m/s2
m = 0.6239   #Kg
I = 2/3 * m * r ** 2 

r_ar_d = ro*A*Cd/2
r_ar_m = ro*A*Cm/2

tmax = 120
deltat = 1e-1
lista_tempo = np.arange(0, tmax, deltat)



#-----------------------#
#--Condições Iniciais:--#

x0 = 0    #m
y0 = 0.91       #m                                                                                                                   
vx0 = 44.7 * np.cos(np.pi/6)    #m/s
vy0 = 44.7 * np.sin(np.pi/6)    #m/s
w = 0    #rad/s                                                                                                          
                                                                                                                          

lista_sol = []
lista_w = []


wrange = range(0, 101, 1)
y0range = range(100,501,5)


for w in wrange:
    lista_w.append(w)
    lista_alcances = []
    for y0 in y0range:
        CI = [x0, y0, vx0, vy0, w]
        solved = scy.odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I,))
        lista_alcances.append(solved[:,0][-1])
    lista_sol.append(lista_alcances)

for index,w in enumerate(lista_w):
    if index % 5 == 0: 
        plt.plot(y0range,lista_sol[index], label = 'w = {0}'.format(w))

plt.title('alcance em função da velocidade angular e altura')
plt.xlabel('altura')
plt.ylabel('alcance')
plt.legend()
plt.grid(True)
plt.savefig('graph1.pdf')
plt.figure(figsize=(20,10))




lista_sol = []
lista_w = []


wrange = range(0, 101, 1)
Vx0range = range(0,100,1)
y0 = 250

for w in wrange:
    lista_w.append(w)
    lista_alcances = []
    for Vx0 in Vx0range:
        CI = [x0, y0, Vx0, vy0, w]
        solved = scy.odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I,))
        lista_alcances.append(solved[:,0][-1])
    lista_sol.append(lista_alcances)

for index,w in enumerate(lista_w):
    if index % 5 == 0: 
        plt.plot(Vx0range,lista_sol[index], label = 'w = {0}'.format(w))

plt.title('alcance em função da velocidade angular e linear em x')
plt.xlabel('Velocidade inicial em x')
plt.ylabel('alcance')
plt.legend()
plt.grid(True)
plt.savefig('graph2.pdf')
plt.figure(figsize=(20,10))

















