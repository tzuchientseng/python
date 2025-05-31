import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from G import G
from datetime import datetime
import mysql.connector as mysql
from django.utils.safestring import mark_safe
# Create your views here.
def html(request):
    info=G.saveHistory(request,'travel')
    request.session["currentPage"] = "/travel"
    if 'userAccount' not in request.session:
        return redirect("/login")
    currentMonth=datetime.now().strftime("%Y-%m")
    return render(
        request, 
        "travel.html",
        {'info':info[1],"userAccount":G.userAccount(request),"currentMonth":currentMonth}
        )

def map_menu(request):
    if "currentMonth" in request.GET:
        currentMonth=request.GET["currentMonth"]
    else:
        currentMonth=datetime.now().strftime("%Y-%m")
    conn=mysql.connect(host=G.dbHost, user=G.dbAccount, password=G.dbPassword, database=G.db)
    cursor=conn.cursor()
    cmd=f"select eventDay as menu from 旅遊軌跡 where eventDay like '{currentMonth}%' group by menu order by menu desc"
    cursor.execute(cmd)
    rs=cursor.fetchall()
    html=""
    for r in rs:
        html+=f"""
            <div class="mapMenuSingle">
                <a href="javascript:void(0)" onclick="loadRoute('{r[0]}')">{r[0]}</a>
            </div>
        """
    if html=="":html="<p>本月無資料</p>"
    return HttpResponse(mark_safe(html))
def route(request):
    userId=1
    if "currentDay" in request.GET:
        currentDay=request.GET["currentDay"]
    else:
        currentDay=datetime.now().strftime("%Y-%m-%d")
    
    conn=mysql.connect(host=G.dbHost, user=G.dbAccount, password=G.dbPassword, database=G.db)
    cursor=conn.cursor()
    cmd=f"select * from 旅遊軌跡 where eventDay='{currentDay}' and userId={userId} order by eventTime"
    cursor.execute(cmd)
    rs=cursor.fetchall()
    routes=[]
    for r in rs:
        flag=int(r[6])
        if flag==1:
            t=[]
            routes.append(t)
        t.append([r[2],r[3]])
    return HttpResponse(
        json.dumps({'routes':routes}),
        content_type="application/json"
    )
def marker(request):
    carId=1
    if "currentDay" in request.GET:
        currentDay = request.GET["currentDay"]
    else:
        currentDay=datetime.now().strftime("%Y-%m-%d")
    conn=mysql.connect(host=G.dbHost, user=G.dbAccount, password=G.dbPassword, database="cloud")
    #conn=mysql.connect(host=G.dbHost, user=G.dbAccount, password=G.dbPassword, database="travel")
    cursor=conn.cursor()
    cmd=f"select * from 旅遊案件 where eventDay='{currentDay}' and userId={carId} order by eventTime"
    cursor.execute(cmd)
    rs=cursor.fetchall()
    cursor.close()
    conn.close()
    markers=[]
    print(cmd)
    for r in rs:
        eventDay=r[6]
        #eventDay=r[7]
        year=eventDay.strftime("%Y")
        url=f'{year}/{r[9]}'
        markers.append([r[2], r[3],r[5],f'{r[6]} {r[7]}',r[8], url])
        #url=f'{year}/{r[10]}'
        #markers.append([r[3],r[4], r[6], f'{r[7]} {r[8]}', r[9], url])
    print("thomas==========",markers)
    return HttpResponse(
        json.dumps({'markers': markers}),
        content_type = "application/json"
    )