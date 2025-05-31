# 從 plyer 中導入 notification 模組
from plyer import notification

# 使用 notification 模組發送通知
notification.notify(
    title='提醒',           # 通知標題
    message='這是您的通知訊息。請注意！',  # 通知內容
    app_name='通知應用程式',    # 應用程式名稱
    timeout=10             # 通知持續時間（秒）
)
