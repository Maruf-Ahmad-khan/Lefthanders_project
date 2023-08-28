# histogram 
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-whitegrid")
data = np.random.randn(1000)
plt.hist(data,bins=30,alpha=0.5,
histtype='stepfilled',color='red',edgecolor='none')
plt.show()