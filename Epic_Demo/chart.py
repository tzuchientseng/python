"""
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] 和 plt.rcParams['font.family']='Microsoft JhengHei' 的差別在於設定的字型類型和具體使用的字型名稱：

字型類型：

plt.rcParams['font.sans-serif'] 是設定無襯線字型的參數，當你使用無襯線字型時（例如 plt.rcParams['font.family'] = 'sans-serif'），它會使用你設定的 Microsoft YaHei。
plt.rcParams['font.family'] 是設定整體字型家族的參數，不僅限於無襯線字型。它可以是任何字型家族，例如 serif（襯線字型）、sans-serif（無襯線字型）、monospace（等寬字型）等。
具體字型名稱：

Microsoft YaHei 是微軟提供的一種無襯線字型，適合用於顯示簡體中文。
Microsoft JhengHei 是微軟提供的一種黑體字型，專門用於顯示繁體中文。
"""
print("----------------------------------------", 'demo-plot', "-"*40)
import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539]
BMW = [4000, 3590, 4423]
Lexus = [5200, 4930, 5350]

years = [2021, 2022, 2023]
plt.rcParams['font.family']='Microsoft JhengHei'#建立中文字體
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.xticks(years)

plt.plot(years, Benz, '-.*', label='Benz')
plt.plot(years, BMW, '-o', label='BMW')
plt.plot(years, Lexus, '-v', label='Lexus')
plt.legend(loc='best') # Adding legend with (label)

plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.grid(True)  # Adding grid for better readability
plt.tick_params(axis='both', which='major', labelsize=12, labelcolor='gray')  # Customizing tick parameters


plt.show()

print("----------------------------------------", 'demo-Scatter', "-"*40)
import matplotlib.pyplot as plt

# Data
hour = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
work = [80, 95, 65, 70, 49, 39, 2, 45, 99, 100]

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(hour, work, color='blue', marker='o', s=100, edgecolor='k')

# Add titles and labels
plt.title("Employee Work Scores Over Hours", fontsize=16)
plt.xlabel("Hours", fontsize=14)
plt.ylabel("Work Score", fontsize=14)

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add data labels
for i in range(len(hour)):
    plt.text(hour[i], work[i], f"({hour[i]}, {work[i]})", fontsize=9, ha='right')

# Show the plot
plt.show()


print("----------------------------------------", 'demo-bar', "-"*40)
import matplotlib.pyplot as plt
goods = ['a', 'b', 'c', 'd']
sell = [69, 79, 49, 59]
index = range(len(goods))  # generate the x-ticks

plt.figure(figsize=(10, 6))  # set the figure size for better readability
plt.bar(index, sell, color='skyblue', width=0.8)  # add color for better visualization; width default = 0.8
plt.xticks(index, goods)  # pair index with goods
plt.xlabel('goods')  # label for the x-axis
plt.ylabel('units sold')  # label for the y-axis
plt.title('sales of goods')  # title of the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)  # add grid lines for the y-axis

plt.tight_layout()  # adjust layout to make room for the labels
plt.show()
"""
import matplotlib.pyplot as plt

# 假設有一組銷售數據
sales_data = [59, 65, 75, 55, 45, 70, 60, 80, 90]
categories = [f'Item {i+1}' for i in range(len(sales_data))]

plt.figure(figsize=(10, 6))  # Set the figure size for better readability (width:10, height:6)
bars = plt.bar(categories, sales_data, color='skyblue', edgecolor='black')  # Create the bar chart

# 在每個柱狀上方顯示數據點的高度
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             int(bar.get_height()), ha='center', va='bottom')

plt.xlabel('Items')  # Label for the x-axis
plt.ylabel('Units Sold')  # Label for the y-axis
plt.title('Sales Data')  # Title of the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for the y-axis

plt.tight_layout()  # Adjust layout to make room for the labels
plt.show()
"""
print("----------------------------------------", 'demo-histogram', "-"*40)
import matplotlib.pyplot as plt
import numpy as np

# 假設有一組銷售數據
sales_data = [59, 65, 75, 55, 45, 70, 60, 80, 90]

plt.figure(figsize=(10, 6))  # Set the figure size for better readability (width:10, height:6)
n, bins, patches = plt.hist(sales_data, bins=5, color='skyblue', edgecolor='black')  # Create the histogram

# 在每個柱狀上方顯示數據點的高度
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width() / 2, patches[i].get_height(),
             int(n[i]), ha='center', va='bottom')

plt.xlabel('Units Sold')  # Label for the x-axis
plt.ylabel('Frequency')  # Label for the y-axis
plt.title('Distribution of Sales Data')  # Title of the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for the y-axis

