from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-2,2,0.1)
Y = np.arange(-2,2,0.1)
X,Y = np.meshgrid(X,Y)
def fuc(x,y):
    return (1 - y**5 + x**5)*np.exp(-x**2 - y**2)
ax.plot_surface(X,Y,fuc(X,Y),rstride=1,cstride=1,cmap=plt.cm.hot)
ax.view_init(elev=30,azim=125)
plt.show()