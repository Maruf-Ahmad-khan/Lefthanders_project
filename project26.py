# using all three function 
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-whitegrid")
def func(x,y):
    return np.sin(x)**10+np.cos(10+x*y)+np.cos(x)
x = np.linspace(0,5,100)
y = np.linspace(0,5,90)
X,Y = np.meshgrid(x,y)
Z = func(X,Y)
var = plt.contour(X,Y,Z,3,colors='black')
plt.clabel(var,inline=True,fontsize=8)
plt.imshow(Z, extent=[0,5,0,5],origin='lower',alpha=0.3,cmap='RdGy')
plt.colorbar()
plt.show()