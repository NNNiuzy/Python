import csv
from datetime import datetime

import matplotlib.pyplot as plt

# 从文件中获取日期、最高气温和最低气温
# filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # # enumerate()来获取每个元素的索引及其值
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)
    # print(len(highs))

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
# alpha指定颜色的透明度，0表示完全透明，1（默认设置）表示完全不透明
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, lows, highs, facecolor='green', alpha=0.1)

# 设置图形的格式
# plt.title("Daily high and low temperature - 2018", fontsize=24)
plt.title("Daily high and low temperature - 2018\nDeath Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜的日期标签
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
