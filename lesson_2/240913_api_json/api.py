"""
[Currency API](https://tw.rter.info/capi.php)
[Bank Code](https://raw.githubusercontent.com/wsmwason/taiwan-bank-code/master/data/taiwanBankCodeATM.json)
+ `curl -X GET https://tw.rter.info/capi.php`
+ 簡化為 `curl https://tw.rter.info/capi.php` 會達到同樣效果，預設GET
"""
import requests

r = requests.get('https://tw.rter.info/capi.php')
# print(r.json())

data  = r.json()

for currency, info in data.items():
    exrate = info['Exrate']
    update = info['UTC']
    # print(f"幣別:{currency}, 匯率{currency}, 更新時間{update}")

r2 = requests.get('https://raw.githubusercontent.com/wsmwason/taiwan-bank-code/master/data/taiwanBankCodeATM.json')
for bank_info in r2.json():
    name = bank_info['name']
    code = bank_info['code'] 
    print(f"Bank_Name: {name}, Code: {code}")
