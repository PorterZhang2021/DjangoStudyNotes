# index的urls.py设置
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.myDate)
]