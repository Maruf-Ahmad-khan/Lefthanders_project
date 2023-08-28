#  Basic error bar
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-whitegrid")
x = np.linspace(0,10,50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x,y, yerr=dy, fmt='.k')
plt.show()
