from django.http import HttpResponse
from django.shortcuts import redirect, render
import mysql.connector as mysql
from Global import DB

# Create your views here.

def login(request):
    return render(request, "login.html")

def logout(request):
    pass

def login_process(request):
    # userAccount = request.GET["userAccount"]
    # userPasword = request.GET["userPassword"]

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
    cmd = "SELECT * from 會員資料"
    cursor.execute(cmd)
    rs = cursor.fetchall() # record set (list)
    for row in rs:
        print(row)

    return HttpResponse()

def check_session(request):
    pass