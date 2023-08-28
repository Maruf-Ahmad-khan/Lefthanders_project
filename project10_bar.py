# This is an example showing how to control bar color 
# and legend entries using the color and label parameters of bar.
from cProfile import label
from turtle import color, title
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
Fruits = ["Apple", "Banana", "Cherry", "Orange"]
Counts = [20, 30, 100, 55]
bar_label = ["red", "blue", "_red", "orange"]
bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]
ax.bar(Fruits, Counts, label=bar_label, color=bar_colors)
ax.set_ylabel("Fruits supply")
ax.set_title("Fruits supply by kinds and color")
ax.legend(title="Fruits color")
plt.show()
