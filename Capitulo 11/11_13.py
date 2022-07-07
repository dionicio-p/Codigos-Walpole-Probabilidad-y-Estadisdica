# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:22:18 2022

@author: dionicio
"""

import numpy as np
import matplotlib.pyplot as plt

#datos
x=np.array([4.3,4.5,5.9,5.6,6.1,5.2,3.8,2.1,7.5])
suma_x=np.sum(x)

y=np.array([126,121,116,118,114,118,132,141,108])
suma_y=np.sum(y)

suma_xy=0

for i in range(9):
    suma_xy=x[i]*y[i]+suma_xy
    
suma_x2=0
for i in range(9):
    suma_x2=x[i]**2+suma_x2
    
b1=(9*suma_xy-suma_x*suma_y)/(9*suma_x2-suma_x**2)
b0=(suma_y-b1*suma_x)/9

print(f'''
suma x = {suma_x}
suma y = {suma_xy}
suma xy = {suma_xy}
suma x**2 = {suma_x2}
valor b0 = {b0}
valor b1 = {b1}''')
#grafica
fig, ax = plt.subplots()
ax.scatter(x, y,label='Puntos')
ax.plot(x,b0+b1*x,'g-.',label='Regresión Lineal')

ax.legend()

plt.show