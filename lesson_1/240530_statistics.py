print("----------------------------------------", 'demo-bar', "-"*40)
import numpy as np                    # Import numpy module
import statistics as st               # Import statistics module
import matplotlib.pyplot as plt       # Import matplotlib.pyplot module
x = [60,10,40,80,80,30,60,90,50,60,\
     70,20,40,40,70,80,90,20,30,30,\
     60,50,80,10,40,20,80,80,80,20,\
     60,70,20,30,80,90,90,80,70,80]
print(f"Mean value = {np.mean(x)}")                  # Print the mean value of x
print(f"Median value = {np.median(x)}")              # Print the median value of x
print(f"Mode value = {st.mode(x)}")                  # Print the mode value of x

y = [0]*9                                            # Initialize a list y with 9 zeros
for s in x:                                          # Loop through each element in x
    if s == 10: y[0] += 1
    elif s == 20: y[1] += 1
    elif s == 30: y[2] += 1
    elif s == 40: y[3] += 1
    elif s == 50: y[4] += 1
    elif s == 60: y[5] += 1
    elif s == 70: y[6] += 1
    elif s == 80: y[7] += 1
    elif s == 90: y[8] += 1

width = 0.35                                       # Width of the bars
N = len(y)                                         # Number of bars
z = np.arange(N)                                   # Generate an array with N elements
plt.rcParams['font.family'] = 'Microsoft JhengHei' # Set the font
plt.bar(z, y, width=1)                               # Plot the bar chart
plt.ylabel('Number of People')                     # Label for y-axis
plt.xlabel('Score')                                # Label for x-axis
plt.xticks(z, ('10','20','30','40','50','60','70','80','90'))  # Set the x-axis ticks
plt.title('Score Distribution')                    # Title of the chart
plt.show()                                         # Show the chart

print("----------------------------------------", 'demo-two data', "-"*40)
import matplotlib.pyplot as plt
x = [60,10,40,80,80,30,60,90,50,60,
     70,20,40,40,70,80,90,20,30,30,
     60,50,80,10,40,20,80,80,80,20,
     60,70,20,30,80,90,90,80,70,80]

y = [60,10,40,70,80,30,60,90,50,60,
     70,20,40,40,70,80,90,20,30,30,
     60,50,80,10,40,20,70,80,70,20,
     60,70,40,40,80,70,90,80,70,60]
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.hist([x, y], 9) #9 intervals 
plt.title('SCORE DISTRIBUTION', fontsize = 20)
plt.xlabel("Group", fontsize = 16)
plt.ylabel("Count", fontsize = 16)
plt.show()

print("----------------------------------------", 'demo-pip install statistic', "-"*40)
import matplotlib as plt
import statistics as st
import numpy as np
print('----Mode----')
print('x', st.mode(x))
print('y', st.mode(y))
print('----Var----')
print('xVariance:', np.var(x))
print('xSampleVariance:', np.var(x, ddof = 1)) #Delta Degrees of Freedom.
print('yVariance:', np.var(y))
print('ySampleVariance:', np.var(y, ddof = 1)) #Delta Degrees of Freedom.
print("----")
print('xVariance:', st.pvariance(x))
print('xSampleVariance:', st.variance(x)) #Delta Degrees of Freedom.
print('yVariance:', st.pvariance(y))
print('ySampleVariance:', st.variance(y)) #Delta Degrees of Freedom.
print('----Dev----')
print('xDeviation:', np.std(x))
print('xSampleDeviation:', np.std(x, ddof = 1)) #Delta Degrees of Freedom.
print('yDeviation:', np.std(y))
print('ySampleDeviation:', np.std(y, ddof = 1)) #Delta Degrees of Freedom.
print("----")
print('xDeviation:', st.pstdev(x))
print('xSampleDeviation:', st.stdev(x)) #Delta Degrees of Freedom.
print('yDeviaton:', st.pstdev(y))
print('ySampleDeiation:', st.stdev(y)) #Delta Degrees of Freedom.
print("----correlation coefficient----")
print("correlation coefficient: ", np.corrcoef(x, y))

print("----------------------------------------", 'demo', "-"*40)
import numpy as np # numpy模組用來計算相關係數
import matplotlib.pyplot as plt # matplotlib用來繪圖

time = [60,10,40,80,80,30,60,90,50,60,
     70,20,40,40,70,80,90,20,30,30,
     60,50,80,10,40,20,80,80,80,20,
     60,70,20,30,80,90,90,80,70,80]

score = [60,10,40,70,80,30,60,90,50,60,
     70,20,40,40,70,80,90,20,30,30,
     60,50,80,10,40,20,70,80,70,20,
     60,70,40,40,80,70,90,80,70,60]
# 計算相關係數 correlation coeficient:相關係數介於-1到1之間
print('Correlation Coeficient:', np.corrcoef(time, score))
"""
time | score
----------------
time | 1 | -0.586
score|-0.586 | 1
"""

#最小平方直線 or 回歸直線 : y = ax + b
a = np.polyfit(time, score, 1)
b = np.poly1d(a)
# 畫出回歸線
plt.plot(time, b(time), color='red')

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.scatter(time, score)
plt.title('PHONE USING TIME', fontsize = 20)
plt.xlabel("Phone Screen time", fontsize = 16)
plt.ylabel("Score", fontsize = 16)
plt.show()

print("----------------------------------------", 'demo-One_way_ANOVA', "-"*40)
import scipy.stats as stats
group1 = [25, 30, 28, 35, 34]
group2 = [18, 22, 25, 20, 28]
group3 = [30, 24, 29, 27, 32]
a, b = stats.f_oneway(group1, group2, group3)
print("f-統計量: ", a)
print("p-值: ", b)
print("Reject H0: obvious different!") if b < 0.05 else print("Accecpt H0: No different!")
