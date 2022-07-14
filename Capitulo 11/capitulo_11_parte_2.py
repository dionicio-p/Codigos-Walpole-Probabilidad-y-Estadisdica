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
    
def datos():
    'Esta esta funcion devuelve los datos de x y, por lo cual se debe usar'
    'como x,y=datos()'
    print('Introducimos los datos, se separan los datos unicamente por un espacio')
    y=np.array(list(map(float, input('''Elementos variable dependiente: 
''').strip().split())))
    x=np.array(list(map(float, input('''Elementos variable independiente: 
''').strip().split())))
    return(x,y)


if __name__ == "__main__":
    print('Dado un conjunto de datos, se hallara el valor de r que nos indica el porcentaje',
          ' de correlación entre X y Y, para despues realizar una prueba tipo t',
          ' para ver que probabilidad hay de que rho = 0, y finalmente una para ver',
          'que probabilidad de que rho = 0.9')
    x,y=datos()
    sxx,syy,sxy,ss=varianzasS(x,y)
    b0,b1=regresionLineal(x,y)
    r1=r(b1,sxx,syy)
    correlacion(b1,sxx,syy)
    pruebaT_correlacion_rho0(0.05, 29, r1)
    prueba_z_para_rho(0.9, 0.05, r1, 29)
