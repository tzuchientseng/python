from django.http import HttpResponse
from django.shortcuts import render, redirect
from G import G
#大陸用語, 把 views.py 稱為 "視圖"

# Create your views here.
def photo_form(request):
    info=G.saveHistory(request,'準備上傳圖片')
    request.session["currentPage"]="/upload/photo_form"
    if 'userAccount' not in request.session:
        return redirect("/login")

    #位於 upload 目錄的模板，不可以寫成 /upload/.....
    return render(request, "upload/photo_form.html",{"state":"first","info":info[1]})
def photo_process(request):
    info = G.saveHistory(request, '上傳圖片成功')
    #上傳圖片，麻煩的地方
    return render(request, "upload/photo_form.html",{"state":"ok","info":info[1]})
