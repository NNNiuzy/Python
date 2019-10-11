# 15_2作业
import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x ** 3 for x in x_values]

plt.title('cube', fontsize=14)
plt.xlabel('x_values', fontsize=14)
plt.ylabel('y_values', fontsize=14)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors=None, s=4)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 5500, 0, 130000000000])

plt.show()
