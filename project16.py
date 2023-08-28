# object oriented interface
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,100)
fig,ax = plt.subplots(2)
ax[0].plot(x, np.cos(x), color='red' )
ax[1].plot(x,np.sin(x), color = 'blue')
plt.show()