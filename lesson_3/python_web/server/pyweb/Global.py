from django.utils.safestring import mark_safe
import requests
from datetime import datetime

class DB():
    dbHost = "localhost"
    dbAcount = "root"
    dbPassword = "open"
    dbTable = "cloud"
    
    @staticmethod
    def saveHistory(request, page):
        """
        Saves the history of a request and fetches geographical information based on the IP address.
        """
        # Get IP
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
        if ip:
            ip = ip.split(',')[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        # Initialize default values for location data
        city = ""
        country = ""
        lat = 0.0
        lng = 0.0

        # Fetch location data based on the IP
        try:
            url = "http://ip-api.com/batch?"
            params = {
                'fields': 'status, message, country, countryCode, region, regionName, city, query, lon, lat',
                'lang': 'en-US'
            }
            ip_list = [ip]
            resp = requests.post(url=url, json=ip_list, params=params)
            info = resp.json()[0]

            if info.get('status') == 'success':
                country = info.get('country', '')
                city = info.get('city', '')
                lat = info.get('lat', 0.0)
                lng = info.get('lon', 0.0)
            else:
                print(f"Error fetching location data: {info.get('message')}")

        except requests.RequestException as e:
            print(f"Error making request to IP API: {e}")

        # Database
        # 儲存到資料庫
        t = datetime.now()
        # 資料庫時間為什麼要分為兩個欄位
        # 方便日後，以日期查詢，效能快，分組快
        # 若日期及時間同一欄，日後要分組很麻煩
        eventDay = t.strftime("%Y-%m-%d")
        eventTime = t.strftime("%H:%M:%S")

        # Return the IP and formatted HTML with location data
        return ip, mark_safe(
            f"""
            <p class='info'>{ip}</p>
            <p class='info'>{country} {city}</p>
            <p class='info'>{lng:.5f}:{lat:.5f}</p>
            """
        )





# from django.utils.safestring import mark_safe
# import requests
# class DB():
#     dbHost = "localhost"
#     dbAcount = "root"
#     dbPassword = "open"
#     dbTable = "cloud"
#     @staticmethod
#     def saveHistory(request, page):
#         """
#             items = request.META.items()
#             for item in items:
#                 print(item)
#         """
#         # get IP
#         str = request.META.get("HTTP_X_FORWARDED_FOR")
#         if str:
#             ip = str.split(',')[0]
#         else:
#             ip = request.META.get("REMOTE_ADDR")
#         return ip, mark_safe(
#             f"""
#                 <p class='info'>{ip}</p>
#             """
#         )


#         # get 地區及經緯度
#         city = ""
#         country = ""
#         # 緯度
#         lat = 0
#         # 經度
#         lng = 0
#         url = "http://ip-api.com/batch?"
#         param={'fields':'status, message, country, countryCode, region, regionName, city, query, lon, lat', 'lang':'en-US'}
#         ip_list = [ip]
#         resp = requests.post(url=url, params=param)
#         info = resp.json()[0]

#         if 'country' in info:
#             country = info['country']
#             city = info['city']
#             lat = info['lat']
#             lng = info['lon']
#         return ip, mark_safe(
#             f"""
#             <p class='info'>{ip}</p>
#             <p class='info'>{country} {city}</p>
#             <p class='info'>{lng:.5f}:{lat:.5f}</p>
#             """
#         )
#         # 存入資料庫
"""
use cloud;
CREATE TABLE `history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ip` varchar(23) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `eventDay` date DEFAULT NULL,
  `eventTime` time DEFAULT NULL,
  `page` varchar(45) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `userAccount` varchar(45) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `country` varchar(20) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `city` varchar(20) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `lng` double DEFAULT NULL,
  `lat` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userAccount` (`userAccount`),
  KEY `ip` (`ip`),
  KEY `page` (`page`) /*!80000 INVISIBLE */,
  KEY `country` (`country`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci
"""