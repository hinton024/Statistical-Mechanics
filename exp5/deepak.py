#!/usr/bin/env python
# coding: utf-8

# In[131]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import quad

k = 1.38*10**(-23)
h = 6.63*10**(-34)
c = 3*10**8

def F_P(x):
    y= (x*x*x)/(np.exp(x)-1) 
    return y

x = np.linspace(0,12,100)
f_P = F_P(x)
y = np.array(f_P)
y_p = max(y[1:])
I = np.where(y == y_p)[0][0]

plt.ylabel(r"$f_P$"),plt.xlabel(r"$x$")
plt.title("Density of states versus frequency")
plt.plot(x, f_P) 
plt.grid()
plt.show()

x_p = x[I]
print("x_p =",x_p)
print("b =",h*c/(k*x_p))
I = quad(F_P,0,np.inf)
print("I_p =",I[0])


# In[129]:


k = 1.38*10**(-23)
h = 6.63*10**(-34)
c = 3*10**8
T = np.linspace(100,10000,21)
c = (8*np.pi*(k**4))/((h*c)**3)
C_T = []
U = []
F = []
for i in T:
    C_t = c*i**4
    C_T.append(c*i**4)
    u = (np.pi**4/15)*(C_t)
    U.append(u)
    F.append((c/4)*u)  
    
plt.plot(T,F)
plt.grid()
plt.show()

plt.loglog(T,F)
plt.grid()
plt.show()
slope,intercepte = np.polyfit(np.log(T),np.log(F),1)
print("slope =" ,slope , "intercepte = ",intercepte)

def F(T):
    f = ((2*np.pi**2*k**4)*T**4)/(15*c**2*h**3)
    return f

f = F(T)
plt.plot(T,F(T))
plt.grid()
plt.show()

