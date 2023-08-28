# scatter plot
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-whitegrid")
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 30)
y = np.sin(x)
ax.plot(x, y, '-ok', color='black', label='sin(x)')
plt.axis("equal")
plt.title("Sine graph", fontsize=15, color='orange')

plt.ylabel("sin(x)", fontsize=15, color='blue')

plt.xlabel("x", fontsize=15, color='blue')
plt.legend()
plt.show()
