import plotly
from django.shortcuts import render
from G import G
import mysql.connector as mysql
import numpy as np
import plotly.graph_objects as go
#因為 Python 製作圖表很方便，是其它程式語言所沒有的，所以才會連網頁都改成 Django
def html(request):
    info=G.saveHistory(request, 'twgold')
    request.session["currentPage"]="/finance/twgold"
    conn=mysql.connect(
        host="mahaljsp.asuscomm.com",
        user="lcc",
        password="lcc0507",
        database="cloud"
    )
    cmd="select * from 台銀黃金 order by 日期"
    cursor=conn.cursor()
    cursor.execute(cmd)
    rows=cursor.fetchall()

    x=range(len(rows))
    sale=[]
    buy=[]
    dates=[]
    for r in rows:
        dates.append(r[1])
        buy.append(r[2])
        sale.append(r[3])
    f=np.poly1d(np.polyfit(x, sale, 10))
    reg=f(x)
    fig=go.Figure()
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=sale,
            mode='lines',
            name='黃金賣出',
            line=dict(
                color='royalblue',
                width=2
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=buy,
            mode='lines',
            name='黃金買入',
            line=dict(
                color='green',
                width=2
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=reg,
            mode='lines',
            name='趨勢線',
            line=dict(
                color='orange',
                width=2
            )
        )
    )
    fig.update_layout(
        dragmode="pan",
        title_text="台銀黃金存摺",
        xaxis=go.layout.XAxis(
            rangeselector=dict(
                buttons=list([
                    dict(
                        count=1,
                        label="1 month",
                        step="month",
                        stepmode="backward"
                    ),
                    dict(
                        count=6,
                        label="6 month",
                        step="month",
                        stepmode="backward"
                    ),
                    dict(
                        count=1,
                        label="1 year",
                        step="year",
                        stepmode="backward"
                    ),
                    dict(
                        count=1,
                        label="1 day",
                        step="day",
                        stepmode="backward"
                    ),
                    dict(
                        step="all"
                    )
                ])
            ),
            #當變更 x 的範圍，想要同時變動 y 軸的範圍，目前無法作出，網路上的說明都是假的。官網說目前無此功能
            rangeslider=dict(visible=True),
            type="date"
        ),
        yaxis=dict(fixedrange=False)#目前有 bug
    )

    #一般人的教法
    # plotly.offline.plot(fig, filename="d:/server/pyweb/static/twgold.html", auto_open=False)
    # return render(request, 'finance/twgold.html')

    #正確的寫法
    data=fig.to_html(include_plotlyjs='cdn')#使用 bootstrap的套件

    return render(
        request,
        'finance/twgold.html',
        {"info":info[1],"userAccount":G.userAccount(request),"data":data}
    )