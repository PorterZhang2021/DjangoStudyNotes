from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def myDate(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))