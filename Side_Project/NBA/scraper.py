"""
|Season:賽季|Age:年齡|Tm:隊伍|Lg:聯盟|Pos:位置|G:比賽數|GS:首發數|MP:平均上場時間（每場比賽）|FG:投籃命中數|FGA:投籃出手數|FG%:投籃命中率|3P:三分球命中數|3PA:三分球出手數|3P%:三分球命中率|2P:
兩分球命中數|2PA:兩分球出手數|2P%:兩分球命中率|eFG%:有效命中率|FT:罰球命中數|FTA:罰球出手數|FT%:罰球命中率|ORB:進攻籃板|DRB:防守籃板|TRB:總籃板|AST:助攻|STL:抄截|BLK:阻攻|TOV:失誤|PF:犯規|PTS:得分|Awards:獎項|
"""
import requests
from bs4 import BeautifulSoup

def fetch_player_data(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', id='per_game')
    headers = [th.text for th in table.find('thead').find_all('th')]
    rows = table.find('tbody').find_all('tr')
    data = []
    for row in rows:
        cells = row.find_all(['th', 'td'])
        data.append([cell.text.strip() for cell in cells])
    return headers, data

url1 = 'https://www.basketball-reference.com/players/j/jamesle01.html'
url2 = 'https://www.basketball-reference.com/players/j/jordami01.html'

headers1, data1 = fetch_player_data(url1)
headers2, data2 = fetch_player_data(url2)

print("LeBron James 的數據:")
print(headers1)
for row in data1:
    print(row)

print("\nMichael Jordan 的數據:")
print(headers2)
for row in data2:
    print(row)

# # 合併成一個字典
# all_data = {
#     'LeBron James': data1,
#     'Michael Jordan': data2
# }
# print(all_data)
