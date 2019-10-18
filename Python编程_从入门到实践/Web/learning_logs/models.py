from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)  # CharField——有字符或文本组成的数据；max_length为预留空间
    date_added = models.DateTimeField(auto_now_add=True)  # DataTimeField——记录日期和时间的数据;参数为自动设置成当前日期和时间
    owner = models.ForeignKey(User)

    def __str__(self):
        """返回模型的字符串"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic)  # 外键，引用了数据库中的另一条记录，这些代码将每个条目关联到特定的主题
    text = models.TextField()  # 这种不需要限制长度
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta存储用于管理模型的额外信息"""
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
