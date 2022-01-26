from django.shortcuts import render
from django.http import HttpResponse
import os


def upload(request):
    # 请求方法为POST时，执行文件上传
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，就默认为None
        myFile = request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("no files for upload!")
        # 打开特定的文件进行二进制的写操作
        # 建立对应的文件夹 否则报错
        f = open(os.path.join("D:\\upload", myFile.name), 'wb+')
        # 分块写入文件
        for chunk in myFile.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse("upload over!")
    else:
        # 请求方法为GET时，生成文件上传页面
        return render(request, 'upload.html')



