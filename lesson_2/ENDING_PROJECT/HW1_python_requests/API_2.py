"""
API說明文件 https://www.ris.gov.tw/rs-opendata/api/Main/docs/v1 API路徑 https://www.ris.gov.tw/rs-opendata/api/v1/datastore/ODRP007/yyymm（請指定年月）
GET https://www.ris.gov.tw/rs-opendata/api/v1/datastore/ODRP001/10601
"""
from abc import ABC, abstractmethod
import requests

# 繼承自 QueryStrategy 抽象類別
class QueryStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class Age_Marrige(QueryStrategy):
    def execute(self):
        # 定義API的URL，這裡使用民國110年
        url = "https://www.ris.gov.tw/rs-opendata/api/v1/datastore/ODRP068/110"

        # 定義查詢參數
        params = {
            "PAGE": "1",          # 第1頁
            "COUNTY": "臺北市"     # 篩選縣市為臺北市
        }

        # 發送 GET 請求
        try:
            response = requests.get(url, params=params)
            
            # 檢查回應狀態碼
            if response.status_code == 200:
                data = response.json()
                
                # 檢查資料的結構並提取需要的內容
                if "responseData" in data:
                    marriage_data = data["responseData"]
                    
                    # 定義一個字典來存儲各年齡段的總結婚人數
                    age_group_totals = {}

                    # 遍歷每個回應的資料項
                    for entry in marriage_data:
                        age = entry["age"]
                        number_of_marry = int(entry["number_of_marry"])

                        # 如果該年齡段尚未在字典中，則初始化
                        if age not in age_group_totals:
                            age_group_totals[age] = 0

                        # 累加該年齡段的結婚人數
                        age_group_totals[age] += number_of_marry
                    
                    # 印出各年齡段的總結婚人數
                    for age, total in age_group_totals.items():
                        print(f"年齡段: {age}, 總結婚人數: {total}")

                else:
                    print("無法找到 'responseData' 欄位")
            else:
                print(f"錯誤: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"請求失敗: {e}")


def main():
    obj = Age_Marrige()
    obj.execute()

if __name__ == "__main__":
    main()