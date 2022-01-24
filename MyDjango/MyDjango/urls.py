"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 导入内置Admin功能模块
from django.contrib import admin
# 导入Django的路由函数模块
from django.urls import path, re_path, include


# urlpatterns整个项目的路由集合，以列表格式表示，每个元素代表一条路由信息
urlpatterns = [
    path('admin/', admin.site.urls),
    # 使用命名空间namespace
    path('', include(('index.urls', 'index'), namespace='index')),
]

