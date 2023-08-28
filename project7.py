from unittest.mock import patch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
mu,sigma = 100,15
x= mu+sigma*np.random.randn(10000)
n,bins,patches=plt.hist(x,50,density=True,facecolor='g',alpha=0.75)
plt.xlabel("Smart")
plt.ylabel("Probablity")
plt.title("Histogram of IQ")
plt.text(60,.025,r'$\mu=100, \ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()