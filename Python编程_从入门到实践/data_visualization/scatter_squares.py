import matplotlib.pyplot as plt

# scatter()绘制散点图
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# edgecolors='none'可以删除点的轮廓 c='reb'/(rgb值)设置点的颜色为红色
# 将c设置成一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)  # s设置了绘制图形时使用的点的尺寸

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])

# plt.show()

# 第一个实参指定要以什么样的文件名保存图表；第二个实参指定将图标多余的空白区域裁剪掉
# plt.savefig('squares_plot.png', bbox_inches='tight')
plt.savefig('squares_plot_test.png')
