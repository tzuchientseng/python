import json

    # 模擬一個 data 字串
data_str = '''
    {
        "success": true,
        "result": {
            "resource_id": "301000000A-000605-071",
            "limit": 3000,
            "total": 375,
            "fields": [
                {"type": "text", "id": "statistic_yyy"},
                {"type": "text", "id": "site_id"},
                {"type": "text", "id": "people_total"},
                {"type": "text", "id": "area"},
                {"type": "text", "id": "population_density"}
            ],
            "records": [
                {"statistic_yyy": "統計年", "site_id": "區域別", "people_total": "年底人口數", "area": "土地面積", "population_density": "人口密度"},
                {"statistic_yyy": "111", "site_id": "新北市板橋區", "people_total": "549572", "area": "23.1373", "population_density": "23753 "},
                {"statistic_yyy": "111", "site_id": "新北市三重區", "people_total": "379825", "area": "16.317", "population_density": "23278 "}
            ]
        }
    }
    '''

    # 將 data_str 轉換為字典
data_dict = json.loads(data_str)

    # 從字典中獲取 records
records = data_dict["result"]["records"]

    # 逐一處理每個記錄
for record in records:
    statistic_yyy = record["statistic_yyy"]
    site_id = record["site_id"]
    people_total = record["people_total"]
    area = record["area"]

    print("統計年:", statistic_yyy)
    print("區域別:", site_id)
    print("年底人口數:", people_total)
    print("土地面積:", area)
    print("===================")
