# index的urls.py设置
from django.urls import path
from . import views

urlpatterns = [
    # 添加带有字符类型、整型和slug的路由
    path('<year>/<int:month>/<slug:day>', views.myVariable),
    # 添加路由地址外的变量month
    path('', views.index, {'month': '2019/10/10'}),
]