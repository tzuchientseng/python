import platform
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from ultralytics import YOLO
import pylab as plt

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

model=YOLO('yolov8x.pt')

img=cv2.imdecode(np.fromfile("street.jpg", dtype=np.uint8), cv2.IMREAD_UNCHANGED)
img=img[:,:,::-1].copy()#一定要 copy，否則無法畫框線
#results=model.predict("street.jpg")
results=model.predict(img)

print('物件種類 : ',results[0].boxes.cls)#cls : class
print('座標 : ',results[0].boxes.xyxy)
#print(results[0].names)#列出80種物件的索引及名稱
# for i in results[0].boxes.cls:
#     idx=int(i.cpu().numpy())
#     print(idx, results[0].names[idx])
names=[results[0].names[int(i.cpu().numpy())] for i in results[0].boxes.cls]
boxes=results[0].boxes.xyxy

for box, name in zip(boxes, names):
    box=box.cpu().numpy()
    print(name, box)
    x1 = int(box[0])
    y1 = int(box[1])
    x2 = int(box[2])
    y2 = int(box[3])
    img=cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 1)
    img=text(img, name, (x1, y1-20), color=(0,0,255), size=16)
plt.imshow(img)
plt.show()
