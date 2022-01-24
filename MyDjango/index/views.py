from django.shortcuts import render
from django.http import Http404


def page_not_found(request, exception):
    """全局404的配置函数"""
    return render(request, '404.html', status=404)


def page_error(request):
    """全局500的配置函数"""
    return render(request, '500.html', status=500)


def index(request):
    # request.GET是获取请求
    if request.GET.get('error', ''):
        raise Http404("page does not exist")
    else:
        return render(request, 'index.html')
