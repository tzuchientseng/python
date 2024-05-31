"""
1.Plotting data: x, y, 型態(線的樣式), 線名稱(label), legend loc (label)
2.標題 X, y 名稱
3.刻度調整(xticks, x最大最小與y最大最小, 網格)
4.文字加入 show()
"""
print("----------------------------------------", 'demo-plot', "-"*40)
import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539]
BMW = [4000, 3590, 4423]
Lexus = [5200, 4930, 5350]

years = [2021, 2022, 2023]

plt.xticks(years)
plt.legend(loc='best')  

plt.plot(years, Benz, '-.*', label='Benz')
plt.plot(years, BMW, '-o', label='BMW')
plt.plot(years, Lexus, '-v', label='Lexus')

plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.grid(True)  # Adding grid for better readability
plt.tick_params(axis='both', which='major', labelsize=12, labelcolor='gray')  # Customizing tick parameters

plt.legend()  # Adding legend

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