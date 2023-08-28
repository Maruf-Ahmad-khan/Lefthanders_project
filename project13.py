# basic of data visualisation using sin and cos graph
import numpy as np
import matplotlib.pyplot as plt
y = np.linspace(0, 10, 100)
fig = plt.figure()
plt.title("Trigonometric graph", fontsize=20, color='blue')
plt.ylabel("y-axis", fontsize=20, color='blue')
plt.xlabel("x-axis", fontsize=20, color='blue')
plt.plot(y, np.sin(y), 'r--', label = 'sin(y)')
plt.plot(y, np.cos(y), ':b', label = 'cos(y)')
plt.plot(y, np.tan(y), '-b', label="tan(y)")
plt.plot(y, np.log(y), '-.g', label="log(y)")
plt.legend()
plt.show()
