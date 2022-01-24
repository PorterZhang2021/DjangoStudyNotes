from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
# Create your views here.


def index(request):
    value = {'title' : 'Hello MyDjango'}
    return render(request, 'index.html', context=value)
