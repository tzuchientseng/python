# 統計學與 AI 的觀點
# 統計學 : 使用歷史資料，預測未來的事。
# 變異數 (Variance)
# 標準差 (Standard Deviation)
# 程式三大挑戰 : 迴圈、資料結構、物件導向

import numpy as np

# 設定隨機種子以確保結果可重現
np.random.seed(1)

# 生成一個包含 10 個隨機整數的陣列，範圍為 1 至 100
a = np.random.randint(1, 100, 10)
print("隨機生成的陣列 a:")
print(a)

# 計算標準差的公式：
# 標準差 = sqrt((所有數字 - 平均數)^2 的總和 / 總數)

# 使用手動方法計算標準差
sum = 0
mean = a.mean()  # 計算平均數
for i in a:
    sum += (i - mean) ** 2  # 累加每個數字與平均數的平方差
variance = sum / len(a)  # 變異數 = 平方差總和 / 總數
manual_std = variance ** 0.5  # 標準差 = 變異數的平方根

# 輸出手動計算的標準差
print("\n手動計算標準差:")
print(manual_std)

# 使用 NumPy 計算標準差
numpy_std = np.std(a)
print("\n使用 NumPy 計算標準差:")
print(numpy_std)

# 使用 NumPy 計算變異數
numpy_variance = np.var(a)
print("\n使用 NumPy 計算變異數:")
print(numpy_variance)
