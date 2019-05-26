

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada


##------------Definindo Variáveis-----------#
R_terra = 6371000
M_Terra = 5.972e24
G = np.float64(0.0000000000667408)
Cd = 1.5
ro = 1
m = 1
A = 0.01

#-------------Redefinindo unidades para variáveis------#


M_Terra = 6             #Unidade em Yg ou Yottagramas (--> (10**24)g ou (10**21)Kg)
R_terra = 6.371         #Unidade em Gm ou Megametro (--> (10**6)m)
print(G)
##------------Função que calcula derivadas-----------#

x0 = 12
y0 = 0
#V0 = 100
#Angulo = 0
#Vx0 = V0 * np.sin(Angulo)
#Vy0 = V0 * np.cos(Angulo)
Vx0 = 100
Vy0 = 0

Timerange = np.arange(0,100,0.1)
CI = [x0, Vx0, y0, Vy0] 
solved = odeint(Derivada, CI, Timerange, args = (G, M_Terra, m, ro, A, Cd,))
plt.axis([-R_terra*1.1,R_terra*1.1,-R_terra*1.1,R_terra*1.1])
plt.plot(solved[:,0],solved[:,2])
plt.title('X por Y')
plt.grid(True)
plt.show()
plt.plot(solved[:,1],solved[:,3])
plt.title('Vx por Vy')
plt.grid(True)
plt.show()

nomes = ['X no tempo', 'Vx no tempo', 'Y no tempo', 'Vy no tempo']
for i in range(len(nomes)):
    plt.title(nomes[i])
    plt.plot(Timerange,solved[:,i])
    plt.grid(True)
    plt.show()

