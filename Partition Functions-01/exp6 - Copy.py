import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
def z_(states,energy,T):
    z=[]
    for i in range(len(states)):
        print(states[i],energy[i])
        z_ =states[i]*(np.exp((-energy[i])/(k*T)))
        z.append(z_)
    z_final = sum(z)
    return z_final,z

def graph(xs_1,ys_1,xs_2,ys_2,xlabel,ylabel,label1,label2,title):
    fig,axs=plt.subplots(2,1,figsize=(10,25))
    fig.suptitle(title, fontsize=10)
    ax11,ax12=axs[0],axs[1]
    ax11.plot(xs_1,ys_1,'*', color='green',label=label1)
    ax11.set_ylabel(ylabel),ax11.set_xlabel(xlabel)
    ax12.plot(xs_2,ys_2,'o',color='black',label=label2)
    ax12.set_ylabel(ylabel),ax12.set_xlabel(xlabel)         
    ax11.legend(),ax11.grid(True),ax12.legend(),ax12.grid(True)
    plt.show()



k = 8.617e-5
states=[1,2]
low_Trange= np.linspace(0.1,5000,100)
high_Trange = np.linspace(5000,10**5,100)
energy=[0,1]
n=10**5
z_final,z=z_(states,energy,low_Trange)
z_final1,z1=z_(states,energy,high_Trange)

# plt.scatter(low_Trange,z_final)
# plt.xlabel("T")
# plt.ylabel("z")
# plt.title("Low Temperature")
# plt.grid()
# plt.legend()
# plt.show()


for i in range(len(energy)):
    plt.scatter(low_Trange,z[i]/z_final,label="state = {}".format(i+1))
plt.xlabel("T")
plt.ylabel(r"$N_{j}/N$")
plt.title("Low Temperature")
plt.grid()
plt.legend()
plt.show()

U_=[]
for i in range(len(states)):
    U_.append(energy[i]*(z[i]/z_final))
U=sum(U_)
plt.scatter(low_Trange,U)
plt.xlabel("T")
plt.ylabel("U/N")
plt.title("Low Temperature")
plt.grid()
plt.legend()
plt.show()

s= n*k*np.log(z_final/n) + (U/low_Trange) + n*k
plt.scatter(low_Trange,s)
plt.title("Entropy(Low Temperature)")
plt.xlabel("T")
plt.ylabel("s")
plt.legend()
plt.show()

F = -n*k*low_Trange*(np.log(z_final))
plt.scatter(low_Trange,F)
plt.title("Gibbs Free Energy(Low Temperature)")
plt.xlabel("T")
plt.ylabel("F")
plt.legend()
plt.show()

slope=linregress(U,s)[0]
print(slope)
plt.scatter(U,s)
# plt.title("Gibbs Free Energy(High Temperature)")
# plt.xlabel("T")
# plt.ylabel("F")
plt.grid()
plt.legend()
plt.show()

# z_final1,z1=z_(states,energy,high_Trange)
# plt.scatter(high_Trange,z_final1)
# plt.xlabel("T")
# plt.ylabel("z")
# plt.title("High Temperature")
# plt.grid()
# plt.legend()
# plt.show()

graph(low_Trange,z_final,high_Trange,z_final1,"T","z","Low Temperature","High Temperature","z vs T")



for i in range(len(energy)):
    plt.scatter(high_Trange,z1[i]/z_final1,label="state = {}".format(i+1))
plt.xlabel("T")
plt.ylabel(r"$N_{j}/N$")
plt.title("High Temperature")
plt.grid()
plt.legend()
plt.show()

U_=[]
for i in range(len(states)):
    U_.append(energy[i]*(z1[i]/z_final1))
U=sum(U_)
plt.scatter(high_Trange,U)
plt.xlabel("T")
plt.ylabel("U/N")
plt.grid()
plt.show()


s= n*k*np.log(z_final1/n) + (U/high_Trange) + n*k
plt.scatter(high_Trange,s)
plt.title("Entropy(High Temperature)")
plt.xlabel("T")
plt.ylabel("s")
plt.grid()
plt.legend()
plt.show()

F = -n*k*high_Trange*(np.log(z_final1))
plt.scatter(high_Trange,F)
plt.title("Gibbs Free Energy(High Temperature)")
plt.xlabel("T")
plt.ylabel("F")
plt.grid()
plt.legend()
plt.show()

slope=linregress(U,s)[0]
print(slope)

plt.scatter(U,s)
# plt.title("Gibbs Free Energy(High Temperature)")
# plt.xlabel("T")
# plt.ylabel("F")
plt.grid()
plt.legend()
plt.show()


