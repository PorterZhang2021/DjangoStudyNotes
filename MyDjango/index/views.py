from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def mydate(request, year):
    return HttpResponse(str(year))


def index(request):
    return render(request, 'index.html')