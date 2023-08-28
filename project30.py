import matplotlib.pyplot as plt
import numpy as np
# load images of the digits 0 through 5 and visualize several of them
from sklearn.datasets import load_digits
digits = load_digits(n_class=6)
fig, ax = plt.subplots(8, 8, figsize=(6, 6))
for i, axi in enumerate(ax.flat):
  axi.imshow(digits.images[i], cmap='binary')
axi.set(xticks=[], yticks=[])
plt.show()
