import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada
#import json



r = 3.64e-2              
Cm = 0.14  #Adimensiona
ro = 1.23     #Kg/m3
A = (r**2)*3.14   #m2
Cd = 0.44   #Adimensional
g = 9.81   #m/s2
m = 0.150   #Kg
I = 2/5 * m * r ** 2 

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
w = 143   #rad/s                                                                                                          
                                                                                                                          
CI = [x0, y0, vx0, vy0, w]

upbnd = 0.5
lowbnd = 0.07
step = 0.0003
#----------------------#
lista_alcances = []
for i in np.arange(lowbnd, upbnd, step):
    k_ar = i                                                                                                                                                                                                                                                                                
    solucao_ar = odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I, k_ar,))
    print(solucao_ar[:,0][-1], i)
    lista_alcances.append(solucao_ar[:,0][-1])

                                                                                                                      
plt.plot(solucao_ar[:,0], solucao_ar[:,1], 'r')
plt.title('Queda Livre; k_ar =  {0}'.format(k_ar))
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid(True)                                                                                                                          
plt.show()

#plt.plot(solucao_ar[:,0],solucao_ar[:,1])
plt.plot(np.arange(lowbnd, upbnd, step), lista_alcances, 'g')
plt.title('Alcance x K_ar')
plt.xlabel('K_ar')
plt.ylabel('Alcance')
plt.grid(True)       
plt.savefig('K_arReach.pdf')                                                                                                                   
plt.show()

