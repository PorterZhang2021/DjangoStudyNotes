# index的urls.py设置
from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    # 定义路由
    path('', views.index, name='index'),
    path('getHeader', views.getHeader, name='getHeader')
]