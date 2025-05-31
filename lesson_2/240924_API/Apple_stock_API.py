"""
APPLE_stock_daily = 'https://api.polygon.io/v1/open-close/AAPL/2024-09-23?adjusted=true&apiKey=FPZ4ieYqCl79yNYU42JQwLsw15ZbhSsF'
{'status': 'OK', 'from': '2024-09-23', 'symbol': 'AAPL', 'open': 227.34, 'high': 229.45, 'low': 225.81, 'close': 226.47, 'volume': 50709047.0, 'afterHours': 226.23, 'preMarket': 228.4}
url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=FPZ4ieYqCl79yNYU42JQwLsw15ZbhSsF'
url2= 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-02-10?adjusted=true&sort=asc&apiKey=FPZ4ieYqCl79yNYU42JQwLsw15ZbhSsF'

c *數字
在給定時間內交易品種的收盤價。

h *數量
在給定時間內該品種的最高價格。

l *數字
在給定時間內該品種的最低價格。

n整數
聚合視窗中的交易數量。

o *數字
在給定時間內交易品種的開盤價。

場外交易布林值
此聚合是否用於場外交易代碼。如果為 false，則該欄位將被忽略。

t *整數
聚合視窗開始的 Unix 毫秒時間戳記。

v *數字
在給定時間內交易品種的交易量。

大眾編號
成交量加權平均價格。

next_url字串
如果存在，該值可用於取得下一頁資料。
"""
from abc import ABC, abstractmethod
import requests
from datetime import datetime, timedelta
from plyer import notification  # 用於彈出桌面通知

# 繼承自 QueryStrategy 抽象類別
class QueryStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# 定義 AppleStock 策略
class AppleStock(QueryStrategy):
    API_key = 'FPZ4ieYqCl79yNYU42JQwLsw15ZbhSsF'

    def execute(self):
        today = datetime.today()
        date_today = today.strftime('%Y-%m-%d')
        url_today = f'https://api.polygon.io/v1/open-close/AAPL/{date_today}?adjusted=true&apiKey={self.API_key}'
        
        try:
            response_today = requests.get(url_today)
            response_today.raise_for_status()
            data_today = response_today.json()
            open_price_today = data_today.get('open')
            
            if open_price_today is None:
                raise ValueError("無法從 API 中獲取今日開盤價")
            
            print(f"Apple 今日開盤價: {open_price_today} 美元")
            
            # 顯示通知
            notification.notify(
                title='Apple Stock Notification',
                message=f'Apple 今日開盤價: {open_price_today} 美元',
                app_name='Stock Notifier',
                timeout=10  # 通知顯示時間，單位為秒
            )

        except requests.exceptions.RequestException as e:
            print(f"網路請求錯誤(超過請求用量): {e}")
        except ValueError as ve:
            print(f'資料錯誤: {ve}')
        except Exception as ex:
            print(f'發生未知錯誤: {ex}')



"""
兩天開盤比較
"""
# import requests
# from datetime import datetime, timedelta
# from plyer import notification  # 用於彈出桌面通知

# # API 金鑰
# API_key = 'FPZ4ieYqCl79yNYU42JQwLsw15ZbhSsF'

# # 取得今天的日期
# today = datetime.today()

# # 計算昨天與前天的日期
# yesterday = today - timedelta(days=1)
# day_before_yesterday = today - timedelta(days=2)

# # 將日期格式化為 'YYYY-MM-DD'
# date_today = today.strftime('%Y-%m-%d')
# date1 = yesterday.strftime('%Y-%m-%d')
# date2 = day_before_yesterday.strftime('%Y-%m-%d')

# # 產生 API 端點 URL
# url_today = f'https://api.polygon.io/v1/open-close/AAPL/{date_today}?adjusted=true&apiKey={API_key}'
# url1 = f'https://api.polygon.io/v1/open-close/AAPL/{date1}?adjusted=true&apiKey={API_key}'
# url2 = f'https://api.polygon.io/v1/open-close/AAPL/{date2}?adjusted=true&apiKey={API_key}'

# try:
#     # 嘗試抓取今天、昨天與前天的數據
#     response_today = requests.get(url_today)
#     response1 = requests.get(url1)
#     response2 = requests.get(url2)

#     # 檢查 API 回應是否成功
#     response_today.raise_for_status()
#     response1.raise_for_status()
#     response2.raise_for_status()
    
#     data_today = response_today.json()
#     data1 = response1.json()
#     data2 = response2.json()
    
#     # 取得今日、昨天與前天的開盤價，若資料不存在，拋出 ValueError
#     open_price_today = data_today.get('open')
#     open_price_day1 = data1.get('open')
#     open_price_day2 = data2.get('open')
    
#     if open_price_today is None:
#         raise ValueError("無法從 API 中獲取今日開盤價")
#     if open_price_day1 is None or open_price_day2 is None:
#         raise ValueError("無法從 API 中獲取昨天或前天的開盤價")

#     # 計算昨日與前日開盤價的差異
#     difference = open_price_day1 - open_price_day2
    
#     # 計算百分比變動
#     percentage_change = (difference / open_price_day2) * 100
    
#     # 設定通知門檻，可以自行調整這個值
#     absolute_threshold = 10  # 美元
#     percentage_threshold = 3  # 百分比
    
#     # 印出今日開盤價
#     print(f"今日開盤價: {open_price_today} 美元")
    
#     # 判斷差異是否超過門檻
#     if difference > 0:
#         print(f"昨日與前日的開盤價上漲。差異 = {difference} 美元，變動百分比 = {percentage_change:.2f}%")
#         # 顯示通知
#         notification.notify(
#             title='股價通知',
#             message=f'AAPL 昨日與前日的開盤價上漲，差異 = {difference:.2f} 美元，變動百分比 = {percentage_change:.2f}%',
#             app_name='Stock Notifier',
#             timeout=10  # 通知顯示時間，單位為秒
#         )
#     elif difference < 0:
#         print(f"昨日與前日的開盤價下跌。差異 = {abs(difference)} 美元，變動百分比 = {abs(percentage_change):.2f}%")
#     else:
#         print("昨日與前日的開盤價沒有變動。")

# except requests.exceptions.RequestException as e:
#     print(f"網路請求錯誤: {e}")
# except ValueError as ve:
#     print(f"資料錯誤: {ve}")
# except KeyError as ke:
#     print(f"資料鍵錯誤: {ke}")
# except ZeroDivisionError:
#     print("除以零錯誤，前天的開盤價可能為零")
# except Exception as ex:
#     print(f"發生未知錯誤: {ex}")