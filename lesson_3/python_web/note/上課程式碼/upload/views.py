import os
import platform
from datetime import datetime

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
    return render(request, "upload/photo_form.html",{"state":"first","info":info[1],"userAccount":G.userAccount(request)})
def photo_process(request):
    if 'userAccount' not in request.session:
        return redirect("/login")    
    info = G.saveHistory(request, '上傳圖片成功')
    #上傳圖片，麻煩的地方
    if platform.system()=="Linux":
        root="/data/upload/primitive"
    else:
        root="d:/upload/primitive"
    #記得更改 settings.py
    #TIME_ZONE = 'Asia/Taipei'
    #在 Windows 下, 不改也沒關係
    #但 Linux 下一定要改，不然會顯示美國時間
    current=datetime.now()
    yyyy=current.strftime("%Y")
    ymd=current.strftime("%Y%m%d")
    path=os.path.join(root, yyyy, ymd)
    if not os.path.exists(path):
        #os.mkdir(path)#不可以使用這個
        #上面的指令，假如只有 d:/upload, 是不能建立 d:/upload/2023/20231109的目錄
        os.makedirs(path)
    img=request.FILES["userFile"]
    fileName=os.path.join(path, str(img))
    with open(fileName, 'wb') as file:
        for data in img.chunks():
            file.write(data)

    return render(request, "upload/photo_form.html",{"state":"ok","info":info[1],"userAccount":G.userAccount(request)})
