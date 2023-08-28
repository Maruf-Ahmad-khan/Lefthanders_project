# scatter plots
import matplotlib.pyplot as plt
import numpy as np
khan = np.random.RandomState(0)
x = khan.randn(100)
y = khan.randn(100)
colors = khan.rand(100)
sizes = 1000*khan.rand(100)
plt.scatter(x,y,c=colors, s = sizes, alpha=0.3,cmap='viridis')
plt.title("Random bubbles")
plt.xlabel('x')
plt.ylabel('y')
plt.show()