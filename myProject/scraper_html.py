from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
import os

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

# 模擬人類行為
actions = ActionChains(driver)
actions.move_by_offset(10, 10).perform()  # 模擬鼠標移動
time.sleep(random.uniform(1, 3))  # 隨機等待
actions.click().perform()  # 模擬點擊

# 等待頁面加載並抓取內容
time.sleep(5)  # 等待頁面完全加載
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 將抓取到的 HTML 寫入檔案
fn = os.path.join(os.path.dirname(__file__), 'output.html')
with open(fn, 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

# 關閉瀏覽器
driver.quit()
