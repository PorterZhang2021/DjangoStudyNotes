from django.shortcuts import render


# Create your views here.
def index(request):
    value = 'This is test!'
    print(value)
    return render(request, 'index.html')
