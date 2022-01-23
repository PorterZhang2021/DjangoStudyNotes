# index的urls.py设置
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]