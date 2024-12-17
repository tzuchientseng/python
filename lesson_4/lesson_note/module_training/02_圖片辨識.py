import os

from keras.applications import vgg19
from keras.applications.vgg19 import preprocess_input

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from PIL import Image, ImageFont, ImageDraw
#透明背景及中文字，是 cv2 作不到的
#cv2=>pillow=>處理=>cv2
import keras
import cv2
import numpy as np
import pylab as plt
model_path="flower_5"
model=keras.models.load_model(model_path)
#有的人認為 : 去辨識用來訓練的圖片，太偷吃步了
#訓練出來的模型，能辨識訓練時的的圖，才是成功的一大步 : 必需經過此關卡驗証
#最後才去辨識網路上其它的圖片
#file="./flower_photos/roses/12240303_80d87f77a3_n.jpg"
file="1.jpg"
img=cv2.imdecode(np.fromfile(file, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
x=cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
x=cv2.cvtColor(x,cv2.COLOR_BGR2RGB)
x=np.expand_dims(x, axis=0)

#預處理圖片及偵測圖片
x=preprocess_input(x)
out=model.predict(x)
kind={0:'daisy', 1:'dandelion', 2:'roses', 3:'sunflowers', 4:'tulips'}
idx=out[0].argmax()
score=out[0][idx]
name=kind[idx]
print(name, score)
pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
font = ImageFont.truetype('simsun.ttc', 20)
txt=f'名稱 : {name}\n信心度 : {score*100:.2f}%'
ImageDraw.Draw(pil).text((5, 5), txt, font=font, fill=(255,255,0))
plt.figure(figsize=(12,9))
plt.imshow(pil)
plt.show()