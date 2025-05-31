# 二維Gram: 格拉姆矩陣
import numpy as np

# 初始化一個 3x5 的 numpy 陣列
a = np.array([[1, 2, 3, 4, 5], 
              [6, 7, 8, 9, 10], 
              [11, 12, 13, 14, 15]])
print("原始陣列 a:")
print(a)

# 將 a 轉置 90 度，變為 b
b = np.transpose(a, (1, 0))
print("\n轉置後的陣列 b:")
print(b)

# 將 b 扁平化，從列優先的順序取出數據
# 結果應該為: [1, 6, 11, 2, 7, 12, 3, 8, 13, 4, 9, 14, 5, 10, 15]
b_flattened = b.flatten(order='F')
print("\n扁平化後的陣列 b_flattened:")
print(b_flattened)

# 計算外積，a 的元素與 b_flattened 相乘
# a.shape = (3, 5) 與 b_flattened.shape = (15,)
# 外積的結果矩陣維度為 (3*5, 5*3) = (15, 15)
result = np.outer(a.flatten(), b_flattened)
print("\n外積結果矩陣:")
print(result)

# 對大陣列的推測:
# 假設輸入一張 800x600 的圖片，陣列有 600 列，800 行
# 格拉姆矩陣結果為 (600*800, 800*600) = (480,000, 480,000)
# 這樣的矩陣包含 2,304,000,000 個數字 (顯卡可能會OOM)
