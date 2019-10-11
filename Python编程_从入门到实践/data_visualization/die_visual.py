import pygal
from die import Die

# 创建一个D6和一个D10骰子
# die = Die()
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
multiply_result = die_1.num_sides * die_2.num_sides
for value in range(1, multiply_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

# hist.title = "Result of rolling one D6 1000 times."
# hist.title="Result of rolling two D6 1000 times."
hist.title = "Result of rolling a D6 and a D10 50,000 times."
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_labels = list(map(lambda x: str(x), list(range(1,multiply_result+1))))
hist.x_title = "Result"
hist.y_title = "frequency of Result"

hist.add('D6+D10', frequencies)  # 向它传递要给添加的值指定的标签，还有一个列表，其中包含出现在图表中的值
hist.render_to_file('die_visual.svg')

print(results)
print(frequencies)