plt.tight_layout()  # Adjust layout to make room for the labels
plt.show()
"""
import matplotlib.pyplot as plt
goods = ['a', 'b', 'c', 'd']
sell = [69, 79, 49, 59]
index = range(len(goods))  # generate the x-ticks

plt.figure(figsize=(10, 6))  # set the figure size for better readability
plt.bar(index, sell, color='skyblue', width=1)  # add color for better visualization; width default = 0.8
plt.xticks(index, goods)  # pair index with goods
plt.xlabel('goods')  # label for the x-axis
plt.ylabel('units sold')  # label for the y-axis
plt.title('sales of goods')  # title of the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)  # add grid lines for the y-axis

plt.tight_layout()  # adjust layout to make room for the labels
plt.show()
"""
print("----------------------------------------", 'demo-barh', "-"*40)
# import matplotlib.pyplot as plt
goods = ['A', 'B', 'C', 'D']
sell = [69, 79, 49, 59]
index = range(len(goods))  # Generate the y-ticks

plt.figure(figsize=(10, 6))  # Set the figure size for better readability
plt.barh(index, sell, color='skyblue')  # Add color for better visualization
plt.yticks(index, goods)  # Set the y-ticks to correspond to the goods
plt.xlabel('Units Sold')  # Label for the x-axis
plt.ylabel('Goods')  # Label for the y-axis
plt.title('Sales of Goods')  # Title of the chart
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add grid lines for the x-axis

plt.tight_layout()  # Adjust layout to make room for the labels
plt.show()

print("----------------------------------------", 'demo-pie', "-"*40)
import matplotlib.pyplot as plt

# Data for the pie chart
language = ["Chinese", "English", "Japanese", "French"]
rate = [0.4, 0.26, 0.22, 0.12]

plt.pie(rate, labels=language, autopct='%1.1f%%', startangle=140) # Create a pie chart with percentage labels
plt.axis("equal") # Ensure the pie chart is a circle
plt.title("Language Proficiency Rates") # Add a title to the pie chart
plt.show() # Display the pie chart

print("----------------------------------------", 'demo-pie_explode', "-"*40)
import matplotlib.pyplot as plt

# Data for the pie chart
language = ["Chinese", "English", "Japanese", "French"]
rate = [0.4, 0.26, 0.22, 0.12]
expl = [0.0, 0.0, 0.0, 0.2]
plt.pie(rate, labels=language, explode=expl, autopct='%1.1f%%', startangle=10) # Create a pie chart with percentage labels
plt.axis("equal") # Ensure the pie chart is a circle
plt.title("Language Proficiency Rates") # Add a title to the pie chart
plt.show() # Display the pie chart

print("----------------------------------------", 'demo', "-"*40)
import numpy as np  # numpy module used to calculate correlation coefficient
import matplotlib.pyplot as plt  # matplotlib used for plotting
time = [
    60, 10, 40, 80, 80, 30, 60, 90, 50, 60,
    70, 20, 40, 40, 70, 80, 90, 20, 30, 30,
    60, 50, 80, 10, 40, 20, 80, 80, 80, 20,
    60, 70, 20, 30, 80, 90, 90, 80, 70, 80
]
score = [
    60, 10, 40, 70, 80, 30, 60, 90, 50, 60,
    70, 20, 40, 40, 70, 80, 90, 20, 30, 30,
    60, 50, 80, 10, 40, 20, 70, 80, 70, 20,
    60, 70, 40, 40, 80, 70, 90, 80, 70, 60
]

# Calculate correlation coefficient: ranges between -1 and 1
correlation = np.corrcoef(time, score)
print('Correlation Coefficient:', correlation)
"""
time | score
----------------
time | 1 | -0.586
score|-0.586 | 1
"""

# Least squares line or regression line: y = ax + b
a = np.polyfit(time, score, 1)
b = np.poly1d(a)

plt.plot(time, b(time), color='red') # Plot the regression line
plt.rcParams['font.family'] = 'Microsoft JhengHei' # Set font to Microsoft JhengHei for better readability
plt.scatter(time, score) # Plot data points

