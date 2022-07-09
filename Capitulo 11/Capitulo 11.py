# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 12:48:22 2022

@author: dioni
"""
#librerias
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import t

'Dado un conjunto de datos, crearemos una gráfica de dispersion,'
'minimos cuadrados, y las estimaciones correspondientes'



def datos():
    'Esta esta funcion devuelve los datos de x y, por lo cual se debe usar'
    'como x,y=datos()'
    print('Introducimos los datos, se separan los datos unicamente por un espacio')
    y=np.array(list(map(float, input('''Elementos variable dependiente: 
''').strip().split())))
    x=np.array(list(map(float, input('''Elementos variable independiente: 
''').strip().split())))
    return(x,y)

def regresionLineal(x,y):
    res = stats.linregress(x, y)
    b0=res.intercept
    b1=res.slope
    return(b0,b1)

def varianzasS(x,y):
    sxx,syy,sxy=0,0,0
    res = stats.linregress(x, y)
    for i in range(len(x)):
        syy=(y[i]-y.mean())**2+syy
        sxx=(x[i]-x.mean())**2+sxx
        sxy=(y[i]-y.mean())*(x[i]-x.mean())+sxy
    ss=(syy-res.slope*sxy)/(len(x)-2)
    return(sxx,syy,sxy,ss)

def intervaloB1(b1,alfa,ss,sxx,x):
    t_alfa=t.isf(alfa/2,(len(x)-2))
    valor=t_alfa*np.sqrt(ss/sxx)
    b_lower,b_upper=b1-valor,b1+valor
    print('Los limites inferior y superior de \u03B2_1	son')
    print(f'{b_lower}  <   \u03B2_1	 < {b_upper}')
    return(b_lower,b_upper)

def respuestaMedia(x0,b0,b1,alfa,ss,sxx,x):
    t_alfa=t.isf(alfa/2,(len(x)-2))
    raiz=np.sqrt(ss)*np.sqrt((1/len(x))+(x0-x.mean())**2/sxx)
    y0=b0+b1*x0
    mu_lower,mu_upper=y0-t_alfa*raiz,y0+t_alfa*raiz
    return(mu_lower,mu_upper)

def prediccionIntervalo(x0,b0,b1,alfa,ss,sxx,x):
    t_alfa=t.isf(alfa/2,(len(x)-2))
    raiz=np.sqrt(ss)*np.sqrt(1+(1/len(x))+(x0-x.mean())**2/sxx)
    y0=b0+b1*x0
    mu1_lower,mu1_upper=y0-t_alfa*raiz,y0+t_alfa*raiz
    return(mu1_lower,mu1_upper)

x=np.array([3,7,11,15,18,27,29,30,30,31,31,32,33,33,34,36,36,
            36,37,38,39,39,39,40,41,42,42,43,44,45,46,47,50])
y=np.array([5,11,21,16,16,28,27,25,35,30,40,32,34,32,34,37,38,
            34,36,38,37,36,45,39,41,40,44,37,44,46,46,49,51])

sxx,syy,sxy,ss=varianzasS(x,y)
b0,b1=regresionLineal(x, y)
b1_lower,b1_upper = intervaloB1(b1, 0.05, ss, sxx,x)
x1,y1=respuestaMedia(x,b0,b1,0.05,ss,sxx,x)
x2,y2=prediccionIntervalo(x,b0,b1,0.05,ss,sxx,x)
fig, ax = plt.subplots()
ax.scatter(x, y,label='Puntos')
ax.plot(x,b0+b1*x,'r-',label='Minimos cuadrados')
#ax.plot(x,x1,x,y1)

ax.fill_between(x, x1,y1 ,alpha=0.3,
                label='''Limites de confianza al 95%
para el valor medio de Y|x''')
ax.fill_between(x, x2,y2 ,alpha=0.2,
                label='''Limites de confianza al 95%
para prediccion del intervalo''')
ax.legend()
