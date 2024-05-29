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
goods = ['A', 'B', 'C', 'D']
sell = [69, 79, 49, 59]
index = range(len(goods))  # Generate the x-ticks

plt.figure(figsize=(10, 6))  # Set the figure size for better readability
plt.bar(index, sell, color='skyblue')  # Add color for better visualization
plt.xticks(index, goods)  # Pair index with goods
plt.xlabel('Goods')  # Label for the x-axis
plt.ylabel('Units Sold')  # Label for the y-axis
plt.title('Sales of Goods')  # Title of the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for the y-axis

plt.tight_layout()  # Adjust layout to make room for the labels
# plt.show()

print("----------------------------------------", 'demo-histogram', "-"*40)
import matplotlib.pyplot as plt
import numpy as np

# 假設有一組銷售數據
sales_data = [59, 65, 75, 55, 45, 70, 60, 80, 90]

plt.figure(figsize=(10, 6))  # Set the figure size for better readability
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
