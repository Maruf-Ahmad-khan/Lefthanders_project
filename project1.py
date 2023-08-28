# line chart with pandas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = {'series1':[1,2,3,4,5],'series2':[6,7,8,9,10],'series3':[11,12,13,14,15]}
plt.xlabel("x-axis",fontsize=14,color='red')
plt.ylabel("y-axis",fontsize=14,color='red')
plt.title("Line Chart with pandas",fontsize=14,color='green',backgroundcolor='pink')
# how to set background color
ax=plt.axes()
ax.set_facecolor("violet")
df = pd.DataFrame(data)
x = np.arange(5)
plt.axis([0,5,0,16])
plt.plot(x,df)
plt.legend(data,loc=2)
plt.show()