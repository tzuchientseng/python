# pip install tensorflow==2.10.1 matplotlib opencv-python
# 本例在無顯卡或顯卡RAM小於8G 的電腦上無法執行，請切換到 colab
# 請先下載訓練的圖片 http://download.tensorflow.org/example_images/flower_photos.tgz
# "解壓縮"至此" 後，進入 flower_photos目錄，將 LICENSE.txt 刪除
# daisy(雛菊)，dandelion(蒲公英)，roses(玫瑰)，sunflowers(向日葵)，tulips(鬱金香)
# 此例是為了熟悉訓練的步驟，其原理日後會慢慢說明

"""
# colab
import os
from google.colab import drive # 載入掛載(mount)套件
import cv2
from google.colab.patches import cv2_imshow
drive.mount("/data") # 自動建立 /data，並將 /MyDrive掛在 /data之下
img_path="/data/MyDrive/flower_photos" # 圖片的完整路徑
import pylab as plt
imgs = []
labels = []
for name in os.listdir(img_path):
    for flower in os.listdir(os.path.join(img_path, name)):
        full = os.path.join(img_path, name, flower)
        print(full)
"""

import tensorflow as tf
# 設定使用 CPU/GPU
gpus = tf.config.list_physical_devices(device_type='GPU')
cpus = tf.config.list_physical_devices(device_type='CPU')
tf.config.set_visible_devices(devices=gpus[0], device_type='GPU')
# tf.config.set_visible_devices(devices=cpus[0])  # 強制使用 CPU

# zlibwapi.dll 錯誤
# nVidia 有很多的bug，如果出現 Could not locate zlibwapi.dll. Please make sure it is in your library path!，
# 這是新版的 bug，請先下載 http://www.winimage.com/zLibDll/zlib123dllx64.zip，
# 解開後將 zlibwapi.dll複製到 C:\Windows\System32位置下面。

import os
import random

from keras import Sequential
from keras.applications import VGG19
from keras.layers import GlobalAveragePooling2D, Dense, BatchNormalization, Dropout
from keras.optimizers import Adam

os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"
import numpy as np
import cv2
import shutil

# 開始讀取圖片資料
# "/":Linux, "\\" : Windows
img_path = "./flower_photos"
imgs = []
labels = []
for flower in os.listdir(img_path):
    for file in os.listdir(os.path.join(img_path, flower)):
        full_path = os.path.join(img_path, flower, file)
        # 讀出圖片
        img = cv2.imdecode(
            np.fromfile(full_path, dtype=np.uint8),
            cv2.IMREAD_UNCHANGED
        )
        # 轉換圖片
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR) # 一定要縮到 224 (規定且省空間)
        imgs.append(img)
        labels.append(flower)

# 共有 3670 張圖片，可且每張圖都是沒壓縮的，所以非常耗記憶體，還好縮小為 224*224
# print(f'共有{len(imgs)}張圖片')
# 混淆資料並切割 10% 為 test
random.seed(1)
upset = list(zip(imgs, labels)) # tuple 是物件再透過 list() 
random.shuffle(upset) # 將 list 的順序搞亂
imgs, labels = zip(*upset) # 兩次 zip 是為了 shuffle 一樣方式 * 表示解包 一個個傳出去
train = int(len(imgs) * 0.9) # 要訓練的數量

# 要訓練的資料
train_imgs = np.array(imgs[:train])
train_labels = np.array(labels[:train])
# 要測試的資料(其實是為了計算正確率的分數)，所以有時會用不到
test_imgs = np.array(imgs[train:])
test_labels = np.array(labels[train:])

# 轉換成 onehot
train_onehot = np.zeros([len(train_labels),5])
test_onehot = np.zeros([len(test_labels),5])
kind = {'daisy':0, 'dandelion':1, 'roses':2, 'sunflowers':3, 'tulips':4}
for i in range(len(train_onehot)):
    # item = train_labels[i] # 'sunflowers'
    # no = kind[item] # kind['sunflowers'], no = 3
    # train_onehot[i][no] = 1  # [0 0 0 1 0]
    train_onehot[i][kind[train_labels[i]]] = 1
