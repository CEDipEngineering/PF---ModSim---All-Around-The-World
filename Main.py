import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada
#import json



r = 3.64e-2              
Cm = 0.24  #Adimensiona
ro = 1.23     #Kg/m3
A = (r**2)*3.14   #m2
Cd = 0.44   #Adimensional
g = 9.81   #m/s2
m = 0.150   #Kg
I = 200/3 * m * r ** 2 

r_ar_d = ro*A*Cd/2
r_ar_m = ro*A*Cm/2

 
tmax = 10
deltat = 1e-3
lista_tempo = np.arange(0, tmax, deltat)



#-----------------------#
#--Condições Iniciais:--#

x0 = 0    #m
y0 = 0.91       #m                                                                                                                   
vx0 = 50 * np.cos(np.pi/6)    #m/s
vy0 = 50 * np.sin(np.pi/6)    #m/s
w = 134   #rad/s                                                                                                          
                                                                                                                          
CI = [x0, y0, vx0, vy0, w]


#----------------------#
lista_alcances = []
for i in np.arange(0.001, 0.5, 0.001):                                                                                                                       
    k_ar = i                                                                                                                                                           
    solucao_ar = odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I, k_ar,))
    print(solucao_ar[:,0][-1], i)
    if solucao_ar[:,0][-1] == 0:
        solucao_ar[:,0][-1] = None
    lista_alcances.append(solucao_ar[:,0][-1])

                                                                                                                      
plt.plot(solucao_ar[:,0], solucao_ar[:,1], 'r')
plt.title('Queda Livre {0}'.format(k_ar))
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid(True)                                                                                                                          
plt.show()

plt.plot(np.arange(0.001, 0.5, 0.001), lista_alcances, 'g')
plt.title('K_ar x Alcance')
plt.xlabel('K_ar')
plt.ylabel('Alcance')
plt.grid(True)                                                                                                                          
plt.show()

