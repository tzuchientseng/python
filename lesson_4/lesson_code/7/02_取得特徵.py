import os
import keras
import numpy as np
from keras.applications.vgg19 import preprocess_input

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
import tensorflow as tf
from keras.applications import VGG19
model=VGG19(weights='imagenet', include_top=False)
outputs_dict=dict([(layer.name, layer.output) for layer in model.layers])
#將隱藏層移到輸出層(全連接層)
model=keras.Model(inputs=model.inputs, outputs=outputs_dict)

img=cv2.imdecode(np.fromfile('./starry_night.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
img=cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img=np.expand_dims(img, axis=0)
img=preprocess_input(img)
outputs=model.predict(img)
#也可以直接使用 model(img)
#再還沒有把圖放入model前，底下的維度都是(None, None, None, 3)
# input_1 (1, 224, 224, 3) : 224*224有3張圖
# block1_conv1 (1, 224, 224, 64) : 224*224 有 64張圖
# block1_conv2 (1, 224, 224, 64)
for layer_name in outputs:
     print(layer_name, outputs[layer_name].shape)
c11=outputs['block1_conv1']
r, h, w, c=c11.shape
c11=tf.reshape(c11,(h, w, c))
# .numpy() : 將 tensorflow格式轉成 numpy 格式
# print(c11[:,:,0].numpy())
import pylab as plt
for i in range(64):
    plt.subplot(8,8,i+1)
    img=np.reshape(c11[:,:,i].numpy(), (h, w, 1))#1, 只有一個顏色，為灰階色
    plt.imshow(img, cmap='gray')#灰階色一定要使用 cmap(色盤)
    plt.axis("off")
plt.show()
#所以總共有 64*2+128*2+256*4+512*8 = 5504張特徵圖
#若有10000張圖片，就要計算5504*10000個權重