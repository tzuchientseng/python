# 安裝必要的套件
# pip install opencv-python tensorflow==2.10.1 matplotlib

import numpy as np

# 設定隨機種子以確保結果可重現
np.random.seed(1)

# 產生兩個隨機向量 a 和 b，每個包含 3 個整數，範圍為 -100 至 100
a = np.random.randint(-100, 100, 3)
b = np.random.randint(-100, 100, 3)

# 印出隨機產生的向量
print("向量 a:")
print(a)
print("\n向量 b:")
print(b)

# 計算向量 a 與 b 的內積並手動驗算
# 內積計算公式：a.b = a1*b1 + a2*b2 + a3*b3
manual_dot = -63 * 37 + 40 * 33 + (-28) * (-21)
print("\n手動計算內積:")
print(manual_dot)

# 使用 NumPy 計算內積
numpy_dot = np.dot(a, b)
print("\n使用 NumPy 計算內積:")
print(numpy_dot)

# 結果解讀:
# a.b > 0: 向量方向大致相同，夾角在 0~90 度之間
# a.b = 0: 向量互相垂直，夾角為 90 度
# a.b < 0: 向量方向相反，夾角在 90~180 度之間
