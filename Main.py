import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada


r = 3.64e-2                
Cm = 0.33  #Adimensiona
ro = 1.23     #Kg/m3
A = (r**2)*3.14   #m2
Cd = 0.35   #Adimensional
g = 9.81   #m/s2
m = 0.145   #Kg
I = 2/3 * m * r ** 2 

r_ar_d = ro*A*Cd/2
r_ar_m = ro*A*Cm/2

 
tmax = 100
deltat = 1e-3
lista_tempo = np.arange(0, tmax, deltat)



#-----------------------#
#--Condições Iniciais:--#

x0 = 0    #m
y0 = 0.91       #m                                                                                                                   
vx0 = 44.7 * np.cos(np.pi/6)    #m/s
vy0 = 44.7 * np.sin(np.pi/6)    #m/s
w = 0    #rad/s                                                                                                          
                                                                                                                          
CI = [x0, y0, vx0, vy0, w]


#----------------------#
                                                                                                                          
for k_ar in np.arange(0.01,0.1,0.01):                                                                                                                                                               
    solucao_ar = odeint(Derivada, CI, lista_tempo, args = (r_ar_d, r_ar_m, w, g, m, I, k_ar,))
    print(solucao_ar[:,0][-1], k_ar)
                                                                                                                              
    plt.plot(solucao_ar[:,0], solucao_ar[:,1])
    plt.title('Queda Livre {0}'.format(k_ar))
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.grid(True)                                                                                                                          
    plt.show()
