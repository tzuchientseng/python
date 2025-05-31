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

class All_tags(QueryStrategy):
    def execute(self):
        url = 'https://www.ris.gov.tw/rs-opendata/api/Main/docs/v1'

        # 使用 GET 請求
        response = requests.get(url)
        if response.status_code == 200:
            # 直接處理 response.json()
            data = response.json()
            
            # 確保資料結構有 "tags" 這個鍵
            if "tags" in data:
                # 印出每個 tag(dict) 裡的 name 和 description
                for tag in data["tags"]:
                    name = tag.get("name", "No name")
                    description = tag.get("description", "No description")
                    print(f"{name} - {description}")
            else:
                print("No 'tags' found in the response data.")


        else:
            print(f"Error: {response.status_code} - {response.text}")

def main():
    obj = All_tags()
    obj.execute()

if __name__ == "__main__":
    main()