# Add titles and labels
plt.title('PHONE USING TIME', fontsize=20)
plt.xlabel("Phone Screen Time", fontsize=16)
plt.ylabel("Score", fontsize=16)
plt.show()
import matplotlib as plt
import statistics as st
import numpy as np
print('----Mode----')
print('time', st.mode(time))
print('score', st.mode(score))
print('----Var----')
print('timeVariance:', np.var(time))
print('timeSampleVariance:', np.var(time, ddof = 1)) #Delta Degrees of Freedom.
print('scoreVariance:', np.var(score))
print('scoreSampleVariance:', np.var(score, ddof = 1)) #Delta Degrees of Freedom.
print("----")
print('timeVariance:', st.pvariance(time))
print('timeSampleVariance:', st.variance(time)) #Delta Degrees of Freedom.
print('scoreVariance:', st.pvariance(score))
print('scoreySampleVariance:', st.variance(score)) #Delta Degrees of Freedom.
print('----Dev----')
print('timeDeviation:', np.std(time))
print('timeSampleDeviation:', np.std(time, ddof = 1)) #Delta Degrees of Freedom.
print('scoreDeviation:', np.std(score))
print('scoreSampleDeviation:', np.std(score, ddof = 1)) #Delta Degrees of Freedom.
print("----")
print('timeDeviation:', st.pstdev(time))
print('timeSampleDeviation:', st.stdev(time)) #Delta Degrees of Freedom.
print('scoreDeviaton:', st.pstdev(score))
print('scoreSampleDeiation:', st.stdev(score)) #Delta Degrees of Freedom.
print("----correlation coefficient----")
print("correlation coefficient: ", np.corrcoef(time, score))

print("----------------------------------------", 'demo', "-"*40)
print("----------------------------------------", 'demo', "-"*40)
print("----------------------------------------", 'demo', "-"*40)
print("----------------------------------------", 'demo', "-"*40)
print("----------------------------------------", 'demo-bar', "-"*40)
import matplotlib.pyplot as plt

# 創建一個圖形並設置大小
plt.figure(figsize=(10, 6))

# 繪製一些數據
index = [1, 2, 3, 4, 5]
sell = [10, 20, 15, 25, 30]
plt.bar(index, sell, color='skyblue', width=1)

# 顯示圖形
plt.show()
import matplotlib.pyplot as plt

# 創建一個圖形並設置大小和解析度
plt.figure(figsize=(10, 6), dpi=100)

# 繪製一些數據
index = [1, 2, 3, 4, 5]
sell = [10, 20, 15, 25, 30]
plt.bar(index, sell, color='skyblue', width=1)

# 顯示圖形
plt.show()
import matplotlib.pyplot as plt

# 第一個圖形
plt.figure(figsize=(10, 6))
index1 = [1, 2, 3, 4, 5]
sell1 = [10, 20, 15, 25, 30]
plt.bar(index1, sell1, color='skyblue', width=1)
plt.title('Figure 1')

# 第二個圖形
plt.figure(figsize=(8, 5))
index2 = [1, 2, 3, 4, 5]
sell2 = [30, 25, 20, 15, 10]
plt.bar(index2, sell2, color='salmon', width=1)
plt.title('Figure 2')

# 顯示圖形
plt.show()
import matplotlib.pyplot as plt

# 創建一個圖形並設置大小
plt.figure(figsize=(12, 6))

# 第一個子圖
plt.subplot(1, 2, 1)
index1 = [1, 2, 3, 4, 5]
sell1 = [10, 20, 15, 25, 30]
plt.bar(index1, sell1, color='skyblue', width=1)
plt.title('Subplot 1')

# 第二個子圖
plt.subplot(1, 2, 2)
index2 = [1, 2, 3, 4, 5]
sell2 = [30, 25, 20, 15, 10]
plt.bar(index2, sell2, color='salmon', width=1)
plt.title('Subplot 2')

# 顯示圖形
plt.show()
import matplotlib.pyplot as plt
goods = ['a', 'b', 'c', 'd']
sell = [69, 79, 49, 59]
index = range(len(goods))  # generate the x-ticks

plt.figure(figsize=(10, 6))  # set the figure size for better readability
plt.bar(index, sell, color='skyblue', width=0.8)  # add color for better visualization; width default = 0.8
plt.xticks(index, goods)  # pair index with goods
plt.xlabel('goods')  # label for the x-axis
plt.ylabel('units sold')  # label for the y-axis
plt.title('sales of goods')  # title of the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)  # add grid lines for the y-axis

plt.tight_layout()  # adjust layout to make room for the labels
plt.show()

print("----------------------------------------", 'demo', "-"*40)
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)

# 建立 2 個子圖
fig, ax = plt.subplots(1, 2, figsize=(8, 4), subplot_kw={'projection': '3d'})

# 繪製曲線表面圖
ax[0].plot_surface(X, Y, Z, cmap="bwr")  # cmap設置顏色新層為 藍-白-紅
ax[0].set_title('Draw curve surface plot', fontsize=7, color='gray')

