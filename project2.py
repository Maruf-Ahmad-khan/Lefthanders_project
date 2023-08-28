from shutil import which
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
x_axis = [1,1001]
y_axis = [x**2 for x in x_axis]
plt.style.use('seaborn')
fix,ax = plt.subplots()
ax.scatter(x_axis, y_axis, c=y_axis,cmap=plt.cm.Blues,linewidth=10)
ax.set_title("Data graph",color='red',fontsize=20)
ax.set_xlabel("X-axis",color='Brown' ,fontsize = 20)
ax.set_ylabel("Y-axis",color='Brown', fontsize = 20)
ax.tick_params(axis='both',which='major',labelsize=20 )
ax.axis([0,1100,0,1100000])
plt.show()

