import requests
from bs4 import BeautifulSoup

# 取得網頁內容
url = 'https://tw-nba.udn.com/nba/team_tab/583ecae2-fb46-11e1-82cb-f4ce4684ea4c'
resp = requests.get(url)

# 確認請求成功
if resp.status_code == 200:
    html = resp.content.decode()
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # 找到所有<h3>標籤
    content = soup.find_all('h3')
    
    # 列印每個<h3>標籤的文字內容
    for title in content:
        print(title.get_text())

else:
    print("Failed to retrieve the webpage.")
