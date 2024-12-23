"""
Leno Gatys 等人發表的神經風格轉換技術(Neural style transfer)
到目前還在持續修正其演算法，所以初學者只要了解其步驟及初步原理即可
1. 一開始，合成圖與原始內容圖一模一樣。
2. 計算原始內容與合成圖 “block5_conv2” 特徵損失
  (因為合成後與原始圖盡可能的接近，才不會破壞原圖的整体架構，而 block5是點線的特徵，較不會破壞原圖)
  然後再加上風格圖及合成圖的5個損失
“block1_conv1”, “block2_conv1”, “block3_conv1”, “block4_conv1”, “block5_conv1” 5
層特徵的格拉姆損失。
3. 計算上述損失函數的梯度下降，進入優化器，產生合成圖。
4. 解開合成圖查看結果。
5. 重複 2~4 步驟 4000次。
ps : 梯度下降 : 就是作微分。優化器逼進求極值(產生合成圖)
"""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import threading
import cv2
import keras
import numpy as np
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input
import os
import shutil
import tensorflow as tf
import pylab as plt
import time

def compute_loss_grads(combination_img, base_img, style_img):
    pass

def deprocess_img(img):
    # todo :調整亮度, BGR=>RBG, # np.clip
    return img

def run():
    for i in range(iterations):
        loss, grads=compute_loss_grads(
            combination_img, base_img, style_img
        ) # 計算損失率及梯度下降
        optimizer.apply_gradients([(grads, combination_img)]) # 產生新的合成照
        print(f'Iteration {i+1}: loss={loss:.2f}')
        img = deprocess_img(combination_img.numpy())
        ax.clear()
        ax.imshow(img)
        ax.axis('off')
        plt.draw() # 更新圖例
        time.sleep(0.01) # 不睡一下的話， plt會來不及更新，最好高於10ms, 視電腦的速度

if __name__=='__main__':

    # 隱藏層移到全連接層
    model = VGG19(weights='imagenet', include_top=False)
    outputs_dict = dict([layer.name, layer.output] for layer in model.layers)
    model = keras.Model(inputs=model.inputs, outputs=outputs_dict)
    style_layer_names = ['block1_conv1',
                         'block2_conv1',
                         'block3_conv1',
                         'block4_conv1',
                         'block5_conv1']
    style_weight = 1e-6 # 這些數值，都是測試出來的。損失函數計算出來的值，都會非常的大，所以要乘上極小的數字
    content_weight = 2.5e-8 # 這些值可以自動化調整，但又是另一門課程

    base_img = cv2.imdecode(np.fromfile('./2.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED) # imread 不能讀取中文路徑
    base_img = cv2.resize(base_img, (224,224), interpolation=cv2.INTER_LINEAR)
    base_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
    base_img = np.expand_dims(base_img, axis=0)
    base_img = preprocess_input(base_img)

    style_img = cv2.imdecode(np.fromfile('./starry_night.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    style_img = cv2.resize(style_img, (224,224), interpolation=cv2.INTER_LINEAR)
    style_img = cv2.cvtColor(style_img, cv2.COLOR_BGR2RGB)
    style_img = np.expand_dims(style_img, axis=0)
    style_img = preprocess_input(style_img)

    # 一開始，合成照跟原始內容照一樣
    combination_img = tf.Variable(base_img)
    iterations = 4000
    # 優化器，採用SGD隨機

    optimizer=keras.optimizers.SGD(
        tf.keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=100, decay_steps=100, decay_rate=0.96 # 每次損失4%
        )
    )
    output_path = "output"
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)
    # 底下是優化過的，跟官網不一樣
    fig, ax = plt.subplots()
    t = threading.Thread(target=run)
    t.start()
    plt.show()
