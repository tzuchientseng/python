# 5 個 API 作品架構

## python 版 -> 用 requests 模組處裡 API 資訊 + 策略模式(取代 if-else 達成開放-封閉和單一職則原則)

- API
  [API 說明文件](https://data.gov.tw/dataset/32972)
  [API 路徑](https://www.ris.gov.tw/rs-opendata/api/v1/datastore/ODRP007/yyymm（請指定年月）)
  示範 API: `GET https://www.ris.gov.tw/rs-opendata/api/v1/datastore/ODRP001/10601`

- 功能:
  0 -> quit
  1 -> 查詢所有名稱
  2 -> 查詢台北市結婚 110 年年齡分布
  3 -> 查詢台北市結婚 110 年教育程度分布
  4 -> 查詢台北市結婚 110 年年齡+教育程度分布
  5 -> 查詢台北市離婚 111 年教育程度分布

## Website 版 -> fetch API(promise) 非同步處理 + DOM 操作(強迫數據給前端做 API 處理 flask 只用 render_template 不做傳值 API 數據處理)

- 自己的 API 伺服器
  [API 說明文件](https://blog.sunnytseng.com/essay/myAPI.html)
  [API Documentation](https://api.sunnytseng.com/docs)
  [API 路徑(base)](http://api.sunnytseng.com)

- 功能:
  API_1:商品定價建議
  API_2:商品銷售量 95 信賴區間
  API_3:商品銷售量 98 信賴區間
  API_4:商品銷售量變異數 95 信賴區間
  API_5:各月份的總營業額描述性統計

---
