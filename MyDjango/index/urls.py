# index的urls.py设置
from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    # 定义首页的路由
    path('', views.index, name='index'),
    # 定义商城的路由
    path('shop', views.shop, name='shop')
]