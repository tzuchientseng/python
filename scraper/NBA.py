from requests_html import HTMLSession
from bs4 import BeautifulSoup
from pyppeteer.launcher import launch
import asyncio
import webbrowser

# 創建一個HTMLSession對象
session = HTMLSession()

# 定義目標 URL
url = "https://tw-nba.udn.com/widget.html"

# 手動指定 Chromium 的路徑
chromium_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'  # 替換為你的 Chrome 或 Chromium 可執行文件的路徑

# 定義渲染函數，手動指定 Chromium 的路徑
async def render_with_chromium(html, timeout=20):
    browser = await launch(executablePath=chromium_path, ignoreHTTPSErrors=True, headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.setContent(html)
    await page.waitForSelector('body', timeout=timeout*1000)
    rendered_html = await page.content()
    await browser.close()
    return rendered_html

# 發送HTTP請求
response = session.get(url)

# 渲染JavaScript
if response.status_code == 200:
    rendered_html = asyncio.run(render_with_chromium(response.html.html))
    
    # 解析HTML
    soup = BeautifulSoup(rendered_html, 'html.parser')

    # 找到包含比賽分數的區域
    dates = soup.find_all('div', class_='card_date')
    cards = soup.find_all('div', class_='card')

    # 檢查是否找到匹配的數據
    if dates and cards:
        date_iter = iter(dates)  # 創建日期迭代器
        current_date = next(date_iter).get_text(strip=True)  # 獲取第一個日期

        for card in cards:
            # 如果當前卡片是日期卡片，更新當前日期
            if 'card_date' in card['class']:
                current_date = card.get_text(strip=True)
                continue

            # 找到每個比賽卡片中的球隊和比分
            teams = card.find_all('div', class_='team')
            if len(teams) == 2:
                team1_name = teams[0].find('span', class_='team_name').get_text(strip=True)
                team1_score = teams[0].find('span', class_='team_score').get_text(strip=True)
                team2_name = teams[1].find('span', class_='team_name').get_text(strip=True)
                team2_score = teams[1].find('span', class_='team_score').get_text(strip=True)

                print(f"{current_date}: {team1_name} {team1_score} - {team2_name} {team2_score}")
    else:
        print("No matching data found.")
        # print(response.text)
        webbrowser.open(url)        
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# from requests_html import HTMLSession
# from bs4 import BeautifulSoup
# from pyppeteer.launcher import launch
# import asyncio

# # 定義目標 URL
# url = "https://tw-nba.udn.com/widget.html"

# # 創建一個 HTMLSession 對象
# session = HTMLSession()

# # 手動指定 Chromium 的路徑
# chromium_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'  # 替換為你的 Chrome 或 Chromium 可執行文件的路徑

# # 定義渲染函數，手動指定 Chromium 的路徑
# async def render_with_chromium(html, timeout=60):
#     browser = await launch(executablePath=chromium_path, ignoreHTTPSErrors=True, headless=True, args=['--no-sandbox'])
#     page = await browser.newPage()
#     await page.setContent(html)
#     await page.waitForSelector('div.card', timeout=timeout*1000)  # 等待比賽卡片元素出現
#     rendered_html = await page.content()
#     await browser.close()
#     return rendered_html

# # 發送 HTTP 請求
# response = session.get(url)

# # 渲染 JavaScript
# if response.status_code == 200:
#     rendered_html = asyncio.run(render_with_chromium(response.html.html))
    
#     # 打印渲染後的 HTML
#     # print(rendered_html)  # 調試用

#     # 解析 HTML
#     soup = BeautifulSoup(rendered_html, 'html.parser')

#     # 找到包含比賽分數的區域
#     dates = soup.find_all('div', class_='card_date')
#     cards = soup.find_all('div', class_='card')

#     # 檢查是否找到匹配的數據
#     if dates and cards:
#         print("Dates found:", len(dates))
#         print("Cards found:", len(cards))

#         date_iter = iter(dates)  # 創建日期迭代器
#         current_date = next(date_iter).get_text(strip=True)  # 獲取第一個日期

#         for card in cards:
#             # 如果當前卡片是日期卡片，更新當前日期
#             if 'card_date' in card['class']:
#                 current_date = card.get_text(strip=True)
#                 continue

#             # 找到每個比賽卡片中的球隊和比分
#             teams = card.find_all('div', class_='team')
#             if len(teams) == 2:
#                 team1_name = teams[0].find('span', class_='team_name').get_text(strip=True)
#                 team1_score = teams[0].find('span', class_='team_score').get_text(strip=True)
#                 team1_color = teams[0].find('span', class_='team_color')['style'].split(':')[-1].strip()
#                 team2_name = teams[1].find('span', class_='team_name').get_text(strip=True)
#                 team2_score = teams[1].find('span', class_='team_score').get_text(strip=True)
#                 team2_color = teams[1].find('span', class_='team_color')['style'].split(':')[-1].strip()

#                 print(f"{current_date}: {team1_name} ({team1_color}) {team1_score} - {team2_name} ({team2_color}) {team2_score}")
#     else:
#         print("No matching data found.")
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
