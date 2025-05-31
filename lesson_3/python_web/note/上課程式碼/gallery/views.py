import base64
import json
import math
import os
import platform
from PIL import ImageFile, Image, ImageFont, ImageDraw
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from G import G
import numpy as np
import cv2

"""
建立縮圖時，如果圖片很多，要好幾10分鐘，網頁就會出現連線 timeout 的錯誤
需更改 nginx.conf的 http區塊
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
	client_max_body_size 100m;
    proxy_connect_timeout   10000;
    proxy_send_timeout      15000;
    proxy_read_timeout      20000;
    server{
    ........
    }
}

專案方案
1. 外包 : 不用養程式設計師，但價格貴，維護慢，需定期付維護費用
2. 專職程式設計師 : 每月支付薪水，專案隨時新增調整，維護較快
"""
#tree=""
thumb_path=""
primitive_path=""
def html(request):
    global thumb_path, primitive_path
    if platform.system()=="Linux":
        primitive_path="/data/upload/primitive"
        thumb_path="/data/upload/thumb"
    else:
        primitive_path="d:/upload/primitive"
        thumb_path="d:/upload/thumb"

    info=G.saveHistory(request,'gallery')
    request.session["currentPage"]="/gallery"
    if 'userAccount' not in request.session:
        return redirect("/login")
    if platform.system()=="Linux":
        thumb_path="/data/upload/thumb/"
    else:
        thumb_path = "d:/upload/thumb/"
    #root=os.listdir(thumb_path)
    #root.sort(reverse=True)

    tree=""
    tree=listDir(thumb_path, tree)
    return render(
        request,
        "gallery/gallery.html",
        {"list_dir":mark_safe(tree),"info":info[1],"userAccount":G.userAccount(request)})

def listDir(path, tree):
    tree +="<ul>"
    files=os.listdir(path)
    files.sort(reverse=True)
    for file in files:
        full=os.path.join(path, file).replace("\\","/")
        if os.path.isdir(full):
            txt=full.replace(path,"").replace("/","")
            url=full.replace(thumb_path,"")
            tree += f"""
                <li>
                    <a href='javascript:void(0)' onclick='loadThumb("{url}");'>
                        {txt}
                    </a>
                </li>
            """
            tree=listDir(full, tree)
    tree +="</ul>"
    return tree
def thumb(request):
    info=G.saveHistory(request,'準備製作縮圖')
    request.session["currentPage"]="/gallery/thumb"
    if 'userAccount' not in request.session:
        return redirect("/login")
    return render(request, "gallery/thumb.html",
                  {"info":info[1],"userAccount":G.userAccount(request)}
                  )
def thumb_doing(request):
    if not os.path.exists(thumb_path):
        os.makedirs(thumb_path)
    primitive=dirTree(primitive_path)
    thumb=dirTree(thumb_path)

    #pip install Pillow
    #底下設定是解決圖片太大出現 "exceeds limit of 178956970 pixels, could be decompression" 的例外
    ImageFile.LOAD_TRUNCATED_IMAGES=True
    Image.MAX_IMAGE_PIXELS=None

    #primitive : "d:/upload/primitive/2003/20231109/1.jpg"
    #thumb     :"d:/upload/thumb/2003/20231109/1.jpg"
    #底下那一張圖會被先製作，不知道，因為 set 是無序的
    for p in primitive:
        if not p.replace('primitive','thumb') in thumb:
            target=ext2lower(p)#將副檔名改成小寫，不然在 Linux 下載時，jpg 會變成 jiff
            make_thumb(target)
    info=G.saveHistory(request,'縮圖製作完成')
    return render(request, "gallery/gallery.html",
                  {"info":info[1],"userAccount":G.userAccount(request)}
                  )
def make_thumb(file):
    thumb_dir=os.path.dirname(file).replace("primitive","thumb")
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)
    #使用 Pillow 會比 cv2 快很多
    pil=Image.open(file)
    pil.thumbnail((800,600))#橫圖:寬為 800, 高會等比例計算。直圖 : 高為 600, 寬會等比例計算
    file=os.path.basename(file)
    pil.save(os.path.join(thumb_dir, file))

def ext2lower(file):
    master, slave=os.path.splitext(file)
    slave=slave.lower()
    target=f"{master}{slave}"
    os.rename(file, target)
    return target

def dirTree(path):
    #一定要用 set, 速度才會快
    s=set([])
    for root, subdirs, files in os.walk(path):
        for file in files:
            lower=file.lower()
            if lower.endswith('.jpg') or lower.endswith('.png') or lower.endswith('.bmp'):
                full_path=os.path.join(root, file).replace("\\","/")
                s.add(full_path)
    return s

