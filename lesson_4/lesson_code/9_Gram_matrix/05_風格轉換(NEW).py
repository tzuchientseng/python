# 神經風格轉換技術 (Neural Style Transfer)
# 使用預訓練的 VGG19 模型進行內容圖像與風格圖像的融合
# 主要實現過程包括：
# 1. 初始化模型，提取內容與風格層的特徵。
# 2. 設置損失函數，包括內容損失與風格損失。
# 3. 使用梯度下降進行損失最小化，生成融合的最終圖像。

import os
import threading  # 用於多執行緒處理，防止主線程被阻塞
import cv2  # OpenCV 用於圖像處理
import keras  # Keras 深度學習框架
import numpy as np  # Numpy 用於數值計算
from keras.applications import VGG19  # 載入 VGG19 預訓練模型
from keras.applications.vgg19 import preprocess_input  # VGG19 的圖像預處理方法
import tensorflow as tf  # TensorFlow，用於梯度計算與優化器操作
import matplotlib.pyplot as plt  # Matplotlib 用於圖像可視化
import time  # 用於計算延遲
import shutil  # 用於操作文件與目錄

# 損失與梯度計算的函數，需實作
def compute_loss_grads(combination_img, base_img, style_img):
    """
    計算損失函數與梯度。
    - 內容損失：內容圖與合成圖在指定層的特徵差異。
    - 風格損失：風格圖與合成圖的多層格拉姆矩陣差異。
    使用自動微分 (tf.GradientTape) 計算梯度。

    Args:
        combination_img (tf.Variable): 合成圖像變數。
        base_img (np.array): 內容圖像數據。
        style_img (np.array): 風格圖像數據。

    Returns:
        loss (float): 損失函數值。
        grads (tf.Tensor): 損失函數的梯度。
    """
    # TODO: 根據指定模型層計算內容損失與風格損失
    pass

# 圖片後處理函數
def deprocess_img(img):
    """
    將 VGG19 預處理後的數據轉換為可視化的 RGB 圖像。
    調整亮度與像素範圍，並進行 BGR 到 RGB 的色彩空間轉換。

    Args:
        img (numpy array): 預處理後的圖像數據。

    Returns:
        numpy array: 解碼後的 RGB 圖像。
    """
    img = img.reshape((224, 224, 3))  # 將圖像數據調整為 224x224x3
    img = img[:, :, ::-1]  # BGR to RGB 色彩轉換
    img = np.clip(img, 0, 255).astype("uint8")  # 將數據範圍限制在 0-255 並轉換為 uint8
    return img

# 執行風格轉換的主函數
def run():
    """
    優化過程的主函數，進行多次迭代，更新合成圖像的數據。
    每次迭代計算損失函數與梯度，並使用優化器進行更新。
    同時顯示合成圖像的實時效果。
    """
    for i in range(iterations):
        # 計算損失與梯度
        loss, grads = compute_loss_grads(combination_img, base_img, style_img)
        
        # 使用優化器進行更新
        optimizer.apply_gradients([(grads, combination_img)])
        
        # 輸出當前迭代的損失
        print(f'Iteration {i+1}: loss={loss:.2f}')
        
        # 解碼並顯示當前的合成圖像
        img = deprocess_img(combination_img.numpy())  # 將合成圖像解碼為 RGB 格式
        ax.clear()  # 清除當前圖例
        ax.imshow(img)  # 顯示解碼後的圖像
        ax.axis('off')  # 隱藏座標軸
        plt.draw()  # 更新 Matplotlib 圖例
        time.sleep(0.01)  # 延遲以確保圖例刷新，建議高於 10ms

if __name__ == '__main__':
    # 加載 VGG19 預訓練模型，不包括全連接層 (include_top=False)
    model = VGG19(weights='imagenet', include_top=False)

    # 獲取模型的輸出字典，將層名稱與對應輸出關聯
    outputs_dict = dict([layer.name, layer.output] for layer in model.layers)
    model = keras.Model(inputs=model.inputs, outputs=outputs_dict)

    # 指定風格損失的提取層
    style_layer_names = [
        'block1_conv1',
        'block2_conv1',
        'block3_conv1',
        'block4_conv1',
        'block5_conv1'
    ]

    # 設置內容與風格損失的權重
    style_weight = 1e-6  # 風格損失權重，數值極小以控制影響
    content_weight = 2.5e-8  # 內容損失權重，數值極小以控制影響

    # 加載內容圖像
    base_img = cv2.imdecode(np.fromfile('./2.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    base_img = cv2.resize(base_img, (224, 224), interpolation=cv2.INTER_LINEAR)  # 調整大小
    base_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)  # BGR 轉 RGB
    base_img = np.expand_dims(base_img, axis=0)  # 添加批次維度
    base_img = preprocess_input(base_img)  # 預處理內容圖像數據

    # 加載風格圖像
    style_img = cv2.imdecode(np.fromfile('./starry_night.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    style_img = cv2.resize(style_img, (224, 224), interpolation=cv2.INTER_LINEAR)  # 調整大小
    style_img = cv2.cvtColor(style_img, cv2.COLOR_BGR2RGB)  # BGR 轉 RGB
    style_img = np.expand_dims(style_img, axis=0)  # 添加批次維度
    style_img = preprocess_input(style_img)  # 預處理風格圖像數據

    # 初始化合成圖像，初始數據與內容圖像相同
    combination_img = tf.Variable(base_img)

    # 設置迭代次數
    iterations = 4000

    # 初始化優化器，採用 SGD，並設置指數衰減學習率
    optimizer = keras.optimizers.SGD(
        tf.keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=100,  # 初始學習率
            decay_steps=100,  # 衰減步驟
            decay_rate=0.96  # 衰減率，每次降低 4%
        )
    )

    # 檢查輸出目錄是否存在，存在則刪除
    output_path = "output"
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)  # 創建輸出目錄

    # 初始化 Matplotlib 圖例
    fig, ax = plt.subplots()

    # 使用多執行緒運行優化過程，防止主線程被阻塞
    t = threading.Thread(target=run)
    t.start()
    plt.show()  # 顯示圖像
