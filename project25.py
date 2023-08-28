# contour plots using plt.imshow()
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-whitegrid")
def fun(a,b):
    return np.sin(a)**10+np.cos(10+a*b)+np.cos(a)
a = np.linspace(0,5,60)
b = np.linspace(0,5,50)
A,B = np.meshgrid(a,b)
C = fun(A,B)
plt.imshow(C, extent=[0, 5, 0, 5], origin='lower',
 cmap='RdGy')
plt.colorbar()
plt.show()