"""
1.Plotting data: x, y, 型態(線的樣式), 線名稱(label), legend loc (label)
2.標題 X, y 名稱
3.刻度調整(xticks, x最大最小與y最大最小, 網格)
4.文字加入 show()
"""
print("----------------------------------------", 'demo-matplotlib.pylot', "-"*40)
import matplotlib.pyplot as plt
y = [8, 12, 24, 28, 10, 23, 3, 3, 34, 23]
x = [x for x in range(len(y))]

# plt.plot(x, y)
plt.plot(x, y, '-o',lw=8, label="sample",) #line width
plt.legend(loc="best") #這行為圖表添加圖例(label)，使用前面行中指定的標籤。

plt.title("Data")
plt.xlabel("x")
plt.ylabel("y")

plt.xticks(x)
plt.axis([0, 10, 0, 50])
plt.grid()

plt.show()

print("----------------------------------------", 'demo-matplotlib.pylot', "-"*40)
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, label='Quadratic')
plt.plot(x, y2, label='Linear')
plt.legend(loc="best")
plt.show()

print("----------------------------------------", 'demo-employee number', "-"*40)
import matplotlib.pyplot as plt
x = [x for x in range(1, 13)]
y = [118, 131, 138, 145, 157, 175,
     142, 136, 129, 125, 116, 107]

plt.plot(x, y,'-o', label='num', lw =5)
plt.legend(loc="best") #這行為圖表添加圖例(label)，使用前面行中指定的標籤。
plt.title("Employee Number", fontsize = 17)
plt.xlabel("Month", fontsize = 14)
plt.ylabel("Number", fontsize = 14)
plt.grid()
plt.show()

print("----------------------------------------", 'demo', "-"*40)
import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]  
data2 = [1, 3, 6, 10, 15, 21, 28, 36] 
data3 = [4, 4, 4, 4, 4, 4, 4, 4] 
data4 = [1, 3, 6, 10, 15, 21, 28, 36] 

seq = [1,2,3,4,5,6,7,8] 
# plt.plot(seq, data1, 'r--', 
#          seq, data2, 'g.')
plt.plot(seq, data1, 'r--*', label='Data 1')
plt.plot(seq, data2, 'g-o', label='Data 2')
plt.plot(seq, data3, 'r-^', label='Data 3')
plt.plot(seq, data4[::-1], 'b->', label='Data 4')
plt.legend(loc="best")
plt.title("Test Chart", fontsize=24)  
plt.xlabel("x-Value", fontsize=14) 
plt.ylabel("y-Value", fontsize=14)  
plt.tick_params(axis='both', labelsize=12, color='blue') 
plt.show()

print("----------------------------------------", 'demo', "-"*40)
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
plt.tick_params(axis='both', which='major', labelsize=12, labelcolor='blue')  # Customizing tick parameters

plt.legend()  # Adding legend

plt.show()


print("----------------------------------------", 'demo-Scatter', "-"*40)
import matplotlib.pyplot as plt
hour = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
work = [80, 95, 65, 70, 49, 39, 2, 45, 99, 100]
plt.scatter(hour, work)
plt.show()
