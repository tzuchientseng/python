#訓練好的模型，會自動儲存在 ./runs/detect/train/weights/best.pt
#./runs/detect/train/weights/last.pt 是中斷前最後一次的訓練，方便以後繼續訓練用的(resume)。
import os
import platform
import pylab as plt
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from ultralytics import YOLO
def text(img, text, xy=(0, 0), color=(0, 0, 0), size=12):
    pil = Image.fromarray(img)
    s = platform.system()
    if s == "Linux":
        font =ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', size)
    elif s == "Darwin":
        font = ImageFont.truetype('....', size)
    else:
        font = ImageFont.truetype('simsun.ttc', size)
    ImageDraw.Draw(pil).text(xy, text, font=font, fill=color)
    return np.asarray(pil)
model=YOLO('./runs/detect/train/weights/best.pt')
path='./Dollar/test/images'
files=['IMG_2022_jpg.rf.858671efee801e1b455b6248d8fb40bd.jpg',
       'IMG_2055_jpg.rf.2b61d396ede26321d219d11eabf6cb81.jpg',
       'IMG_2178_jpeg_jpg.rf.953788ffa7a6b2f3cbfeda9443ac7136.jpg',
       'IMG_2274_jpeg_jpg.rf.f867e6964483cd87feefadd6d2acbf01.jpg']
#將每張圖讀入/餵入 model偵測得到 results/取得每個物件的四個角/畫框線
for i, file in enumerate(files):
    img=cv2.imdecode(np.fromfile(os.path.join(path, file), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    img=img[:,:,::-1].copy()
    results=model.predict(img, save=False)
    boxes=results[0].boxes.xyxy
    #底下是給有顯卡的人用的
    names=[results[0].names[int(idx.cpu().numpy())] for idx in results[0].boxes.cls]
    # 底下是給沒有顯卡的人用的
    #names = [results[0].names[int(idx.numpy())] for idx in results[0].boxes.cls]
    for box, name in zip(boxes, names):
        box=box.cpu().numpy()#沒顯卡的人，不需加 .cpu()
        x1 = int(box[0])
        y1 = int(box[1])
        x2 = int(box[2])
        y2 = int(box[3])
        img=cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 3)
        img=text(img, name, (x1, y1-20), (0,0,255),20)
    plt.subplot(2,2,i+1)
    plt.axis("off")
    plt.imshow(img)
plt.show()

