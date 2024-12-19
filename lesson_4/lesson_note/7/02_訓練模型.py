import os
import shutil

import cv2
from keras import Sequential
from keras.applications import VGG19
from keras.layers import GlobalAveragePooling2D, Dense, BatchNormalization, Dropout
from keras.optimizers import Adam

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
flowers = []
dirs = []

with open('label.txt','r')as file:
    for line in file:
        line=line.strip() # 去除 \n
        cols=line.split()
        # s=int(cols[0])
        # e=int(cols[1])
        flower=cols[2]
        flowers.append(flower)
        # dirs += [flower] * (e-s+1)#此寫法會比上面陣列的效能高很多
# dirs = np.array(dirs)

train_imgs = []
train_labels = []
test_imgs = []
test_labels = []
train_path = "train_images"
test_path = "test_images"

for flower in flowers:
    for file in os.listdir(os.path.join(train_path, flower)):
        full = os.path.join(train_path, flower, file)
        img = cv2.imdecode(np.fromfile(full, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
        train_imgs.append(img)
        train_labels.append(flower)
train_imgs = np.array(train_imgs)

# 測試資料
for flower in flowers:
    for file in os.listdir(os.path.join(test_path, flower)):
        full = os.path.join(test_path, flower, file)
        img = cv2.imdecode(np.fromfile(full, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
        test_imgs.append(img)
        test_labels.append(flower)
test_imgs = np.array(test_imgs)

# one hot
train_onehot = np.zeros([len(train_labels),17], dtype=np.int32)
test_onehot = np.zeros([len(test_labels),17], dtype=np.int32)

for i in range(len(train_onehot)):
    train_onehot[i][flowers.index(train_labels[i])]=1
    # print(train_labels[i], train_onehot[i])
for i in range(len(test_onehot)):
    test_onehot[i][flowers.index(test_labels[i])]=1
    # print(test_labels[i], test_onehot[i])

# 建模
model_base = VGG19(weights='imagenet', include_top=False, input_shape=(224,224,3))
for layer in model_base.layers:
    layer.trainable = False

model = Sequential()
model.add(model_base)
model.add(GlobalAveragePooling2D())
model.add(Dense(256, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(17, activation='softmax')) # 要辨識 17 跟5種花卉唯一不一樣的地方
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy']
)

# 訓練
history = model.fit(
    train_imgs,
    train_onehot,
    batch_size = 64, # 記憶夠不夠時，改小一點
    epochs = 50,
    validation_data = (test_imgs, test_onehot)
)
model_path = './flower_17_model'

if os.path.exists(model_path):
    shutil.rmtree(model_path)
model.save(model_path)

import pylab as plt
plt.plot(history.history['accuracy'], label='training acc') # 訓練時的準確度
plt.plot(history.history['val_accuracy'], label='val acc') # 測試時的準確度
plt.plot(history.history['loss'], label='training loss') # 訓練時的損失率
plt.plot(history.history['val_loss'], label='val loss') # 測試時的損失率
plt.legend()
plt.show()
