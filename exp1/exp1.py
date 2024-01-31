import numpy as np 
import random 
import matplotlib.pyplot as plt

No_of_trials = 10
No_of_coins = 2
t=[];res=[];rand_num=[]
grid = np.zeros([No_of_trials,No_of_coins])
for j in range(0,No_of_coins):
    rand_num.append(random.randint(0, 1))
print("random Numbers list",rand_num)
for i in range(1,No_of_trials+1):
    t.append([random.randint(0, 1),random.randint(0, 1)])
    result = res.append([(np.sum(t,0)/np.sum(t)),(np.sum(t,1)/np.sum(t))][0])
    
    #print(res[i-1][1])
print("outcomes ", t)
print("probability",res)
plt.plot(range(1,No_of_trials+1),res)
plt.show()

