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
model=YOLO("./runs/detect/train2/weights/best.pt")
#model=YOLO("./best.pt")
img_path="./valid/images"
plt.figure(figsize=(12,9))
for i, file in enumerate(os.listdir(img_path)[-6:]):
    full=os.path.join(img_path, file)
    img=cv2.imdecode(
        np.fromfile(full, dtype=np.uint8),
        cv2.IMREAD_UNCHANGED
    )[:,:,::-1].copy()
    results=model.predict(img)
    boxes=results[0].boxes.xyxy
    #names = [results[0].names[int(idx.numpy())] for idx in results[0].boxes.cls]
    names=[results[0].names[int(idx.cpu().numpy())] for idx in results[0].boxes.cls]
    for box, name in zip(boxes, names):
        box=box.cpu().numpy()
        x1=int(box[0]);y1=int(box[1]);x2=int(box[2]);y2=int(box[3]);
        img=cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0),2)
        img=text(img, name, (x1, y1-25), (0,255,0), 25)
    plt.subplot(2, 3, i+1)
    plt.axis("off")
    plt.imshow(img)
plt.show()