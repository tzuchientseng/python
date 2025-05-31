from django.http import HttpResponse
from django.shortcuts import redirect, render
import mysql.connector as mysql
from Global import DB
import time
import json

login_chances = 3

# Create your views here.

def login(request):
    info = DB.saveHistory(request, 'login')
    if "loginCount" in request.session and request.session["loginCount"] >= login_chances:
        return redirect("/reject") 
    else:
        return render(request, "login.html", {"Info" : info[1]})

def logout(request):
    if 'userAccount' in request.session:
        del request.session["userAccount"]

def login_process(request):
    # userAccount = request.GET["userAccount"]
    # userPasword = request.GET["userPassword"]
    if "loginCount" in request.session and request.session["loginCount"] >= login_chances:
        return redirect("/reject") 

    userAccount = request.POST["userAccount"]
    userPassword = request.POST["userPassword"]
    print(userAccount, userPassword)
    
    conn = mysql.connect(
        host = DB.dbHost,
        user = DB.dbAcount,
        password = DB.dbPassword,
        database = DB.dbTable
    )
    cursor = conn.cursor()
    cmd = f"SELECT * from 會員資料 where userAccount ='{userAccount}' and userPassword = '{userPassword}'"
    cursor.execute(cmd)
    rs = cursor.fetchall() # record set (list)
    conn.close()
    # for row in rs:
        # print(row)
    if len(rs) > 0:
        # session 可以橫跨不同的網頁
        # 不是全域店數 只有這條 session 的人可以看到
        request.session['userAccount'] = userAccount
        if 'currentPage' in request.session:
            return redirect(request.session["currentPage"])
        else:
            return redirect('/')
    else:
        if "logintCount" not in request.session:
            request.session["loginCount"] = 1
        else:
            request.session["lognCount"] += 1
        time.sleep(3)

        if request.session['loginCount'] >= login_chances:
            return redirect("/reject")
        return render(request, 'login.html', context={"login": "error"})

    # return HttpResponse()

def check_session(request):
    session={"session":"ok"}

    if "userAccount" not in request.session:
        session["session"]="error"

    return HttpResponse(json.dumps(session), content_type="application/json")

def reject(request):
    return redirect('/reject')