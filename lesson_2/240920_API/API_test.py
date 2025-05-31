import requests
import json

currency_API = 'https://tw.rter.info/capi.php'
bank_code = 'https://raw.githubusercontent.com/wsmwason/taiwan-bank-code/master/data/taiwanBankCodeATM.json'
sport_API = 'https://vbs.sports.taipei/opendata/sports_tms2.json'
school_API = 'https://stats.moe.gov.tw/files/school/113/school08_new.json'

resp = requests.get(sport_API)
data = resp.json()
# print(data)

# ensure_ascii=False: 允許非 ASCII 字符（如中文）直接輸出，而不是使用 \uXXXX 轉義
#                     這裡的 False 意味著"不要限制只使用 ASCII 字符"
#                     如果設為 True，所有非 ASCII 字符都會被轉換為 \uXXXX 格式
# \uXXXX 格式: 這是 Unicode 轉義序列，其中 XXXX 是字符的 16 進制 Unicode 碼點
#              例如，中文字符 "中" 的 Unicode 碼點是 U+4E2D，轉義後就是 \u4E2D
pretty_data = json.dumps(data, indent=4, ensure_ascii=False)
print(pretty_data)

for key1 in data:
    print("--------")
    area = key1["Area"]
    name = key1["Name"]
    name_eng = key1["NameEng"]
    sport_type = key1["SportType"]
    address = key1["Address"]
    address_eng = key1["AddressEng"]
    start_time = key1["startTime"]
    end_time = key1["endTime"]
    local_call_service = key1["LocalCallService"]

    print("區域(Area):", area)
    print("名稱(Name):", name)
    print("英文名稱(NameEng):", name_eng)
    print("運動類型(SportType):", sport_type)
    print("地址(Address):", address)
    print("英文地址(AddressEng):", address_eng)
    print("開始時間(startTime):", start_time)
    print("結束時間(endTime):", end_time)
    print("本地電話服務(LocalCallService):", local_call_service)
    print("--------")
