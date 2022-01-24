# index的urls.py设置
from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    # 添加带有字符类型、整型和slug的路由
    path('<year>/<int:month>/<slug:day>', views.mydate, name='mydate'),
    # 定义首页的路由
    path('', views.index),
    # 设置路由跳转
    path('turnTo', RedirectView.as_view(url='/'), name='turnTo'),
]