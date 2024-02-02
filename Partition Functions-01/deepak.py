import numpy as np
import matplotlib.pyplot as plt


def Z(g,E,T):
    L = []
    for j in range(len(E)):
        z = g[j]*np.exp(-E[j]/(k*T))
        L.append(z)
    return sum(L)

k = 8.617*10**(-5)
g = [1,2]
T_low = np.linspace(0.1,5000,50)
T_high = np.linspace(5000,10**5,50)
E = [0,1]
z_low = []
z_high = []
fig ,axs = plt.subplots(2,figsize=(10,10))
for i in T_low:
    z_low.append(Z(g,E,i))
axs[0].scatter(T_low,z_low)
axs[0].title.set_text("At low Temp")
axs[0].set_xlabel("temp")
axs[0].set_ylabel("Z")
axs[0].grid()

for i in T_high:
    z_high.append(Z(g,E,i))
axs[1].scatter(T_high,z_high)
axs[1].title.set_text("At high Temp")
axs[1].set_xlabel("temp")
axs[1].set_ylabel("Z")
axs[1].grid()
plt.show()

###############################################################################################

def N_N(g,Z,E,T):
    N = []
    for i in range(len(T)):
        n = (g*np.exp(-E/(k*T[i])))/Z[i]
        N.append(n)
    return N

N_0_low = []
N_1_low = []
N_0_low.append(N_N(g[0],z_low,E[0],T_low))
N_1_low.append(N_N(g[1],z_low,E[1],T_low))
fig ,axs = plt.subplots(2,figsize=(10,10))
axs[0].scatter(T_low,N_0_low,label = "1st State",c = "darkorange")
axs[0].scatter(T_low,N_1_low,label = "2nd State")
axs[0].title.set_text("At low Temp")
axs[0].set_xlabel("temp")
axs[0].set_ylabel("N_0/N")
axs[0].legend()
axs[0].grid()

N_0_high = []
N_1_high = []
N_0_high.append(N_N(g[0],z_high,E[0],T_high))
N_1_high.append(N_N(g[1],z_high,E[1],T_high))
axs[1].scatter(T_high,N_0_high,label = "1st State",c = "darkorange")
axs[1].scatter(T_high,N_1_high,label = "2nd State")
axs[1].title.set_text("At high Temp")
axs[1].set_xlabel("temp")
axs[1].set_ylabel("N_0/N")
axs[1].legend()
axs[1].grid()
plt.show()
################################################################################################
def U(g,E,Z,T):
    L = []
    for j in range(len(E)):
        u = (g[j]*E[j]*np.exp(-E[j]/(k*T)))/Z
        L.append(u)
    return sum(L)

U_low = []
U_high = []
fig ,axs = plt.subplots(2,figsize=(10,10))
for i in range(len(T_low)):
    U_low.append(U(g,E,z_low[i],T_low[i]))
axs[0].scatter(T_low,U_low)
axs[0].title.set_text("At low Temp")
axs[0].set_xlabel("temp")
axs[0].set_ylabel("U/N")
axs[0].grid()

for i in range(len(T_high)):
    U_high.append(U(g,E,z_high[i],T_high[i]))
axs[1].scatter(T_high,U_high)
axs[1].title.set_text("At high Temp")
axs[1].set_xlabel("temp")
axs[1].set_ylabel("U/N")
axs[1].grid()
plt.show()

#################################################################################################
def S(Z,U,T,N):
    S_S = []
    for i in range(len(T)):
        s = N*k*np.log(Z[i]/N)+(U[i]*N)/T[i]+N*k
        S_S.append(s)
    return S_S

N = 10**(5)
S_low = S(z_low,U_low,T_low,N)
S_high = S(z_high,U_high,T_high,N)

fig ,axs = plt.subplots(2,figsize=(10,10))
axs[0].scatter(T_low,S_low)
axs[0].title.set_text("At low Temp")
axs[0].set_xlabel("temp")
axs[0].set_ylabel("S")
axs[0].grid()

axs[1].scatter(T_high,S_high)
axs[1].title.set_text("At high Temp")
axs[1].set_xlabel("temp")
axs[1].set_ylabel("S")
axs[1].grid()
plt.show()  
#####################################################################
F_low = -N*k*T_low*np.log(z_low)
F_high = -N*k*T_high*np.log(z_high)
fig ,axs = plt.subplots(2,figsize=(10,10))
axs[0].scatter(T_low,F_low)
axs[0].title.set_text("At low Temp")
axs[0].set_xlabel("temp")
axs[0].set_ylabel("F")
axs[0].grid()

axs[1].scatter(T_high,F_high)
axs[1].title.set_text("At high Temp")
axs[1].set_xlabel("temp")
axs[1].set_ylabel("F")
axs[1].grid()
plt.show()  


plt.scatter(U_low,S_low,c = "r",label = "low temp")
plt.scatter(U_high,S_high,c = "g",label = "High temp")
plt.xlabel("U")
plt.ylabel("S")
plt.grid()
plt.legend()
plt.show()
