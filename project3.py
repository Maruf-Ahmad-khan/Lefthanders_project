from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
fix,ax=plt.subplots()
ax.set_title("Data visualization",color='red' ,fontsize=20)
ax.set_xlabel("x-axis",color='Blue', fontsize=20)
ax.set_ylabel("y-axis",color='Blue',fontsize=20)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()