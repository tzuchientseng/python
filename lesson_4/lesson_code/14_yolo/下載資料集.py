#https://public.roboflow.com/
#進入 roboflow 100, 搜尋 : Dollar bill detection
#下載後，解壓縮檔案，將目錄改為 Dollar, 裏面會有 train/test/valid/data.yaml
#開啟 Dollar/data.yaml，前三個改成絕對路徑
# train: E:/python_ai/dollars/Dollar/train/images
# val: E:/python_ai/dollars/Dollar/valid/images
# test: E:/python_ai/dollars/Dollar/test/images

#下載權重 : https://github.com/ultralytics/ultralytics，下載 yolov8n.pt

#使用 yolo.exe 訓練
#yolo task=detect mode=train model=./yolov8n.pt data=./Dollar/data.yaml epochs=200 imgsz=640
