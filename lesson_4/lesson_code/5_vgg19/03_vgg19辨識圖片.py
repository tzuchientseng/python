# vgg19 一張照片只能辨識一個物件，所以圖片的主角只能有一個
# yolo/yolact可以辨識多個物件
# Google Object Detection功能如同 vgg19, 但 GOD 效能極差，所以不用學習
# tensorflow 已到 2.13 版，一樣不支援 cuda 11.8
# pip install tensorflow==2.10.1 opencv-python Pillow matplotlib
# 沒有顯卡的人，只能在colab執行
# Pillow: 另一套圖型處理套件，主要是用來寫入中文字體
# cv -> pillow -> 寫中文 -> cv

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

from PIL import Image, ImageFont, ImageDraw
import numpy as np
import cv2
import pylab as plt
from keras.applications import VGG19, vgg19
from keras.applications.vgg19 import preprocess_input

# 第一次執行時, 會上網下載 VGG19模型，所以要比較久一點
# 下載位置 : c:/user/登入者/.keras/models
model = VGG19(weights='imagenet', include_top=True)

"""
1. 讀取並處理圖片
"""
img = cv2.imdecode(np.fromfile('2.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# VGG19的100萬張圖片，都縮小成224*224來訓練
# img 保留，用 x 去偵測，主要是留原圖(img)來顯示
x = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
# plt.imshow(x)
# plt.show()

"""
2. 處理資料 (1. 維度擴充, 2. 預處理)
x原本的維度是(224,224,3)
vgg19規定, 在偵測圖片時，必需傳入 (1,224,224,3)的格式
vgg19會把偵測後的結果，填入最前面的維度
"""
x = np.expand_dims(x, axis=0)
"""
# 預處理資料
# 預處理有三種, caffe, tf, torch, vgg使用 caffe
# 先將 RGB 轉成 BGR, 再將所有點的 B值減 B的平均數，G/R亦同，讓每個顏色都分佈在 0 的左右二邊
# 假設 B平均是 100，其中有一點 B 為250，則結果為 150
# 另一點 B 若為 50，則結果為 -50
"""
x = preprocess_input(x) # from keras.applications.vgg19 import preprocess_input

"""
3. 開始辨識
out 是每一個物件的分數，分數愈大，可能性愈大
"""
out = model.predict(x)
results = vgg19.decode_predictions(out, top=3) # vgg 這次是小寫
# print(results) # 各個物件種類
# results = vgg19.decode_predictions(out, top=1000)
# for r in results[0]:
#     print(r)

"""
4. 圖片寫入名稱與信心度
"""
name = results[0][0][1]
score = results[0][0][2]
pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# truetype : 向量字(以前都是用點陣字，放大後很醜，有鋸齒狀)
font = ImageFont.truetype('simsun.ttc',100)
txt = f'名稱:{name}\n\n信心度:{score*100:.2f}%'
ImageDraw.Draw(pil).text((5,5), txt, font=font, fill=(255,255,0))
plt.imshow(pil)
plt.show()
