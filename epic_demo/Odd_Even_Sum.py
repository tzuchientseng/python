print("----------------------------------------", 'Test', "-"*40)
# 設定數字範圍
start = 1
end = 100

# 初始化基數和偶數的總和
odd_sum = 0
even_sum = 0

# 使用迴圈來計算基數和偶數的總和
for number in range(start, end + 1):
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

# 輸出結果
print(f"偶數總和: {even_sum}")
print(f"基數總和: {odd_sum}")

print("----------------------------------------", 'Test', "-"*40)
# 設定數字範圍
start = 1
end = 100

# 初始化基數和偶數的總和
odd_sum = 0
even_sum = 0

# 使用迴圈並應用位元運算來計算基數和偶數的總和
for number in range(start, end + 1):
    if number & 1:
        odd_sum += number
    else:
        even_sum += number

# 輸出結果
print(f"偶數總和: {even_sum}")
print(f"基數總和: {odd_sum}")

print("----------------------------------------", 'Test', "-"*40)
# 設定數字範圍
start = 1
end = 100

# 使用列表推導式生成數字列表
numbers = [number for number in range(start, end + 1)]

# 初始化基數和偶數的總和
odd_sum = sum(number for number in numbers if number & 1)
even_sum = sum(number for number in numbers if not number & 1)

# 輸出結果
print(f"偶數總和: {even_sum}")
print(f"基數總和: {odd_sum}")

print("----------------------------------------", 'Test', "-"*40)
import numpy as np

# 設定數字範圍
start = 1
end = 100

# 使用 numpy 生成數字陣列
numbers = np.arange(start, end + 1)

# 使用位元運算和 numpy 的方法計算基數和偶數總和
odd_sum = np.sum(numbers[numbers % 2 == 1])
even_sum = np.sum(numbers[numbers % 2 == 0])

# 輸出結果
print(f"偶數總和: {even_sum}")
print(f"基數總和: {odd_sum}")

print("----------------------------------------", 'Test', "-"*40)
# 設定數字範圍
start = 1
end = 100

# 生成數字序列
numbers = range(start, end + 1)

# 使用 filter 和 lambda 函數篩選偶數和奇數
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 計算總和
odd_sum = sum(odd_numbers)
even_sum = sum(even_numbers)

# 輸出結果
print(f"偶數總和: {even_sum}")
print(f"基數總和: {odd_sum}")

print("----------------------------------------", 'Test', "-"*40)
from itertools import compress

# 設定數字範圍
start = 1
end = 100

# 生成數字序列
numbers = range(start, end + 1)

# 使用位元運算創建選擇器
odd_selector = [(x % 2 != 0) for x in numbers]
even_selector = [(x % 2 == 0) for x in numbers]

# 篩選奇數和偶數
odd_numbers = list(compress(numbers, odd_selector))
even_numbers = list(compress(numbers, even_selector))

# 計算總和
odd_sum = sum(odd_numbers)
even_sum = sum(even_numbers)

# 輸出結果
print(f"偶數總和: {even_sum}")
print(f"基數總和: {odd_sum}")

print("----------------------------------------", 'Test', "-"*40)