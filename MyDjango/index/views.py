from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request, month):
    return HttpResponse('这是路由地址之外的变量' + month)


def myVariable(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str('day'))