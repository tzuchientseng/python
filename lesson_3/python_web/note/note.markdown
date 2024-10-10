# 安全性

1.  在 dos 啟動 django
    d:
    cd \server\pyweb
    venv\Scripts\python.exe manage.py runserver 0.0.0.0:7001

2.  漏洞：http://localhost:7000/abc
    網頁立即出現相關資訊(router)

3.  補漏洞：
    settings.py : Debug = False
    http://localhost:7000/abc => Not Found

4.  補完漏洞後，http://localhost:7000/static 立即失效
    Django 官網說 Debug 一關掉，就不再處裡 /static，應該交由其他 web Server 處理

5.  其他 web Server: Apache, Nginx(俄羅斯人寫小而強悍)
    WAMP: Windows/Apache/MySQL/php
    Nginx+php+MySQL

6.  Nginx：可作反向代理伺服器
    http://mahaljsp.ddns.net
    http://shenny.ddns.net
    都指向同一台電腦，但不同目錄
    也可以出租網路空間

7.  port 的規劃
    Nginx : 80, Django:7001: http://localhost
    Nginx : 7000, Django:7001: http://localhost:7000
    啟動方式: `python manage.py runserver 0.0.0.0:7001`

8.  安裝 Nginx

    1. 下載 nginx/Windows-1.25.2，置於 server 目錄下，
       然後解壓縮至此，再將 nginx-1.25.2 目錄改成 nginx
    2. 啟動（只是測試有沒有用）
       e:
       cd \server\nginx
       start nginx
    3. http://localhost

9.  設定 Nginx

    1. 開啟 server\nginx\conf\nginx.conf
    2. listen 80 ; 改成想要的 port 比如 7000
       nginx -s stop: 停止 nginx
       start nginx: 重新啟動
    3. 測試 http://localhost:7000

10. 自動啟動 Nginx
    a. 下載 winsw : 將 Nginx 移到背景服務區
    [可用 Visual studio c# 自己寫](https://mahaljsp.asuscomm.com/windows-service/)
    http://repo.jenkins-ci.org/releases/com/sun/winsw/winsw/2.9.0/
    下載：winsw-2.9.0-bin.exe
    b. 按二下安裝，會要求安裝.netFramework：選下載及安裝
    c. 將 winsw-2.9.0-bin.exe 複製到 \server\nginx 之下，並改名為 nginx-winsw.exe
    d. 在 \server\nginx 下新增 nginx-winsw.xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <service>
    <id>Nginx</id>
    <name>Nginx</name>
    <description>Start Nginx Service</description>
    <logpath>D:\Coding\python\lesson_3\python_web\server\nginx\logs</logpath>
    <executable>nginx.exe</executable>
    <stopexecutable>nginx.exe</stopexecutable>
    <stopargument>-s</stopargument>
    <stopargument>stop</stopargument>
    <logmode>rotate</logmode>
    </service>

11. 安裝到背景服務

    1. 系統管理員開啟 DOS
    2. d:
       cd \server\nginx
       nginx-winsw.exe install : 安裝到背景服務區
       若要移除背景服務：nginx-winsw.exe uninstall
       此時工作管理員的服務就會有 nginx
    3. 啟動執行需重新開機，不然就是手動啟動
       執行 `net start nginx`
       停止`net stop nginx`

12. Nginx 與 Django 建立連線

    1. 開啟 nginx.conf
    2. location / {
       root html;
       index index.html index.htm;
       }

       location / {
       proxy_pass http://localhost:7001; #Nginx : 7000, Django:7001: http://localhost:7000
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; #取得客戶端連線真實 ip
       }

       location /pictures {
       alias d:/pictures;
       }

       location /static {
       alias D:\Coding\python\lesson_3\python_web\server\pyweb\static\;
       }

       location /download {
       alias d:/tools;
       }

       location /upload {
       alias d:/upload;
       }

    3. 動啟 nginx
       系統管理員開啟 dos 視窗
       net stop nginx
       net start nginx

    4. 所有 src static 前面都要加上 http://新路徑/static

13. 最後記得開啟 nginx port 的防火牆及 ip 分享器

---
