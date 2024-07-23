print("----------------------------------------", 'demo-one_way_anova', "-"*40)
import scipy.stats as stats
group1 = [25, 30, 28, 35, 34]
group2 = [18, 22, 25, 20, 28]
group3 = [30, 24, 29, 27, 32]
a, b = stats.f_oneway(group1, group2, group3)
print("f-統計量: ", a)
print("p-值: ", b)
print("reject h0: obvious different!") if b < 0.05 else print("accecpt h0: no different!")

print("----------------------------------------", 'pip install panda', "-"*40)
print("----------------------------------------", 'demo-two_way_avona', "-"*40)
import scipy.stats as stats
import pandas as pd

data = {
    'method_a_male': [85, 88, 84, 79, 90],
    'method_a_female': [82, 87, 88, 90, 84],
    'method_b_male': [78, 82, 80, 85, 88],
    'method_b_female': [75, 80, 78, 83, 86],
    'method_c_male': [92, 94, 89, 87, 95],
    'method_c_female': [88, 93, 91, 85, 90]
}

df = pd.DataFrame(data)

result = stats.f_oneway(df['method_a_male'], df['method_a_female'],
                        df['method_b_male'], df['method_b_female'],
                        df['method_c_male'], df['method_c_female'])

print("f statistic:", result.statistic)
print("p-value:", result.pvalue)

if result.pvalue < 0.05:
    alpha = 0.05
else:
    alpha = 0.01

print("significance level chosen as", alpha)

print("----------------------------------------", 'demo', "-"*40)

import scipy.stats as stats
import pandas as pd
x = {
    'a_male':[85,80],
    'a_female':[88,84],
    'b_male':[82,89],
    'b_female':[78,85],
    'c_male':[92, 94],
    'c_female':[89,83]
    }
y = pd.DataFrame(x)  # 建立 dataframe 物件
# 計算 f統計量 及 p-值:
z1,z2 = stats.f_oneway(y['a_male'],y['a_female'],
                       y['b_male'],y['b_female'],
                       y['c_male'],y['c_female'])
print("f-統計量:", z1)
print("p-value:", z2)
if z2 < 0.05:
    print("有個別主效應或交互作用")
else:
    print("無個別主效應及交互作用")

print("----------------------------------------", 'demo-csv', "-"*40)
import csv
fn = 'lesson/hw0604.csv'
with open(fn, encoding='utf-8') as fobj:
    data = csv.reader(fobj)
    data_list = list(data)
    # print(list)
# for i in list:
#     print(i)
print('data_list[7][0]: ', data_list[7][0])
print('data_list[7][1]: ', data_list[7][1])

print("----------------------------------------", 'demo-web crawler', "-"*40)
import csv
import os
fn = os.path.join(os.path.dirname(__file__), 'stocks.csv')

# # File path
# fn = 'lesson/stocks.csv'

# Reading the CSV file
with open(fn, encoding='utf-8') as fobj:
    data = csv.reader(fobj)
    data_list = list(data)

# Print specific values from the data
print("日期:", data_list[2][2])
print("開盤價:", data_list[2][3])
print("收盤價:", data_list[2][6])

# Initialize lists to store Open and Close prices
Open = []
Close = []

# Collect the first 5 opening prices and closing prices
for i in range(1, 6):  # Adjusted range to start from 1
    Open.append(float(data_list[i][3]))  # Convert to float for potential decimal values
    Close.append(float(data_list[i][6]))  # Convert to float for potential decimal values

# Calculate and print the averages
print("近五天開盤價平均:", sum(Open) / len(Open))
print("近五天收盤價平均:", sum(Close) / len(Close))

print("----------------------------------------", 'demo', "-"*40)
