import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# status_code是状态码，200表示请求成功
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

# print("\nSelected information about each repository:")
names, stars = [], []
for repo_dict in repo_dicts:
    # print('Name:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    # print('Description:', repo_dict['description'])
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18
# 表格式配置文件
my_config = pygal.Config()  # 配置对象
my_config.x_label_rotation = -45  # x轴标签旋转角度
my_config.show_legend = False  # 是否展示图例

# 书中这三行有问题，无论怎么改没有变化;python 2.2.0: move font_size config to style
# my_config.title_font_size = 24  # 图表标题字体大小
# my_config.label_font_size = 14  # 副标签字体大小
# my_config.major_label_font_size = 18  # 主标签字体大小

my_config.truncate_label = 15  # 将裁剪较长字符到15个
my_config.show_y_guides = False  # 是否展示图标中水平线
my_config.width = 1000  # 自定义图表宽度

# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)  # 第二三个实参：让标签绕x轴旋转45度；隐藏了图例
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
# chart.config.style.title_font_size = 24
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

# # 处理结果
# print(response_dict.keys())
