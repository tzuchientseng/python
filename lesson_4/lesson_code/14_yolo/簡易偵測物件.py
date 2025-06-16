# 在 terminal 執行
# yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"

# 上面會自動下載 yolov8n.pt 模型，並存放在專案的根目錄之下
# 也會自動下載 bus.jpg
# 偵測結果在 ./runs/detect/predict, predict2, ...

# yolov8n.pt 為 預先訓練好的模型(權重)，可辨識80種物件 : https://github.com/ultralytics/ultralytics
# yolo v8n, v8s, v8m, v8l, v8x :愈後面愈準確，愈慢

# yolo.exe 是一個執行檔, 置於 venv\Scripts\yolo.exe，此檔由 vs2019(也有可能是 vs2022)編譯而成的
# 如果 yolo.exe 無法執行，請安裝 vs2019試試，若還不行，再安裝 vs2022

