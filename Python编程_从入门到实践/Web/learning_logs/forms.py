from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        # 它告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段。
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # widget是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表
        # widgets可覆盖Django选择的默认小部件
        # 通过让Django使用forms.Textarea，我们定制了字段'text'的输入小部件，将文本区域的宽度设置为80列而不是默认的40列。
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
