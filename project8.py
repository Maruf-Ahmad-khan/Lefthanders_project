import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
dataset = {'series': [1, 2, 3, 4, 5], 'series1': [6, 7, 8, 9, 10], 'sereies2': [
    11, 12, 13, 14, 15], 'series3': [16, 17, 18, 19, 20]}
plt.xlabel("x-axis", fontsize=20, color='red')
plt.ylabel("y-axis", fontsize=20, color='Blue')
plt.title("Line chart with pandas", fontsize=20,
              color='green', backgroundcolor='violet')
ax = plt.axes()
ax.set_facecolor("yellow")
data = pd.DataFrame(dataset)
x = np.arange(5)
plt.axis([0, 5, 0, 20])
plt.plot(x, data)
plt.legend(dataset, loc=2)
plt.show()
