# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 19:30:00 2022

@author: dioni
"""

'Correlacion entre X y Y'

import numpy as np
import scipy as sc
from scipy import stats

def varianzasS(x,y):
    sxx,syy,sxy=0,0,0
    res = stats.linregress(x, y)
    for i in range(len(x)):
        syy=(y[i]-y.mean())**2+syy
        sxx=(x[i]-x.mean())**2+sxx
        sxy=(y[i]-y.mean())*(x[i]-x.mean())+sxy
    ss=(syy-res.slope*sxy)/(len(x)-2)
    return(sxx,syy,sxy,ss)

def regresionLineal(x,y):
    res = stats.linregress(x, y)
    b0=res.intercept
    b1=res.slope
    return(b0,b1)

def r(b1,sxx,syy):
    funcion= b1*np.sqrt(sxx/syy)
    return(funcion)

def correlacion(b1,sxx,syy):
    corr=(r(b1,sxx,syy))**2
    corr1=round(corr*100,1)
    print(f'Aproximandamente el {corr1}% de la variacion de los valores de Y es causada por X')
    return(corr1)

def pruebaT_correlacion_rho0(alfa,df,r):
    t=stats.t.isf(alfa/2,df-2)
    t=round(t,3)
    prueba=(r*np.sqrt(df-2))/np.sqrt(1-r**2)
    prueba=round(prueba,3)
    if t > -prueba:
        a='Hipotesis rechaza, \u03C1 != 0 '
    elif t < prueba:
        a='Hipotesis rechaza, \u03C1 != 0 '
    else:
        a='No existe evidencia concreta para rechazar la hipotesis nula'
    print('El intervalo de la prueba es')
    print(f'-{t} < t < {t}')
    print(f'El valor de t para la prueba fue: {prueba}')
    print(a)


def prueba_z_para_rho(rho,alfa,r1,df):
    z=stats.norm.isf(alfa)
    prueba=(np.sqrt(df-3)/2)*np.log(((1+r1)*(1-rho))/((1-r1)*(1+rho)))
    prueba=round(prueba,3)
    if z < prueba:
        a='Hipotesis nula rechazada'
    else:
        a='No existe evidencia concreta para rechazar la hipotesis nula'
    
    print(f'\nHipotesis nula: \u03C1={rho}')
    print(f'Hipotesis alternativa: \u03C1>{rho}')
    print('Para esta prueba el punto critico esta en')
    print(f'z > {z}')
    print(f'El valor de z para la prueba fue: {prueba}')
    print(a)
    
    
x=np.array([0.414,0.383,0.399,0.402,0.442,0.422,0.466,0.500,0.514,
            0.530,0.569,0.558,0.577,0.572,0.548,0.581,0.557,0.550,
            0.531,0.550,0.556,0.523,0.602,0.569,0.544,0.557,0.530,
            0.547,0.585])
y=np.array([29186,29266,26215,30162,38867,37831,44576,46097,59698,
            67705,66088,78468,89869,77369,67095,85156,69571,84160,
            73466,78610,67657,74017,87291,86836,82540,81699,82096,
            75657,80490])


sxx,syy,sxy,ss=varianzasS(x,y)
b0,b1=regresionLineal(x,y)
r1=r(b1,sxx,syy)
correlacion(b1,sxx,syy)
pruebaT_correlacion_rho0(0.05, 29, r1)
prueba_z_para_rho(0.9, 0.05, r1, 29)