# 繪製曲線框線圖
ax[1].plot_wireframe(X, Y, Z, color='g')
ax[1].set_title('Draw curve frame line drawing', fontsize=7, color='gray')

plt.show()

print("----------------------------------------", 'demo', "-"*40)
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (1.2-x**2+y*5)*np.exp(-x**2-y**2)

x = np.linspace(-3.0, 3.0, 100)  # 模擬 生成 -3 到 3 之間 100的數據
y = np.linspace(-3.0, 3.0, 100)

X, Y = np.meshgrid(x, y)  # 將上述生成的數據形成座標
Z = f(X, Y)  # 將座標帶入函數

# 建立 2 個子圖
fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# 繪製等高圖
con = ax[0].contourf(X, Y, Z, cmap='Greens')  # 填充輸出圖
plt.colorbar(con, ax=ax[0])  # 加入顏色條(左圖右邊的長條)
oval = ax[0].contour(X, Y, Z, colors='b')  # 輸出圖
ax[0].clabel(oval, colors='b')  # 增加高度標記
ax[0].set_title('等高圖', fontsize=16, color='b')

# 繪製等高圖 level=12
ax[1].contourf(X, Y, Z, 12, cmap='Greens')  # 填充輸出圖
oval = ax[1].contour(X, Y, Z, 12, colors='b')  # 輸出圖
ax[1].clabel(oval, colors='b')  # 增加高度標記
ax[1].set_title('等高圖level=12', fontsize=16, color='b')

plt.show()

print("----------------------------------------", 'demo', "-"*40)
import matplotlib.pyplot as plt
import numpy as np

z = np.linspace(0, 1, 300)  # z 軸值
x = z * np.sin(30 * z)      # x 軸值
y = z * np.cos(30 * z)      # y 軸值
colors = x + y              # 色彩是沿 x + y 累增

# 建立 2 個子圖
fig, ax = plt.subplots(1, 2, figsize=(8, 4), subplot_kw={'projection': '3d'})
ax[0].scatter(x, y, z, c=colors)  # 繪製左圖
ax[1].scatter(x, y, z, c=colors, cmap='hsv')  # 繪製右圖
ax[1].set_axis_off()  # 關閉軸線
plt.show()

print("----------------------------------------", 'demo-kbar', "-"*40)
import csv
import matplotlib.pyplot as plt

x = 'XXX.csv'

with open(x, encoding='utf-8') as y:
    z = csv.reader(y)
    a = list(z)

def kbar(Open, Close, High, Low, Pos):
    if Close > Open:
        color = 'red'
        height = Close - Open
        bottom = Open
    else:
        color = 'green'
        height = Open - Close
        bottom = Close
    
    plt.bar(Pos, height=height, bottom=bottom, width=0.8, color=color)
    plt.vlines(Pos, High, Low, color)

day = []
for i in range(1, len(a)):
    day.append(a[i][0])
    kbar(float(a[i][1]), float(a[i][4]), float(a[i][2]), float(a[i][3]), i)

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.xticks(range(len(day)), day)
plt.grid()
plt.title('2330 台積電蠟燭 K線圖')
plt.xlabel('日期')
plt.ylabel('股價')
plt.show()

print("----------------------------------------", 'demo-kbar', "-"*40)
# pip install mplfinance
import pandas as pd
import mplfinance as mpf

# 並且包含標題：Date,Open,High,Low,Close,Volume
file_path = 'XXX.csv'

# 讀取CSV文件
df = pd.read_csv(file_path, index_col=0, parse_dates=True)

# 檢查讀取的數據
print(df.head())

# 繪製K線圖
mpf.plot(df, type='candle', style='charles', title='2330 台積電蠟燭 K線圖', ylabel='股價', volume=True)

print("----------------------------------------", 'demo-kbar', "-"*40)
import matplotlib.pyplot as plt
import numpy as np

# 標籤名稱
labels = ['類別1', '類別2', '類別3', '類別4']
# 每組中的數據
data1 = [4, 7, 3, 5]
data2 = [2, 4, 6, 4]
data3 = [3, 5, 4, 6]

# 設置X軸的位置
x = np.arange(len(labels))  # [0, 1, 2, 3]
width = 0.2  # 長條的寬度

fig, ax = plt.subplots()

# 繪製每組的長條
rects1 = ax.bar(x - width, data1, width, label='數列1')
rects2 = ax.bar(x, data2, width, label='數列2')
rects3 = ax.bar(x + width, data3, width, label='數列3')

# 添加一些文字標籤
ax.set_xlabel('類別')
ax.set_ylabel('數值')
ax.set_title('分組長條圖')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()
