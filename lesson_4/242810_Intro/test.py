# .\venv\Scripts\activate
# python test.py
# .\venv\Scripts\python test.py

# 測試抓 CPU / GPU
"""
import tensorflow as tf

gpus = tf.config.list_physical_devices(device_type="GPU")
cpus = tf.config.list_physical_devices(device_type="CPU")

print("GPUs:", gpus)
print("CPUs:", cpus)
print("GPU Available:", tf.test.is_gpu_available())

# import tensorflow as tf

# # 顯示可用的 GPU
# gpus = tf.config.list_physical_devices('GPU')
# print("Available GPUs:", gpus)

# if gpus:
#     with tf.device('/GPU:0'):
#         a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
#         b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
#         c = tf.matmul(a, b)
#         print("GPU computation result:\n", c)
# else:
#     print("No GPUs found.")
"""

# 測試畫圖
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0, 1, 10000)
y = np.random.uniform(0, 1, 10000)
plt.scatter(x, y)

x = np.random.uniform(0, 1, 1000)
y = np.random.uniform(0, 1, 1000)

plt.scatter(x, y, c='r')
plt.show()
"""

# numpy 計算數量
"""
import numpy as np
np.random.seed(1)
d = np.random.uniform(0, 1, 10)
# print(np.where(d<0.01))
# print(np.where(d<0.01)[0])
print(np.where(d<0.01)[0].shape[0])
"""

# 呼叫 SunnySdk
"""
import cv2
from SunnySdk import SunnySdk

img = SunnySdk.read('老虎.jpg')
cv2.imshow("tiger",img)
cv2.waitKey(0)
"""