for i in range(len(test_onehot)):
    test_onehot[i][kind[test_labels[i]]] = 1

"""
# 建立模型
from keras.applications import VGG19 : 此才是正統的
keras : 凱拉斯，也是 AI 的套件, 被 tensorflow 併入，但後來又不明原因分開
from tensorflow import keras : 可能會被拋棄掉
VGG19 共有 16 層隱藏層(捲積conv)及 3 個全連接層(輸出層) :
其實最前面還有一個 input層，是圖片輸入的 layer
隱藏層就是演算的地方 : 通常進行捲積
全連接層，就是輸出結果的 layer
VGG19 最後的輸出激活函數為 softmax, 是計算 1000種物件，每個物件的機率，總合為 1
include_top : False, 不包含最後的全連接層, 要換成我們的 5 種 (原本是1000種)
weights權重: imagenet, 由VGG19幫我們訓練的，權重置於隱藏層中
conv : 捲積層
pool : 池化層，刪除一些沒用的資料
"""
model_base = VGG19(weights='imagenet', include_top=False, input_shape=(224,224,3))
for layer in model_base.layers:
    # 保留 VGG19 所給的權重，不要重新訓練
    layer.trainable = False
model = Sequential() # 依序，也就是一層一層往下執行，沒有迴圈，也不會跳
model.add(model_base)

# 底下是第一個全連接層
# GlobalAveragePooling2D : 將(長*寬*通道)轉成 (1*1*通道)，其方法是將每個通道中的權重作平均值
# 通道 : channel, 也就是 RGB 3通道
# 100 * 100 = 10000 個點，共有 30000個顏色值
model.add(GlobalAveragePooling2D())
# 將資料壓縮到只有256種，每麼壓，要看後面的激活函數
# relu : 線性整流，將負值去除掉
model.add(Dense(256, activation='relu'))
# batch 批量(1000), Normalization : 常態分佈
# BN的作用 : 把 batch 內的所有數據，從不規則的分佈拉到常態分佈，
# 將數字集中在平均為0，標準差為1的範圍，使數據能分佈在激活函數的敏感區域
# BN是一篇很長的論文，也有複雜的數學計算式，只需了解其功能即可。
model.add(BatchNormalization())
# 第二個全連接層
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2)) # 將20%的資料丟棄，避免過度擬合
# 第三個全連接層
# softmax : 每個狀況都用機率來表示，最大值表示最有可能
model.add(Dense(5, activation='softmax'))
# 編譯模型, 設定優化器，學習率，損失函數
# learning_rate : 太大太小都不行，會造成無法收斂
# 損失函數 : categorical:分類(這 5 類的那一種), crossentropy : 交叉熵:混亂的程度
# 一個房間，久了沒住，就會開始混亂，熵是用來計算混亂的程度
# 本來是要計算宇宙的混亂程度
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy']
)
# 開始訓練模型
history = model.fit(
    train_imgs,
    train_onehot,
    batch_size = 64, # OOM(out of memory) 的話，調整 32, 16, 8, 4 ， 愈小越慢
    epochs = 50,
    validation_data = (test_imgs, test_onehot)
)


model_path = "flower_5"
if os.path.exists(model_path):
    shutil.rmtree(model_path) # shutil 會把非空目錄全部砍掉
model.save(model_path)

# 底下是看有沒有過度擬合，精準度無法再提高(維持水平)，就不需再繼續，再繼續，浪費時間，過度擬合
# pip install matplotlib
import pylab as plt
plt.plot(history.history['accuracy'], label='training acc') # 訓練時的準確度
plt.plot(history.history['val_accuracy'], label='val acc') # 測試時的準確度
plt.plot(history.history['loss'], label='training loss') # 訓練時的損失率
plt.plot(history.history['val_loss'], label='val loss') # 測試時的損失率
plt.legend()
plt.show()
