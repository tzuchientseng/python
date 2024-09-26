# 網站規劃

e:\server
mysql
wordpress
tomcat
pyweb
💡

# Pycharm 設定

1. new Project

# django

> 每個客戶要分別建立虛擬主機
>
> > Anaconda
> > VENV _virtual environment_
> >
> > > `python -m venv myenv` >>>`WINDOWS: myenv\Scripts\activate` >>>`UNIX/MacOS: source myenv/bin/activate`

---

# 建立專案

1. `django-admin startproject webapp`
2. `cd webapp`
3. `python ./manage.py runserver` _按下 TAB 會自動補齊_

---

# 建立資料夾

1. `python .\manage.py migrate`

---

# Anaconda

1. 過於肥大
2. 跟 qt 相衝 (好的呈現方式)
3. 跟 AI cuda11.8 不合：只適用於 python3.8/3.9，pytorch 也是
   tkinter：玩具(matplotlib 使用 tkinter)

(政府系統 不推薦)Windwows IIS MSSQL ASP.NET

Linux Apache->Nginx MySQL PHP

Pycharm 設定

1. new Project

2. 第一個 location : e:\server\20230921 ： 整個路徑，絕對不可以用中文

但裏面的檔案，.py 或 .html 可以使用中文

因為 pip install 安裝套件時，不認識中文

3. 注意一下第二個 location 有沒有手動加 \venv

4. 改成白底黑字：File/settings/Apperance/Theme/Intellij Light
   放大字體：File/Settings/Editor/General/
   Change font size with control + mouse wheel
   安裝套件時 (pip install) 會發生 activate.ps1 無法載入的問題
   a. 開始/Windows PowerShell/Windows PowerShell 按右鍵以系統管理員身份執行，啟動
   b. set-ExecutionPolicy remotesigned：再選 A(ll)
   c. 關閉 Pycharm，再重啟才會生效
   d. pip install numpy

# djaongo

`cd pyweb`
`django-admin startproject pyweb`
`python manage.py runserver 0.0.0.0:7000`
http://127.0.0.1:7000/ 或 http://localhost:7000/
不要用 9000 port 那是給 nginx 聯繫 PHP 重要 port

# 兩種傳法

render()：用於返回完整的模板頁面，適合處理複雜的 HTML 模板，並能夠輕鬆將數據傳遞給模板。
HttpResponse：用於直接返回一個字符串（通常是 HTML 內容），適合簡單回應或在模板不可用的情況下使用。

# MVC 架構: Model/View/Controller

模板

1. 在 templates 裡撰寫 html
2. settings.py 增加 'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
3. 在專案根目錄新增 second.py
4. 設定 urls

# 網頁 APP

python manage.py startapp myapp
python .\manage.py startapp home

Pycharm 注意事項

1. Microsoft Defender 請按 automatic： 不使用防毒軟體偵測，加快效能
2. PreBuild 千萬別按，不然會變成簡體中文，比如 new Project => 建立新項目

HttpResponse：第一個網頁
render：第二個網頁，模板 #模板：MVC 架構：Model/View/Controller

網頁 app：一個網頁，可能由多個 python 組合而成

1. python manager.py startapp home : admin/apps/models/tests/views 的 py 檔
   其中的 view.py 是 app 的 py 檔案
2. 修改 view.py
3. 寫模板 .html
4. 修改 urls.py
   import home.views as home
   from home import views as home # 這樣也可
   path('xxx/', home.html)

---

# 電腦啟動後 自動啟動 django server

1. 按下 Win + R 鍵以開啟「執行」對話框。
2. 在「執行」對話框中輸入以下指令：
   `taskschd.msc`
3. 開始/Windows 系統管理工具/工作排程器/建立基本工作
   名稱：Django
   在電腦啟動時執行
   啟動程式
   程式或指令碼：e:\server\pyweb\venv\Scripts\python.exe
   新增引數：e:\server\pyweb\manage.py runserver 0.0.0.0:7000
   Django 按二下：不論使用者登入與否均執行

shell:startup (此方法需要登入才能啟動)

---

# ip

1. 進入 dos : ipconfig ： 查詢虛擬 ip
2. chrome 搜尋 ip ： 查真實 ip
3. 回報上網的方式： 手機熱點，社區網路，都無法架站，只能用 http://localhost
4. Default Gateway . . . . . . . . . : fe80::8202:9cff:fed3:93f8%11
   192.168.1.1

# 網域申請

1. no ip : https://www.noip.com/sign-up : SignUp
2. 登入 : Dynamic DNS/NO-IP HostName : Create hostname
3. Domain : ddns.net

no ip : https://www.noip.com/sign-up : SignUp
登入：Dynamic DNS/NO-IP HostName : Create hostname
Domain：ddns.net
其實浮動 ip 也可以監控，也可以架站
跟 no-ip 回報自己的真實 ip Dynamic DNS/Dynamic Update Client : DUC
測試：ping 網域.ddns.net：有看到 ip 表示成功了

---
