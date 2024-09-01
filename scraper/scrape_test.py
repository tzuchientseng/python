from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import os

# 設定選項
options = Options()
options.headless = False  # 設為 True 以啟動 headless 模式
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 指定 ChromeDriver 的路徑
service = Service('C:/Users/GOOD-PC/.wdm/drivers/chromedriver/win64/127.0.6533.119/chromedriver-win32/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

# 請求目標 URL
# url = 'https://www.scribd.com/document/579691735/Joe-Robinson-Byron-s-Bounce'
driver.get(url)

# 等待頁面加載
driver.implicitly_wait(10)

# 找到所有 image_layer 的 divs
image_layers = driver.find_elements(By.CLASS_NAME, 'image_layer')

# 創建保存圖片的資料夾
if not os.path.exists('sheet_music'):
    os.makedirs('sheet_music')

# 下載圖片
for index, image_layer in enumerate(image_layers):
    # 檢查 image_layer 中是否有 img 標籤
    img = image_layer.find_element(By.TAG_NAME, 'img')
    img_url = img.get_attribute('src')

    if img_url.startswith('http'):
        img_data = requests.get(img_url).content
        with open(f'sheet_music/page_{index + 1}.jpg', 'wb') as handler:
            handler.write(img_data)
            print(f'下載完成: page_{index + 1}.jpg')
    else:
        print(f'跳過非HTTP圖片: {img_url}')

# 關閉瀏覽器
driver.quit()

