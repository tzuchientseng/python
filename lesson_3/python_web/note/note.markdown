# 安全性

1. 在 dos 啟動 django
   d:
   cd \server\pyweb
   venv\Scripts\python.exe manage.py runserver 0.0.0.0:7001

2. 漏洞：http://localhost:7000/abc
   網頁立即出現相關資訊(router)

3. 補漏洞：
   settings.py : Debug = False
   http://localhost:7000/abc => Not Found

4. 補完漏洞後，http://localhost:7000/static 立即失效
   Django 官網說 Debug 一關掉，就不再處裡 /static，應該交由其他 web Server 處理

5. 其他 web Server: Apache, Nginx(俄羅斯人寫小而強悍)
   WAMP: Windows/Apache/MySQL/php
   Nginx+php+MySQL

6. Nginx：可作反向代理伺服器
   http://mahaljsp.ddns.net
   http://shenny.ddns.net
   都指向同一台電腦，但不同目錄
   也可以出租網路空間

7. port 的規劃
   Nginx : 80, Django:7001: http://localhost
   Nginx : 7000, Django:7001: http://localhost:7000
   啟動方式: `python manage.py runserver 0.0.0.0:7001`

8. 安裝 Nginx
   a. 下載 nginx/Windows-1.25.2，置於 server 目錄下，
   然後解壓縮至此，再將 nginx-1.25.2 目錄改成 nginx

   b. 啟動（只是測試有沒有用）
   e:
   cd \server\nginx
   start nginx

---
