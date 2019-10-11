import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # 尝试根据这些数字绘制出有意义的图形

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)  # z第一个参数：指定的实参将影响x轴和y轴上的刻度


plt.show()  # 打开matplotlib查看器，并显示绘制图形
