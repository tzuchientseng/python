import datetime
import json
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector as mysql
from G import G
chance=3
# Create your views here.
def login(request):
    info=G.saveHistory(request,'login')

    if "loginCount" in request.session and request.session["loginCount"]>=chance:
        return redirect("/reject")
    else:
        return render(request, "login.html",{"info":info[1],"userAccount":G.userAccount(request)})
def logout(request):
    if 'userAccount' in request.session:
        del request.session["userAccount"]
    return redirect("/login")#重新導向首頁

def login_process(request):
    #萬用密碼：SQL Injection
    #帳號 : 隨便
    #密碼 :a' or '1'='1
    #select * from 會員資料 where userAccount='aa' and userPassword='a' or '1'='1'
    if "loginCount" in request.session and request.session["loginCount"]>=chance:
        return redirect("/reject")
    userAccount=request.POST["userAccount"].replace("'","\\'")#防止 SQL Injection
    userPassword=request.POST["userPassword"].replace("'","\\'")

    conn=mysql.connect(
        host=G.dbHost,
        user=G.dbAccount,
        password=G.dbPassword,
        database=G.db
    )

    cursor=conn.cursor()
    cmd=f"select * from 會員資料 where userAccount='{userAccount}' and userPassword='{userPassword}'"
    cursor.execute(cmd)
    rs=cursor.fetchall()#record set
    conn.close()
    if len(rs)>0:
        #session 可以橫跨不同的網頁
        #但又不是全域變數，只有這條 session 的人可以看到
        #G檔的類別變數才是全域變數，每條 session 每個網頁都看得到
        request.session['userAccount']=userAccount
        if 'currentPage' in request.session:
            response = redirect(request.session["currentPage"])
        else:
            response = redirect("/")
        max_age=7200
        #response.set_cookie("userAccount", userAccount, domain="shenny.ddns.net")
        return response
    else:
        #一條連線為一個執行緒，睡個 3秒不會影響其它人的運作
        if "loginCount" not in request.session:
            request.session["loginCount"] = 1
        else:
            request.session["loginCount"] +=1;
        time.sleep(3)

        if request.session['loginCount'] >=chance:
            return redirect("/reject")
        return render(request, 'login.html',{"login":"error","userAccount":G.userAccount(request)})
def reject(request):
    info=G.saveHistory(request,'封鎖')
    return render(request, 'reject.html',{"info":info[1],"userAccount":G.userAccount(request)})