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

# [1] 导入项目应用index
# [1] from index.views import index
# 配置媒体文件夹media
from django.views.static import serve
from django.conf import settings

# urlpatterns整个项目的路由集合，以列表格式表示，每个元素代表一条路由信息
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    # [1] path('', index, name='index'),
    # include index app下的路由
    # 配置媒体文件的路由地址
    re_path('media/(?P<path>.*)', serve,
            {'document_root': settings.MEDIA_ROOT}, name='media'),
]
