import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from sklearn.linear_model import LinearRegression
from G import G
import mysql.connector as mysql
from datetime import datetime, timedelta
import yfinance as yf
import numpy as np
import plotly.graph_objects as go
import pandas as pd
# Create your views here.
def html(request):
    request.session["currentPage"]="/finance/ai"
    info=G.saveHistory(request, "finance_ai")
    conn=mysql.connect(host=G.dbHost, user=G.dbAccount, password=G.dbPassword, database=G.db)
    cursor=conn.cursor()
    cursor.execute("select * from 股票代號")
    rs=cursor.fetchall()
    conn.close()

    stock_menu = "<table width='120'>"
    for r in rs:
        stock_menu += f"""
            <tr>
                <td onclick="queryStock('{r[1]}','{r[2]}');" style="cursor:pointer;">
                {r[2]}
                </td>
            </tr>
        """
    stock_menu += "</table>"
    return render(
        request,
        "finance/finance.html",
        {"info":info[1], "userAccount":G.userAccount(request),"stock_menu":mark_safe(stock_menu)}
    )
def stock_query(request):
    ticker=request.GET["ticker"]
    #pip install yfinance
    #yfinance由 yahoo 開發，免費使用
    current=datetime.now()
    df=yf.download(ticker, '1970-01-01', current, auto_adjust=True)
    ma1 = 5#move average
    ma2 = 10
    #df=df[['Open','High','Low','Close','Volume']]
    df['s1'] = df['Close'].rolling(window=ma1).mean()
    df['s2'] = df['Close'].rolling(window=ma2).mean()
    df=df.dropna()
    #底下使用線性迴歸模型訓練及預測
    #pip install scikit-learn
    model = LinearRegression()
    train=df[['Close','s1','s2']]
    train['next_day_price']=train['Close'].shift(-1)
    train=train.dropna()
    x_train=train[['s1','s2']]
    y_train=train['next_day_price']
    model.fit(x_train, y_train)
    df['predict_price']=model.predict(df[['s1','s2']])
    df['signal']=np.where(df.Close<df.predict_price,"漲", "跌")

    stock_name=request.GET["stock_name"]
    html=f"""
    <table>
        <tr>
            <td colspan="8">{stock_name}預測資訊</td>
        </tr>
        <tr>
            <td colspan="6">實際交易</td>
            <td colspan="2">翌日預測</td>
        </tr>
        <tr>
            <td width="85">日期</td>
            <td width="65">開盤</td>
            <td width="65">最高</td>
            <td width="65">最低</td>
            <td width="65">收盤</td>
            <td width="80">成交量</td>
            <td width="70">價格</td>
            <td width="40">漲跌</td>
        </tr>
    """
    info=df.tail(10)
    date_array=info.index.strftime("%Y-%m-%d").values
    values=info.values
    for i,(d,v)in enumerate(zip(date_array, values)):
        if i%2 == 0:
            color="#f0f0f0"
        else:
            color="#e0e0e0"
        if v[8]=="漲":
            img = "<img src='/static/images/stock_up.png' width='15' height='20'>"
        else:
            img = "<img src='/static/images/stock_dn.png' width='15' height='20'>"
        html += f"""
            <tr bgcolor="{color}">
                <td>{d}</td>
                <td>{v[0]:,.2f}</td>
                <td>{v[1]:,.2f}</td>            
                <td>{v[2]:,.2f}</td>
                <td>{v[3]:,.2f}</td>
                <td>{v[4]:,}</td>
                <td>{v[7]:,.2f}</td>
                <td>{img}</td>
            </tr>
        """
    html+="</table>"

    fig=go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Close'].values,
            mode='lines',
            name="實際價格",
            line=dict(color='royalblue', width=2)
        )
    )

    pred=df[['predict_price']]
    #將預測值往後移一天
    s=(pred.tail(1).index + timedelta(days=1))[0]
    dates=pd.date_range(s, periods=1)
    pred.loc[dates[0]]=[0]
    pred['predict_price']=pred['predict_price'].shift(1)
    fig.add_trace(
        go.Scatter(
            x=pred.index,
            y=pred['predict_price'].values,
            mode='lines',
            name='AI預測',
            line=dict(color='orange', width=1)
        )
    )

    #底下是 copy twgold.py檔
    fig.update_layout(
        dragmode="pan",
        title_text=f"{stock_name}{ticker} 趨勢圖",
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

    graph=fig.to_html(include_plotlyjs='cdn')
    return HttpResponse(
        json.dumps(
            {'ai':mark_safe(html),'graph':graph}
        ),
        content_type="application/json"
    )