import time
from ultralytics import YOLO
if __name__=="__main__":
    #model=YOLO("yolov8n.pt")
    model = YOLO("yolov8s.pt")
    print("開始訓練模型...")
    t1=time.time()
    results=model.train(data="./data.yaml", epochs=200, imgsz=640)
    t2=time.time()
    path=model.export()
    print(f'訓練花費時間{t2-t1}秒')
    print(f'模型儲存位置 : {path}')