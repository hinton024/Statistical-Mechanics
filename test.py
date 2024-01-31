import numpy as np
import matplotlib.pyplot as plt

def graph(xs_1,ys_1,xs_2,ys_2,T,title,subtitle1,subtitle2):
    fig,axs=plt.subplots(2,1,figsize=(10,25))
    fig.suptitle(title, fontsize=10)
    ax11,ax12=axs[0],axs[1]
    ax11.plot(xs_1[0],ys_1,'*',color='black',label="T ={}K".format(T[0]));ax11.plot(xs_1[1],ys_1,'*', color='green',label="T ={}K".format(T[1]))
    ax11.plot(xs_1[2],ys_1,'*', color='red',label="T ={}K".format(T[2]));ax11.plot(xs_1[3],ys_1,'*', color='brown',label="T ={}K".format(T[3]))
    ax11.set_ylabel("f(epsilon)"),ax11.set_title(subtitle1)
    ax12.plot(xs_2[0],ys_2,'*',color='black',label="T ={}K".format(T[0]));ax12.plot(xs_2[1],ys_2,'*', color='green',label="T ={}K".format(T[1]))
    ax12.plot(xs_2[2],ys_2,'*', color='red',label="T ={}K".format(T[2]));ax12.plot(xs_2[3],ys_2,'*', color='brown',label="T ={}K".format(T[3]))
    ax12.set_ylabel("f(epsilon)"),ax12.set_xlabel("epsilon"),ax12.set_title(subtitle2)         
    ax11.legend(),ax11.grid(True),ax12.legend(),ax12.grid(True)
    plt.show()

T=[10,100,1000,5000]
k = 8.617*(10**-5);eV=1.6*(10**-19)

def bose_einstien(x,T):
    scale=[];alpha=0
    output=(1/(np.exp(x+alpha)-1))
    for i in T:
        scale.append(x*k*i)
    return scale, output
x1 = np.linspace(0,2,100)
x2 = np.linspace(-2,0,100)
scale1,output1=bose_einstien(x1,T)
scale2,output2=bose_einstien(x2,T)
graph(scale1,output1,scale2,output2,T,"Bose Einstien","epsilon>n","epsilon<n")

def dirac(x,T):
    scale=[]
    for i in T:
        scale.append(x*k*i)
    output=1/(np.exp(x)+1)
    return scale,output
x = np.linspace(0,2,100)
scale1,output1=dirac(x1,T)
scale2,output2=dirac(x2,T)
graph(scale1,output1,scale2,output2,T,"Fermi Dirac","epsilon>n","epsilon<n")