def listThumbDir(request):
    if platform.system() == "Linux":
        path="/data/upload/thumb"
    else:
        path="d:/upload/thumb"
    if 'dir' in request.GET:
        dir=request.GET["dir"]
    else:
        dir=''
    full=os.path.join(path,dir)
    files=os.listdir(full)
    files.sort()#因為 Linux 不會自動排序
    files=[f'{dir}/{file}'
        for file in files if os.path.isfile(os.path.join(path, dir, file))
    ]
    total=len(files)
    txt=""
    for i in range(math.ceil(total/5)):
        txt +="<div style='display:flex;'>"
        for j in range(5):
            if i * 5 + j < total:
                file=files[i * 5 + j]
                txt +=f"""
                <div class='with_img'>
                    <a href='javascript:void(0)' onclick='showPrimitive({i*5+j});'>
                        <img class ='img_thumb' src='/pictures/thumb/{file}'/>
                    </a>
                </div>
                """
            else:
                txt += "<div class='without_img'></div>"
        txt += '</div>'
    return HttpResponse(
        json.dumps(
            {'url':mark_safe(txt),'files':','.join(files)}
        ),
        content_type='application/json'
    )
def ai_detect(request):
    '''
    #有顯卡的人，要安裝 nVidia的 cuda及cudnn : https://mahaljsp.asuscomm.com/python_cuda_environment/
    #安裝套件
    #   有顯卡的人 :
    #       pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio===2.0.2+cu118 -f https://download.pytorch.org/whl/cu118/torch_stable.html
    #       pip install ultralytics
    #   沒顯卡的人 :
    #       pip install ultralytics
    #Django 一啟動，就要載入 yolov8n, yolov8x模型，需將載入程式寫在 manage.py檔中
    Javascript 編輯器 :　Visual studio code : https://code.visualstudio.com/
    1. File/Open folder : 選 d:/server/pyweb
    2. 修改完記得 Ctrl + S : 儲存
    '''
    path=f'{primitive_path}/{request.GET["photo"]}'

    pil=Image.open(path)
    #pil_show=pil

    ai_type=int(request.GET["ai_type"])
    if ai_type!=0:
        if ai_type==1:
            model=G.model_8n
        elif ai_type==2:
            model=G.model_8x
        h=800
        rate=3
        pil_show=pil.resize((int(pil.width/pil.height*h), h))
        #底下是要偵測的圖，縮小三倍，速度快，較不精準
        pil_dest=pil.resize((int(pil.width/pil.height * h / rate), int(h/rate)))
        results=model.predict(pil_dest)
        #底下適合有顯卡,有安裝 cuda的人
        names=[results[0].names[int(i.cpu().numpy())] for i in results[0].boxes.cls]

        #底下適合沒有顯卡的人，不可加 .cpu()
        #names = [results[0].names[int(i.numpy())] for i in results[0].boxes.cls]
        boxes=results[0].boxes.xyxy
        for box, name in zip(boxes, names):
            box=box.cpu().numpy()
            #box = box.numpy()
            x1 = int(box[0]) * rate
            y1 = int(box[1]) * rate
            x2 = int(box[2]) * rate
            y2 = int(box[3]) * rate
            pil_show = drawTag(pil_show, name, x1, y1, x2, y2, color=(255,255,255), size=22)
    #將圖片以 base64 傳回 ajax。切記，絕對不可以儲存在硬碟，再由 ajax取回
    img=np.asarray(pil_show)[:,:,::-1].copy()
    base64_str=cv2.imencode('.jpg', img)[1].tostring()
    base64_str=base64.b64encode(base64_str)
    return HttpResponse(base64_str)
def drawTag(pil, text, x1=0, y1=0, x2=0, y2=0, color=(0,0,0), size=12):
    s=platform.system()
    if s=="Linux":
        font=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', size)
    elif s=="Darwin":#Mac
        font=ImageFont.truetype('不知，自已查', size)
    else:
        font=ImageFont.truetype('simsun.ttc', size)
    draw=ImageDraw.Draw(pil, 'RGBA')
    draw.rectangle((x1, y1, x2, y2), outline=(0,255,0), width=2)
    #底下是預測文字寫入後，所佔的大小
    tx1, ty1, tx2, ty2 = draw.textbbox(xy=(x1, y1), text=text, font=font)
    #底下才是繪製方框
    draw.rectangle((x1+2, y1+2, tx2+2, ty2+2), fill=(0,0,200,100))
    draw.text((x1+2, y1+2), text, font=font, fill=color)
    return pil
