import matplotlib.pyplot as plt
import numpy as np
mean = [0,0]
cov = [[1,1],[1,2]]
x,y = np.random.multivariate_normal(mean, cov, 10000).T
plt.hist2d(x,y,bins=30,cmap ='Blues')
cb=plt.colorbar()
cb.set_label('counts in bin')
plt.show()

