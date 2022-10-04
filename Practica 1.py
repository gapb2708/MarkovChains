#!/usr/bin/env python
# coding: utf-8

# In[2]:


import quantecon as qe
import numpy as np


# In[3]:


#b)
def stationary(p1,p2,s1,s2,f1,f2,t):
    P=np.array([[p1, s1, 1-p1-s1],
     [s2, p2, 1-p2-s2],
     [f1, f2, 1-f1-f2]])
    pt=np.linalg.matrix_power(P,t)
    return print("la probabilidad de conseguir empleo estando desempleado en "+
                 str(t)+" meses es "+str(round(pt[2,0],2)))
stationary(0.9,0.8,0.09,0.19,0.1,0.05,12)


# In[4]:


#c)
def stationary(p1,p2,s1,s2,f1,f2):
    P=np.array([[p1, s1, 1-p1-s1],
     [s2, p2, 1-p2-s2],
     [f1, f2, 1-f1-f2]])
    pstat=qe.MarkovChain(P).stationary_distributions
    return print("la tasa de desempleo de largo plazo es "+ str(round(pstat[0,2],2))+ 
                 " y la tasa de empleo informal de largo plazo es "+ str(round(pstat[0,1],2)))
stationary(0.9,0.8,0.09,0.19,0.1,0.05)


# In[5]:


#d)
stationary(0.9,0.84,0.09,0.15,0.1,0.05)
# Vemos que la tasa de empleo informal de largo plazo aumenta 5 pp. Esto debido a que estamos haciendo que la probabilidad 
# de quedarse desempleado aumente /rho2 y al mismo tiempo estamos haciendo menos probable conseguir empleo formal /s2 si 
# una persona esta desempleada. Esto provoca que la probabilidad de ir al sector informal estando desempleado aumente. 
# La tasa de desempleo a largo plazo se mantiene igual


# In[6]:


#e)
def stationary(p1,p2,s1,s2,f1,f2):
    P=np.array([[p1, s1, 1-p1-s1],
     [s2, p2, 1-p2-s2],
     [f1, f2, 1-f1-f2]])
    pstat=qe.MarkovChain(P).stationary_distributions
    return print("la tasa de desempleo de largo plazo es "+ str(round(pstat[0,2],2))+ 
                 " y la tasa de empleo formal de largo plazo es "+ str(round(pstat[0,0],2)))
stationary(0.9,0.8,0.09,0.15,0.1,0.05)
# Vemos que como baja la probabilidad de pasar a ser empleado estando desempleado /s2, esto provocara que la tasa de de 
# desempleo suba 8pp y la caiga la tasa de empleo formal. Tambien es importante acotar que la tasa de empleo informal tambien 
# se ve afectada

