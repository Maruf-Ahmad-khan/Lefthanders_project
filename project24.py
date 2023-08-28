# DATA VISUALISATION
# using contour function
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-whitegrid")
def f(x,y):
    return np.sin(x)**10+np.cos(10+x*y)*np.cos(x)
x =np.linspace(0,5,50)
y = np.linspace(0,5,40)
X ,Y= np.meshgrid(x,y)
# meshgrid is a function it retruns cordinates 
# of matrices from coordinate vector
Z=f(X,Y)
plt.contourf(X,Y,Z, 20, cmap = 'RdGy')
plt.colorbar()
plt.show()