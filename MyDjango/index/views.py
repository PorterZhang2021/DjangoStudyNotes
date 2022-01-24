from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
# Create your views here.


def index(request):
    html = '<h1>Hello World</h1>'
    return HttpResponse(html, status=200)
