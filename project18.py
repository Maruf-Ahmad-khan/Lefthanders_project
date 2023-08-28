import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-whitegrid")
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0,10,1000)
ax.plot(x,np.sin(x-20), color = "r", linestyle = ':')
plt.xlim(-1,20)
plt.plot(x,np.cos(x),linestyle = '-',color = 'b')
# plt.ylim(1,15)
plt.ylabel("sin(x)", fontsize = 30, color = 'red')
plt.xlabel("x", fontsize = 30, color ='red')
plt.title("Sine graph", fontsize = 30, color = 'blue')
plt.show()