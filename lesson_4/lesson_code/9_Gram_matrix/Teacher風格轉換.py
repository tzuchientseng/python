#Leno Gatys 等人發表的神經風格轉換技術(Neural style transfer)
#到目前還在持續修正其演算法，所以初學者只要了解其步驟及初步原理即可
# 1. 一開始，合成圖與原始內容圖一模一樣。
# 2. 計算原始內容與合成圖 “block5_conv2” 特徵損失
#   (因為合成後與原始圖盡可能的接近，才不會破壞原圖的整体架構，而 block5是點線的特徵，較不會破壞原圖)
#   然後再加上風格圖及合成圖的5個損失
# “block1_conv1”, “block2_conv1”, “block3_conv1”, “block4_conv1”, “block5_conv1” 5
# 層特徵的格拉姆損失。
# 3. 計算上述損失函數的梯度下降，進入優化器，產生合成圖。
# 4. 解開合成圖查看結果。
# 5. 重複 2~4 步驟 4000次。
#ps : 梯度下降 : 就是作微分。優化器逼進求極值(產生合成圖)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import threading
import cv2
import keras
import numpy as np
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input
import os
import shutil
import tensorflow as tf
#pip install matplotlib
import pylab as plt
import time
def gram_matrix(x):
    x=tf.reshape(x, (x.shape[1], x.shape[2], x.shape[3]))#h, w, c
    x=tf.transpose(x, (2,0,1))#c, h, w
    #features=tf.reshape(x, (tf.shape(x)[0], -1))
    features = tf.reshape(x, (x.shape[0], -1))
    #上述就會變成
    # [[r1, r2, r3....],
    #  [g1, g2, g3....],
    #  [b1, b2, b3....]]
    #底下需請同學請參照 03_格拉姆.py 的運算方式，了解其邏輯
    gram = tf.matmul(features, tf.transpose(features))#矩陣相乘
    return gram
def style_loss(style_feature, combination_feature):
    s=gram_matrix(style_feature)
    c=gram_matrix(combination_feature)
    channels=3
    size=width * height
    #官網建議再除以 (4*(channels**2)*(size**2))，依 RGB 3 Channel, 及圖片大小而縮小
    #使用 rsnet 的人，也調整這邊看看，讓風格照不要太強烈
    #使用 VGG19 也可以調整其它值看看，會有不同的風格
    return tf.reduce_sum(tf.square(s-c))/(4.0* (channels**2)*(size**2))
def compute_loss_grads(combination_img, base_img, style_img):
    #定義損失函數並設定梯度下降
    #梯度下降待下一章節說明 : 想像成就像要作一階微分，並採用逼進法求下一個值
    with tf.GradientTape() as tape:
        base_features=model(base_img)
        loss=tf.zeros(shape=())#純量 0
        base_feature=base_features['block5_conv2']
        combination_features=model(combination_img)
        combination_feature=combination_features['block5_conv2']
        #計算合成及原始的變異數，依迴歸線的方式計算，也可用 PCA, 請自行驗証
        #殘差平方總和通常會很大，所以就要再乘上一個極小的數, 比如1e-6(權重)，因此有沒有除以 n, 就沒差了
        #tf.reduce_sum()就是計算裏面的總和
        loss=loss+content_weight*tf.reduce_sum(#第一次時，因原始跟合成是一樣，所以 loss 為 0
            tf.square(combination_feature-base_feature)
        )
        style_features=model(style_img)
        for layer_name in style_layer_names:
            style_feature=style_features[layer_name]
            combination_feature=combination_features[layer_name]
            # 風格與合成的特徵要先轉格拉姆, 所以寫在 style_loss函數中
            style_loss_value=style_loss(style_feature, combination_feature)
            loss += style_weight * style_loss_value
    #正式作梯度下降
    grads=tape.gradient(loss, combination_img)
    return loss, grads
def deprocess_img(img):
    #todo :調整亮度, BGR=>RBG
    img = img.reshape((height, width, 3))#因為是 h, w, c
    # 底下是將亮度調亮
    img[:, :, 0] += 103.939
    img[:, :, 1] += 116.779
    img[:, :, 2] += 123.68
    img = img[:, :, ::-1].copy()#轉成 RGB格式
    #底下將 >255 改為 255，<0 改為0
    img = np.clip(img, 0, 255).astype("uint8")
    return img
def run():
    for i in range(iterations):
        loss, grads=compute_loss_grads(
            combination_img, base_img, style_img
        )#計算損失率及梯度下降
        optimizer.apply_gradients([(grads, combination_img)])#產生新的合成照
        print(f'Iteration {i+1}: loss={loss:.2f}')
        img=deprocess_img(combination_img.numpy())
        #UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
        #新執行緒照理說，是不能操控 UI元件的
        #在 PyQT5中，只有 UI 主執行緒才可控制 UI 元件
        #請參照 http://mahaljsp.asuscomm.com/index.php/2020/08/14/pyqt5_thread/
        #matplotlib 是使用 tkinter 套件完成視窗程式，tkinter 是個玩具，無法商業化，所以就無需理會其執行緒的運作
        #若不會使用執行緒，幾乎任何專案都寫不出來
        if i%100==0:
            ax.clear()
            ax.imshow(img)
            ax.axis('off')
            plt.draw()#更新圖例
            time.sleep(0.01)#不睡一下的話， plt會來不及更新，最好高於10ms, 視電腦的速度
if __name__=='__main__':
    model=VGG19(weights='imagenet', include_top=False)
    outputs_dict=dict([layer.name, layer.output] for layer in model.layers)
    model=keras.Model(inputs=model.inputs, outputs=outputs_dict)
    style_layer_names=['block1_conv1',
                       'block2_conv1',
                       'block3_conv1',
                       'block4_conv1',
                       'block5_conv1']

    #自已調整看看
    style_weight=1e-6/len(style_layer_names)#這些數值，都是測試出來的。損失函數計算出來的值，都會非常的大，所以要乘上極小的數字
    content_weight=2.5e-8#這些值可以自動化調整，但又是另一門課程

    base_img=cv2.imdecode(np.fromfile('./2.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)

    #將圖片調整為 800*600 或 600*450(4:3)
    original_height, original_width, _ = base_img.shape#假設是 1024*768
    height = 600

    #1024/768=w*600 => w* 1024*600/768
    width = round(original_width * height / original_height)
    base_img=cv2.resize(base_img, (width,height), interpolation=cv2.INTER_LINEAR)

    # rsnet 底下不用轉換，待查証
    base_img=cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)

    base_img=np.expand_dims(base_img, axis=0)
    base_img=preprocess_input(base_img)#將 RBG轉成 BGR

    style_img=cv2.imdecode(np.fromfile('./starry_night.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    style_img=cv2.resize(style_img, (width,height), interpolation=cv2.INTER_LINEAR)

    #rsnet 底下不用轉換，待查証
    style_img=cv2.cvtColor(style_img, cv2.COLOR_BGR2RGB)

    style_img=np.expand_dims(style_img, axis=0)
    style_img=preprocess_input(style_img)
    #一開始，合成照跟原始內容照一樣
    combination_img=tf.Variable(base_img)
    iterations=4000
    #優化器，採用SGD隨機, initial_learning_rate必需是小數
    optimizer=keras.optimizers.SGD(
        tf.keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=100.0, decay_steps=100, decay_rate=0.96#每次損失4%
        )
    )
    output_path="output"
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)
    #底下是優化過的，跟官網不一樣
    fig,ax=plt.subplots()
    t=threading.Thread(target=run)
    t.start()
    plt.show()