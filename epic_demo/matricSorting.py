import numpy as np

# 創建一個隨機矩陣
matrix = np.random.randint(0, 10, size=(5, 5))
print("原始矩陣:")
print(matrix)

# 按行排序
sorted_matrix_by_row = np.sort(matrix, axis=1)
print("\n按行排序後的矩陣:")
print(sorted_matrix_by_row)

# 按列排序
sorted_matrix_by_column = np.sort(matrix, axis=0)
print("\n按列排序後的矩陣:")
print(sorted_matrix_by_column)

