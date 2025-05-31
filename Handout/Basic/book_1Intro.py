################################################

print('Hellow python')
#################################################
'''
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
'''

# or

"""
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa~
"""

#################################################

import this

#################################################
import antigravity

#################################################
print("----------------------------------------", 'demo', "-"*40)
#Using python shell by cmd (enter "python")
googol = 10**100
Large_number = 1_000_000


fobj1 = open("test.txt", mode="w", encoding="utf-8")
print("Testing mod=w, using utf-8 format", file = fobj1)
fobj1.close()

import math
print(math.inf)
print(math.e)

print("----------------------------------------", 'demo', "-"*40)
import math
r = 6371  # 地球半徑

x1, y1 = 22.2838, 114.1731  # 香港紅磡車站經緯度
x2, y2 = 25.0452, 121.5168  # 台北車站經緯度

# 使用球面三角法計算兩點之間的距離
d = r * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
                  math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
                  math.cos(math.radians(y1 - y2)))

print(f"distance = {d:6.1f} 公里")

print("----------------------------------------", 'demo', "-"*40)
x, y = 23, 34234
max_ = x if x>y else y
min_ = x if x<y else y
max2_ = max(23, 24)
min2_ = min(23, 24)
print(max_)
print(min_)
print(max2_)
print(min2_)

print("----------------------------------------", 'demo', "-"*40)
item = eval(input("Enter the number:"))
item = 10 if item>=10 else item
print(item)

print("----------------------------------------", 'demo', "-"*40)
list = [0,1,2,3,4,5,6,7,8,9]
print(f"{list[::]}")
print(f"{list[0:2]}")
print(f"{list[2:-2]}")
print(f"{list[::-1]}")
print(f"{list[::-2]}")
# test = 2.32
# print(f"{test:.2f}")

print("----------------------------------------", 'demo', "-"*40)
x = list('Deepmind')
y = x[4:]
print(y)

for x in range(3,4,-3):
    print(x)

print("----------------------------------------", 'demo', "-"*40)
list_ = [1,2,3,23,2,3,3] 
for i, j in enumerate(list_):
    print(i, j, sep=" ")

print("----------------------------------------", 'demo', "-"*40)
n = int(input("Enter the n:\n"))
sum = 0
for valua_of_range in range(1,n+1):
    sum += valua_of_range
print(sum)

print("----------------------------------------", 'demo', "-"*40)
n2 = int(input("Enter the n2:\n"))
total = sum(range(1,n2+1))
print(f"From 1 to {n2} sum is: {total}")

print("----------------------------------------", 'demo-list generator', "-"*40)
# list generator
oddlist = [num for num in range(1,10) if num % 2 == 1]
print(oddlist)
import random
random_numbers = [random.randint(1, 4) for _ in range(10)]
print(random_numbers, end=" ")
list = [print("Hi", end=" ") for _ in range(10)]
print("Hi "*10)

print("----------------------------------------", 'demo', "-"*40)
players = ["Lebron", "Curry", "Jordan"]
n = int(input("Enter the number:"))
if n>len(players): n = len(players)
index = 0
for player in players:
    if index == n:
        break
    print(player, end=" ")
    index +=1   

print("----------------------------------------", 'demo', "-"*40)
sc = [[1, 'aaa', 80, 95, 88, 0, 0, 0],
      [2, 'bbb', 98, 97, 96, 0, 0, 0],
      [3, 'ccc', 91, 93, 95, 0, 0, 0] 
    ]
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])
    sc[i][6] = round(sc[i][5]/3, 1)
    print(sc[i])
sc.sort(key=lambda x:x[5], reverse=True)
for i in range(len(sc)):
    sc[i][7] = i + 1
sc.sort(key=lambda x:x[0])
print(sc)

print("----------------------------------------", 'demo', "-"*40)
noodles  = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60, '大滷麵':90, '麻醬麵':70}
noodlesLst = sorted(noodles.items(), key=lambda item:item[1], reverse=False)
print(noodlesLst)

seq1 = ['name', 'city']
list_dic1 = dict.fromkeys(seq1)
print(f"字典1:{list_dic1}")
list_dic2 = dict.fromkeys(seq1, 'Chicago')
print(f"字典2:{list_dic2}")

seq2 = ('name', 'city')
tup_dict1 = dict.fromkeys(seq2)
print(f"字典3:{tup_dict1}")
tup_dict2 = dict.fromkeys(seq2, 'New York')
print(f"字典4:{tup_dict2}")

print("----------------------------------------", 'demo', "-"*40)
word = 'deepmind'
alphabetCount = {alphabet: word.count(alphabet) for alphabet in word}
alphabetCount = {alphabet: word.count(alphabet) for alphabet in set(word)} #較快
print(alphabetCount)

print("----------------------------------------", 'demo', "-"*40)
abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
end23 = abc[-3:]            # 從字符串 abc 中取出倒數三個字元。
front3 = abc[:3]            # 從字符串 abc 中取出前三個字元。
subText = end23 + front3    # 將 end23 和 front3 兩個字串合併起來。
encry_dict = dict(zip(abc, subText)) # 使用 zip 函數將 abc 和 subText 組成一對一的映射關係，並轉換成字典。
print("列印編碼對應\n", encry_dict)  # 列印加密字典，顯示字符映射關係。

print("----------------------------------------", 'demo', "-"*40)
msgTest = input("請輸入原始人類語字串：")  # 提示用戶輸入一串原始文本。
# (這行代碼上面有手寫註解 '1/ a/'，可能是指代換的規則或者其他意義，但不是代碼的一部分。)

cipher = []                  # 初始化一個空列表，用於存放加密後的字符。
for i in msgTest:            # 遍歷用戶輸入的文本中的每個字符。
    v = encry_dict[i]        # 根據加密字典找到每個字符對應的加密字符。
    cipher.append(v)         # 把加密字符添加到列表中。
ciphertext = ''.join(cipher) # 使用 join 方法把列表中的字符串聯起來形成一個字符串。

print("原始字串 = ", msgTest)       # 輸出用戶輸入的原始文本。
print("加密字串 = ", ciphertext)    # 輸出加密後的文本。

print("----------------------------------------", 'demo', "-"*40)
def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def running(func, arg1, arg2):
    return func(arg1, arg2)

print(running(add, 5, 10))
print(running(mul, 5, 10))

print("----------------------------------------", 'demo', "-"*40)
def func(b):
    return lambda x: 2 * x + b
linear = func(5)
print (linear(10))

