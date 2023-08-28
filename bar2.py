from cProfile import label
from turtle import color, width


import numpy as np
import matplotlib.pyplot as plt
N = 5
menMeans = (20,40,35,30,-27)
womenMeans = (25,35, 38, 40 ,-25)
menstd = (1,2,3,4,5)
womenstd = (1,2,3,4,6)
ind = np.arange(N)
width = 0.35
fig, ax = plt.subplots()
p1 = ax.bar(ind, menMeans, width, yerr = menstd, label = 'Men')
p2 = ax.bar(ind, womenMeans, width,bottom = menMeans, yerr = womenstd, label = 'Women')
ax.axhline(0, color='grey',linewidth=0.8)
ax.set_ylabel("Scores")
ax.set_title("Scores by group and gender")
ax.set_xticks(ind, label=['G1','G2','G3','G4','G5'])
ax.legend()
ax.bar_label(p1,label_type='center')
ax.bar_label(p2,label_type='center')
ax.bar_label(p2)
plt.show()