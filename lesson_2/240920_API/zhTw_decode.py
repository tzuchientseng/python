import requests
import json

school_API = 'https://stats.moe.gov.tw/files/school/113/school08_new.json'

resp = requests.get(school_API)

# print(resp.text)
# print(resp.content)
"""
# resp.text 和 resp.content 的差異：
# 1. resp.text: 返回解碼後的字符串，自動處理編碼（通常是 UTF-8）
# 2. resp.content: 返回原始的字節串（bytes），未經解碼

print("resp.text (解碼後的字符串):")
print(resp.text[:100])  # 只打印前100個字符作為示例

print("\nresp.content (原始字節串):")
print(resp.content[:100])  # 只打印前100個字節作為示例
"""

try:
    data = resp.json()  # 使用 json() 方法解析 JSON 數據
    print(data)  # 打印解析後的數據

except requests.exceptions.JSONDecodeError:
    # Handle UTF-8 BOM
    data = resp.content.decode('utf-8-sig') # 回傳字串
    dict_ = json.loads(data)
    # print(json.loads(data))
     
    
    for school in dict_:
        print(school.get('學年度'))
        print(school.get('學校級別'))
        print(school.get('學校代碼'))
        print(school.get('學校名稱'))
        print(school.get('郵遞區號'))
        # print(school['學校地址']) # KeyError: '學校地址'
        print('---')
