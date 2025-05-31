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
url = 'https://stock.wearn.com/cdata.asp?Year=113&month=06&kind=2382'
driver.get(url)

# 等待頁面加載並抓取內容
time.sleep(3)  # 增加等待時間

# 等待表格元素出現
wait = WebDriverWait(driver, 3)  # 增加等待時間到3秒
try:
    table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tr.stockalllistbg1, tr.stockalllistbg2')))
    print("表格已找到")
except Exception as e:
    print(f"表格未找到: {e}")
    driver.quit()
    exit()

# 解析頁面
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 提取股價數據
def get_stock_data(soup):
    table_rows = soup.find_all('tr', {'class': ['stockalllistbg1', 'stockalllistbg2']})
    if not table_rows:
        print("無法找到表格")
        return []

    stock_data = []
    for row in table_rows:
        columns = row.find_all('td')
        if len(columns) == 6:  # 確保有6個數據列
            stock_data.append({
                '日期': columns[0].get_text(strip=True),
                '開盤價': columns[1].get_text(strip=True),
                '最高價': columns[2].get_text(strip=True),
                '最低價': columns[3].get_text(strip=True),
                '收盤價': columns[4].get_text(strip=True),
                '成交量': columns[5].get_text(strip=True)
            })
    return stock_data

# 提取數據並打印
stock_data = get_stock_data(soup)
for data in stock_data:
    print(data)

# 保存數據到CSV文件
def save_to_csv(data, filename):
    if not data:
        print("無數據可保存")
        return
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8-sig') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# 保存到文件
fn = os.path.join(os.path.dirname(__file__), 'csv/QUANTA.csv')
save_to_csv(stock_data, fn)

print("數據已保存到 QUANTA.csv")

# 關閉瀏覽器
driver.quit()

