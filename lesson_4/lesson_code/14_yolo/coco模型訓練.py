#底下的程式會產生 train/labels.cache及valid/labels.cache
#若要重新訓練，比如日後的 yolov9，要先刪除再訓練
import time
from ultralytics import YOLO
if __name__=='__main__':
    model=YOLO('yolov8n.pt')
    t1=time.time()
    model.train(data='./coco/data.yaml', epochs=3000, imgsz=640)
    t2=time.time()
    path=model.export()
    print(f'訓練花費時間 : {t2-t1}秒')
    print(f'模型儲存路徑 : {path}')
