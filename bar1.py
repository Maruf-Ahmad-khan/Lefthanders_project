#  how to control bar color and legend entries
#  using the color and label parameters of bar.
from cProfile import label
from turtle import color, title
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
Names = ["Umar", "Imran", "Sahil", "Sohaib", "Rehan", "Arshalan"]
Marks = [98, 88, 89, 84, 99, 87]
bar_label = ["red", "blue", "green", "pink", "orange", "red"]
bar_colors = ["tab:red", "tab:blue", "tab:green",
              "tab:pink", "tab:orange", "tab:red"]
ax.bar(Names, Marks, label=bar_label, color=bar_colors)
ax.set_ylabel("Marks",fontsize=20, backgroundcolor="violet")
ax.set_title("Marks of the Students" , fontsize=20, backgroundcolor= "violet")
ax.legend(title="Marks in the same subject")
plt.show()
