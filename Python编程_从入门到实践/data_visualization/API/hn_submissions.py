import requests

from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    reponse_dict = submission_r.json()

    submission_dict = {
        'title': reponse_dict['title'],
        'link': 'http://news.yocmbinator.com/item?id=' + str(submission_id),
        'comments': reponse_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

# itemgetter()，像这个函数传递了键'comments'，因此它将从这个列表的每个字典中提取与键键'comments'相关联的值
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discussion link:', submission_dict['link'])
    print('Comments:', submission_dict['comments'])
