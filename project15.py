import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
fig = plt.figure()
# create a plot figure
# create the first of two panels and set current axis
plt.subplot(2, 1, 1)  # (rows, columns, panel number)
plt.plot(x, np.sin(x), color='red')
plt.title("Trigonometric graph with two interfaces", fontsize=20, color='blue')
plt.ylabel("y-axis", fontsize=20, color='blue')
# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), color='orange')
plt.ylabel("y-axis", fontsize=20, color='blue')
plt.xlabel("x-axis", fontsize=20, color='blue')
plt.show()
