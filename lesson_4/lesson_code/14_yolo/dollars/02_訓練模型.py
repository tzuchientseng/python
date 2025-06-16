import os
import shutil
import time
from ultralytics import YOLO
#訓練時，一定要放在 __name__區塊中，否則會要求使用 fork 子行程來執行
if __name__=='__main__':
    train_path="./runs/detect/train"
    if os.path.exists(train_path):
        shutil.rmtree(train_path)
    model=YOLO('yolov8n.pt')
    print("開始訓練....")
    t1=time.time()
    model.train(data="./Dollar/data.yaml", epochs=200, imgsz=640)
    t2=time.time()
    print(f'訓練花費時間 : {t2-t1}秒')
    path=model.export()#將訓練好的模型儲存起來
    print(f"新模型路徑 : {path}")