import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada
                
Cm = 0.01
ro = 1
A = (0.05**2)*3.14
Cd = 0.25
g = 9.81
m =2


r_ar_d = ro*A*Cd/2
r_ar_m = ro*A*Cm/2

 
tmax = 100
deltat = 1e-3
lista_tempo = np.arange(0, tmax, deltat)

x0 = 0
y0 = 250                                                                                                                          
vx0 = 0
vy0 = 0    
w = 5                                                                                                           
                                                                                                                          
CI = [x0, y0, vx0, vy0]

                                                                                                                          
                                                                                                                                                                  
solucao_ar = odeint(Derivada, CI, lista_tempo, args = (r_ar_d,r_ar_m, w, g, m,))

                                                                                                                          
plt.plot(solucao_ar[:,0], solucao_ar[:,1])
plt.title('Queda Livre')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid(True)                                                                                                                          
plt.show()
