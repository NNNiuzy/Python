"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 登陆页面
    # 鉴于我们没有编写自己的视图函数，我们传递了一个字典，告诉Django去哪里查找我们将编写的模板。
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    # 注销
    url(r'^logout/$', views.logout_view, name='logout'),
    # 注册页面
    url(r'^register/$', views.register, name='register')
]
