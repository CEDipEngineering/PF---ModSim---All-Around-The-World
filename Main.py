

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada

Cm = 0.20
ro = 1
A = (12**2)*np.pi*2
Cd = 0.20 
g = 9.81
m =0.20


r_ar_d = ro*A*Cd/2
r_ar_m = ro*A*Cm/2
##------------Definindo Variáveis-----------#

w = 20
x0 = 200
y0 = 0
Vx0 = 0
Vy0 = 0

Timerange = np.arange(0,1,0.001)
CI = [x0, Vx0, y0, Vy0] 
solved = odeint(Derivada, CI, Timerange, args = (r_ar_d, r_ar_m, w, g, m,))
plt.plot(solved[:,0],solved[:,2])
plt.title('Trajetória')
plt.grid(True)
plt.show()
plt.plot(solved[:,1],solved[:,3])
plt.title('Vx por Vy (Não sei pra que serve)')
plt.grid(True)
plt.show()

nomes = ['X no tempo', 'Vx no tempo', 'Y no tempo', 'Vy no tempo']
for i in range(len(nomes)):
    plt.title(nomes[i])
    plt.plot(Timerange,solved[:,i])
    plt.grid(True)
    plt.show()

