import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Derivada import Derivada
import csv
#import json

lista_dados_x = []
lista_dados_y = []

'''
O Arquivo valData.csv foi produzido a partir do site https://apps.automeris.io/wpd/
no qual colocamos uma imagem do gráfico do paper http://baseball.physics.illinois.edu/TrackingTechnologiesBaseball.pdf
e produzimos uma lista de pontos em CSV. O código abaixo lê esse arquivo, o transorma em 2 listas
adequadamente formatadas, converte as unidades de pés para metros, e plota
os dados do Paper com nosso modelo num só gráfico.
'''

with open('valData.csv','r') as dados:
    lista = csv.reader(dados)
    for row in lista:
        for i,e in enumerate(row):
            if i%2 == 0:    
                row[i] = float(e)
            else:
                row[i] = float(e)/(10**len(e))
        lista_dados_x.append(row[0]+row[1])
        lista_dados_y.append(row[2]+row[3])



r = 3.64e-2              
Cm = 0.07  #Adimensiona
ro = 1.23     #Kg/m3
A = (r**2)*np.pi   #m2
Cd = 0.36785   #Adimensional
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
vx0 = 50 * np.cos(np.radians(27))    #m/s
vy0 = 50 * np.sin(np.radians(27))    #m/s
w = 134.66   #rad/s                                                                                                          
                                                                                                                          
CI = [x0, y0, vx0, vy0, w]


k_ar = 0.32

solved = odeint(Derivada, CI, lista_tempo,  args = (r_ar_d, r_ar_m, w, g, m, k_ar,))
lista_dados_x_m = [x/3.281 for x in lista_dados_x]
lista_dados_y_m = [y/3.281 for y in lista_dados_y]
plt.plot(solved[:,0],solved[:,1], 'xkcd:cyan', label = 'Modelo')
plt.title('Trajetória em validação')
plt.plot(lista_dados_x_m,lista_dados_y_m, 'g.', label = 'Dados')
plt.xlabel('Alcance (m)')
plt.legend()
plt.ylim((0,max(lista_dados_y_m)+5))
plt.xlim((-1,max(lista_dados_x_m)+5))
plt.grid(True)
plt.ylabel('Altura (m)')
plt.savefig('validation.pdf')
plt.show()


