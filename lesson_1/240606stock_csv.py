print("----------------------------------------", 'demo-csv.reader(fobj)', "-"*40)
import os 
import csv
fn = os.path.join(os.path.dirname(__file__), '0606stock.csv')
"""
os.path.join：這個函數用於將多個路徑組合在一起。它會根據作業系統的不同，自動選擇正確的路徑分隔符（例如在 Windows 上是 \，在 Unix 系統上是 /）。
os.path.dirname(__file__)：__file__ 是一個特殊變量，表示當前 Python 檔案的路徑。os.path.dirname(__file__) 會返回該路徑的目錄部分。
"""
with open(fn, encoding='utf-8') as fobj:
    content = csv.reader(fobj)
    list_ = list(content)
# ['\ufeff日期_', '開盤價', '最高價', '最低價', '收盤價', '成交量']
# for row in list_:
#     print(row)
sum = 0
for i in range(1,len(list_)):
    sum += eval(list_[i][5].replace(',', ''))
print(sum)

print("----------------------------------------", 'demo-csv.write(fobj)', "-"*40)
import os 
import csv
fn = os.path.join(os.path.dirname(__file__), '0606stock.csv')
newfn = os.path.join(os.path.dirname(__file__), '0606newfile.csv')

with open(fn, encoding='utf-8') as fobj:
    content = csv.reader(fobj)
    list_ = list(content)

with open(newfn, 'w', newline='', encoding='utf-8') as obj:
    writerObject = csv.writer(obj) #建立writer物件
    for row in list_:
       writerObject.writerow(row)
os.remove(newfn)

print("----------------------------------------", 'demo-weather', "-"*40)
import os
import csv
import matplotlib.pyplot as plt

# Get the correct path to the CSV file
fn = os.path.join(os.path.dirname(__file__), 'weather.csv')

# Read the CSV file
with open(fn, encoding='utf-8') as fobj:
    content = csv.reader(fobj)
    list_ = list(content)

# Extract location data
location = []
for row in range(1, len(list_)):
    location.append(list_[row][0])
print(location)

# Extract June temperature data
june_temper = []
for row in range(1, len(list_)):
    june_temper.append(float(list_[row][6]))

# Plotting the bar chart
plt.figure(figsize=(10, 5))
plt.bar(location, june_temper, color='skyblue', width=0.8)
plt.xlabel('Location')
plt.ylabel('June Temperature', fontsize=1)
plt.title('June Temperature by Location')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print("----------------------------------------", 'demo-class', "-"*40)
class student():
    name = "Sunny"
    def __init__(self) -> None:
        pass
obj = student()
print(obj.name)
