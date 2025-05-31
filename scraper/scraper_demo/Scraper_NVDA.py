from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import csv
import time
import random
from webdriver_manager.chrome import ChromeDriverManager

# 設定選項
options = Options()
options.headless = False  # 設為 True 以啟動 headless 模式
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 使用 webdriver_manager 安裝並啟動 ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 請求目標 URL
url = 'https://hk.investing.com/equities/nvidia-corp-historical-data'
driver.get(url)

# 等待頁面加載並抓取內容
time.sleep(1)  # 增加等待時間

# 等待表格元素出現
wait = WebDriverWait(driver, 30)  # 增加等待時間到30秒
try:
    table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.freeze-column-w-1.w-full.overflow-x-auto.text-xs.leading-4')))
    print("表格已找到")
except Exception as e:
    print(f"表格未找到: {e}")
    driver.quit()
    exit()

# 解析頁面
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 提取股價數據
def get_stock_data(soup):
    table = soup.find('table', {'class': 'freeze-column-w-1 w-full overflow-x-auto text-xs leading-4'})  # 根據實際HTML結構選擇合適的標籤和類別
    if not table:
        print("無法找到表格")
        return []

    stock_data = []
    for row in table.find_all('tr')[1:]:  # 跳過標題行
        columns = row.find_all('td')
        if len(columns) == 7:  # 確保有7個數據列
            stock_data.append({
                '日期': columns[0].get_text(strip=True),
                '收市': columns[1].get_text(strip=True),
                '開市': columns[2].get_text(strip=True),
                '高': columns[3].get_text(strip=True),
                '低': columns[4].get_text(strip=True),
                '成交量': columns[5].get_text(strip=True),
                '升跌(%)': columns[6].get_text(strip=True)
            })
    return stock_data

# 提取數據並打印
stock_data = get_stock_data(soup)
for data in stock_data:
    print(data)

# 保存數據到CSV文件
def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8-sig') as output_file:  # 使用utf-8-sig編碼
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# 保存到文件
fn = os.path.join(os.path.dirname(__file__), 'NVDA.csv')
save_to_csv(stock_data, fn)

print("數據已保存到 NVDA.csv")

# 關閉瀏覽器
driver.quit()

"""
畫圖
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

# File path (adjust if needed)
file_path = os.path.join(os.path.dirname(__file__), 'NVDA.csv')

# Read CSV file
df = pd.read_csv(file_path)

# 確保「日期」列的格式正確
df['日期'] = pd.to_datetime(df['日期'], format='%Y-%m-%d')

# 強制將「收市」列轉換為字符串類型
df['收市'] = df['收市'].astype(str)
df['收市'] = df['收市'].str.replace(',', '').astype(float)

# 強制將「成交量」列轉換為字符串類型
df['成交量'] = df['成交量'].astype(str)
df['成交量'] = df['成交量'].str.replace('M', '').astype(float)

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot closing prices
ax1.set_xlabel('Date')
ax1.set_ylabel('Close', color='tab:blue')
ax1.plot(df['日期'], df['收市'], color='tab:blue', label='Close')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis for volume
ax2 = ax1.twinx()
ax2.set_ylabel('Volume (M)', color='tab:red')
ax2.plot(df['日期'], df['成交量'], color='tab:red', label='Volume')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Title and layout
plt.title('Closing Price and Volume Line Chart')
fig.tight_layout()
plt.show()
