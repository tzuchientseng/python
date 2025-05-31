"""
https://www.youtube.com/watch?v=wm9yR1VspPs
pip install matplotlib ipywidgets
pip install notebook
jupyter notebook
"""

import pandas as pd 
import matplotlib.pyplot as plt
from ipywidgets import interact

# 設置字體
plt.rcParams['font.family'] = 'Microsoft JhengHei'

# 讀取數據
url = 'https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv'
data = pd.read_csv(url)

# 提取特徵和標籤
x = data['YearsExperience']
y = data['Salary']

# 初始化參數
w, b = 0, 0

# 定義繪圖函數
def plot_pred(w, b):
    y_pred = x * w + b
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, marker='x', color='red', label='真實線')
    plt.plot(x, y_pred, color='blue', label='預測線')
    plt.legend(loc='best')
    plt.title("Employee", fontsize=16)
    plt.xlabel("years", fontsize=14)
    plt.ylabel("salary (千) per month", fontsize=14)
    plt.axis([0, 12, -60, 140])  # 設置坐標範圍
    plt.show()

# 繪製初始圖
plot_pred(0, 10)

"""
# 使用 interact 進行互動式調整
interact(plot_pred, w=(-100, 100, 1), b=(-100, 100, 1))
"""
