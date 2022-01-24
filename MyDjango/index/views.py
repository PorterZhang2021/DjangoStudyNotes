from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
# Create your views here.


def index(request):
    title = {'key': 'Hello MyDjango'}
    content = {'key': 'This is MyDjango'}
    return render(request, 'index.html', locals())
