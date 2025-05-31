print("----------------------------------------", 'demo-logging', "-"*40)
import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, format='')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(message)s')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s : %(message)s')
logging.disable(logging.CRITICAL) 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')

# logging.debug('logging message, DEBUG')
logging.debug('logging message')
logging.info('logging message')
logging.warning('logging message')
logging.error('logging message')
logging.critical('logging message')

print("----------------------------------------", 'demo-factorial()', "-"*40)
import logging
"""
#disable logging
logging.disable(logging.CRITICAL) 
#or
logging.basicConfig(level=logging.CRITICAL)
"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('--start--')                
def factorial(n):
    logging.debug(f"factorial({n}) start")
    ans = 1
    # for i in range(1, n + 1):
    for i in range(n + 1):
        ans *= i
        logging.debug(f'i = {i}, ans = {ans}')
    logging.debug(f"factorial({n}) end")
    return ans

num = 5
print(f"{num}! = {factorial(num)}")
logging.debug('--end--')                

print("----------------------------------------", 'demo-Assignment Expressions(指派運算式[海象運算符])', "-"*40)
import pprint
dict_ = {}
dict_2 = {}

print("Create the dict1, input end to stop")
# while (key := input('key: ')) != 'end':
while (key := input('key: ').strip()) != 'end':
    dict_[key] = input('Value: ')

print("Create the dict2, input end to stop")
# while (key := input('key: ')) != 'end':
while (key := input('key: ').strip()) != 'end':
    dict_2[key] = input('Value: ')

dict_ |= (dict_2)
pprint.pprint(dict_)
"""
dict_1.update(dict_2)  # 合併字典
dict_ = {**dict_1, **dict_2}  # 合併字典的另一種方式
dict_1 |= dict_2  # python 3.9 後可以使用
"""
for key, value in dict_.items():  # 返回元組 (key, value) 去解包
    print(key, value)

for key in dict_.keys():  # 遍歷字典的所有 key
    print(key)

for key in sorted(dict_.keys()):  # 對 key 進行排序後遍歷
    print(key, dict_[key])

for value in dict_.values():  # 遍歷字典的所有值
    print(value)

for value in set(dict_.values()):  # 去除重複值後遍歷字典的所有值
    print(value)
    
# 定義字典和要查找的值
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
target = 2
# 使用列表解析找出所有等於target值的鍵
keys = [k for k, v in d.items() if v == target]
print(keys)  # 輸出: ['b', 'e']

print("----------------------------------------", 'demo-repeat value of list', "-"*40)
lst = ['a', 'b', 'c', 'o', 'e', 'o', 'g']
i = lst.index(value) # 回傳第一個出現的索引值

# 找出所有位置
lst = ['a', 'b', 'c', 'o', 'e', 'o', 'g']
target = 'o'
# 使用列表解析找出所有等於target值的元素的索引
positions = [i for i, char in enumerate(lst) if char == target]

num = lst.count(value) # 回傳指定元素的出現次數

print("----------------------------------------", 'Test-with open', "-"*40)
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()  # 讀取整個文件
    print(content)
with open('example.txt', 'r', encoding='utf-8') as file:
    line = file.readline()  # 讀取一行
    print(line)
with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()  # 讀取所有行並以列表形式返回
    print(lines)
filename = 'example.txt'
with open(filename, 'r', encoding='utf-8') as file:
    print("讀取整個文件:")
    print(file.read())  # 讀取整個文件
    file.seek(0)  # 回到文件開始位置

    print("\n讀取第一行:")
    print(file.readline())  # 讀取第一行

    file.seek(0)  # 回到文件開始位置
    print("\n讀取所有行:")
    print(file.readlines())  # 讀取所有行並返回一個列表

print("----------------------------------------", 'Test-find the certain word', "-"*40)
from io import StringIO

# 模擬日誌文件內容
s = """192.168.111.13 - frank [10/Oct/2000:13:55:36] "GET /login HTTP/1.1" 200 3217
192.168.100.165 - alan [10/Oct/2000:22:01:17] "GET /user HTTP/1.1" 200 5480
192.168.113.214 - bob [11/Oct/2000:07:45:22] "GET /main HTTP/1.1" 301 1078
192.168.131.21 - lindy [11/Oct/2000:10:23:09] "GET /settings HTTP/1.1" 200 5466
192.168.192.89 - peter [11/Oct/2000:19:56:00] "GET /data HTTP/1.1" 200 4912
192.168.111.13 - frank [12/Oct/2000:11:03:37] "GET /login HTTP/1.1" 200 3226
192.168.114.117 - grace [12/Oct/2000:17:15:54] "GET /main HTTP/1.1" 200 5603"""

# 使用 StringIO 模擬文件打開行為
def open(file, mode='r'):
    return StringIO(s)

# 定義要搜尋的關鍵字
keyword = "/login"

# 開啟並讀取文件
with open('dummy_file.txt', 'r') as file:
    lines = file.readlines()

# 初始化一個空的列表來存儲包含關鍵字的行數
lines_with_keyword = []

# 遍歷每一行並檢查是否包含關鍵字
for index, line in enumerate(lines, start=1):
    if keyword in line:
        lines_with_keyword.append(index)

# 輸出包含關鍵字的行數
print(f"包含關鍵字的行數: {lines_with_keyword}")

print("----------------------------------------", 'Test', "-"*40)
