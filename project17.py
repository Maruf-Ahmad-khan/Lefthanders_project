# simple line plot
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0,10,1000)
ax.plot(x, np.sin(x), color = 'red')
ax.plot(x,np.cos(x), color = 'blue')
ax.plot(x,x+1, linestyle = 'solid')
ax.plot(x, x+2, linestyle = 'dashed')
ax.plot(x, x+3, linestyle = 'dashdot')
ax.plot(x,x+4, linestyle=':')
plt.title("Sin and dotted graph", fontsize = 30, color = 'blue')
plt.ylabel("y-axis", fontsize = 30, color = 'blue')
plt.xlabel("x-axis", fontsize = 30, color = 'blue')
plt.show()