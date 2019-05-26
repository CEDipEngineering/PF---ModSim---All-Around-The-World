import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada
##------------Definindo Variáveis-----------#
R_Terra = 6371000
M_Terra = 5.972e24
G = 6.674e-11
Cd = 1.5
ro = 1
m = 1
A = 0.01
r_ar = Cd * A/2
print(G)
print(M_Terra)

##------------Função que calcula derivadas-----------#

x0 = R_Terra + 1
y0 = 0
V0 = 1000
Angulo = 45
Vx0 = V0 * np.sin(Angulo)
Vy0 = V0 * np.cos(Angulo)


Timerange = np.arange(0,0.1,0.01)
CI = [x0, Vx0, y0, Vy0] 
solved = odeint(Derivada, CI, Timerange, args = (G, M_Terra, m, ro, A, Cd,))
plt.plot(solved[:,0],solved[:,1], 'ro')