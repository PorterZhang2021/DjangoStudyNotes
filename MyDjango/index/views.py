from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
# Create your views here.


def mydate(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))


def index(request):
    print(reverse('index:turnTo'))
    return redirect(reverse('index:mydate', args=[2019, 12,  12]))