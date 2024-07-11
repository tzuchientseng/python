# import requests
# from bs4 import BeautifulSoup

# # resp = requests.get('https://www.showtimes.com.tw/')
# # html = resp.text
# # soup = BeautifulSoup(html, 'html.parser')
# # print(soup.find('section'))
# # # print(soup.find_all(class_="sc-gFAWRd iCPDmh"))
# """
# for i in range(5):
#     print(f"=== PAGE {i} ===")
#     res = requests.get(f'https://www.vscinemas.com.tw/vsweb/film/index.aspx?p={i}')
#     html = res.text

#     soup = BeautifulSoup(html, 'html.parser')
#     sections = soup.find_all('section', {'class': 'infoArea'})
#     for section in sections:
#         print(section.find('a').text)
# """


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import os
# import csv
# import time
# from webdriver_manager.chrome import ChromeDriverManager

# # 設定選項
# options = Options()
# options.headless = False  # 設為 True 以啟動 headless 模式
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# # 使用 webdriver_manager 安裝並啟動 ChromeDriver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# url = 'https://tw-nba.udn.com/nba/team_tab/583ecae2-fb46-11e1-82cb-f4ce4684ea4c'
# driver.get(url)
# html = driver.page_source

# print(html)

"""
sudo apt update && sudo apt upgrade -y
sudo apt install netcat
nc -l -p 10000
"""
import requests
url = 'http://127.0.0.1:9998'

header = {

    
}
res = requests.get(url)
print(res.content.decode())