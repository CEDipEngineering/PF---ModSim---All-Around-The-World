

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada


##------------Definindo Variáveis-----------#

x0 = 0
y0 = 0
Vx0 = 0
Vy0 = 0

Timerange = np.arange(0,100,0.1)
CI = [x0, Vx0, y0, Vy0] 
solved = odeint(Derivada, CI, Timerange)
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

