# start to learn from here
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,100)
fig = plt.figure()
plt.title("logrithmic,tangent,cosine and sine graph", color='green',fontsize=20)
plt.ylabel("y-axis",color='red',fontsize=20)
plt.xlabel("x-axis",color='red',fontsize=20)
plt.plot(x,np.log(x),'--',color='red')
plt.plot(x,np.tan(x), '-',color = 'blue')
plt.plot(x,np.cos(x), '-',color = 'green')
plt.plot(x,np.sin(x), '-',color = 'violet')
plt.show()