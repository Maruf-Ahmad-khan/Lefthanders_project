import matplotlib.pyplot as plt
import numpy as np
# basic error visualisation
plt.style.use("seaborn-whitegrid")
x = np.linspace(0,10,50)
dy = 0.8
y = np.sin(x)*dy+np.random.randn(50)
plt.errorbar(x,y,yerr=dy,fmt='o',color='blue',ecolor='red',elinewidth=3,capsize=0)
plt.title("Basic error visualisation",fontsize=14,color='blue')
plt.ylabel('y-error', color='blue',fontsize=14)
plt.xlabel('x-error', color ='blue',fontsize=14)
plt.show()