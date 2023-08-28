# labelling plots
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-whitegrid")
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0,10,1000)
ax.plot(x, np.sin(x), ':r', label = 'sin(x)')
ax.plot(x,np.cos(x), '-.b',label= "cos(x)")
plt.xlim(0,10)
plt.title("sin and cos graph", fontsize = 15, color = 'orange')
plt.ylabel("sin(x) and cos(x)", fontsize = 15, color = 'blue')
plt.xlabel("x", fontsize = 15, color = "blue")
plt.legend()
plt.show()
