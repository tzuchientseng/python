import requests
import json

url = 'https://api.sunnytseng.com/calculate_max_revenue'

data = {
"monthly_data": {
    "m1": { "profit": 10, "sales": 200 },
    "m2": { "profit": 15, "sales": 190 },
    "m3": { "profit": 17, "sales": 200 },
    "m4": { "profit": 18, "sales": 210 },
    "m5": { "profit": 20, "sales": 200 },
    "m6": { "profit": 20, "sales": 230 },
    }
}

headers = {"Content-Type" : "Application/json"}
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())