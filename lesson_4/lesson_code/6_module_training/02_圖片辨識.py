"""
1. 讀取並處理圖片
2. 處理資料 (1. 維度擴充, 2. 預處理)
    # 預處理有三種, caffe, tf, torch, vgg使用 caffe
    # 先將 RGB 轉成 BGR, 再將所有點的 B值減 B的平均數，G/R亦同，讓每個顏色都分佈在 0 的左右二邊
    # 假設 B平均是 100，其中有一點 B 為250，則結果為 150
    # 另一點 B 若為 50，則結果為 -50
3. 開始辨識 // out 是每一個物件的分數，分數愈大，可能性愈大
4. 圖片寫入名稱與信心度
"""

import os

from keras.applications import vgg19
from keras.applications.vgg19 import preprocess_input

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from PIL import Image, ImageFont, ImageDraw
# 透明背景及中文字，是 cv2 作不到的
# cv2 => pillow => 處理 => cv2
import keras # k 勒斯
import cv2
import numpy as np
import pylab as plt

# 載入模型
model_path = "flower_5"
model = keras.models.load_model(model_path)

# 有的人認為 : 去辨識用來訓練的圖片，太偷吃步了
# 訓練出來的模型，能辨識訓練時的的圖，才是成功的一大步 : 必需經過此關卡驗証
# 最後才去辨識網路上其它的圖片
# file="./flower_photos/roses/12240303_80d87f77a3_n.jpg"

# 待辨識圖片
file = "1.jpg"
img = cv2.imdecode(np.fromfile(file, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
x = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
x = cv2.cvtColor(x,cv2.COLOR_BGR2RGB)
x = np.expand_dims(x, axis=0)

# 用from keras.applications.vgg19 import preprocess_input 預處理圖片及偵測圖片 
x = preprocess_input(x)
# results = vgg19.decode_predictions(out, top=3)
out = model.predict(x) # print(out) 可以印出分數 output: [[0.04167958 0.01030884 0.9125696  0.00181153 0.03363045]]
kind = {0:'daisy', 1:'dandelion', 2:'roses', 3:'sunflowers', 4:'tulips'}
idx = out[0].argmax() # numpy.ndarray 最大值的索引
score = out[0][idx]
name = kind[idx]
print(name, score)

# pillow 去處理文字
pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
font = ImageFont.truetype('simsun.ttc', 20) # 20表示字體大小
txt = f'名稱 : {name}\n信心度 : {score * 100: .2f}%'
ImageDraw.Draw(pil).text((5, 5), txt, font=font, fill=(255,255,0))
plt.figure(figsize=(12,9))
plt.imshow(pil)
plt.show()
