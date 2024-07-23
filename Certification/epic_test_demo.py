print("----------------------------------------", 'Test', "-"*40)
# a, b, c, d = map(float, input("Input four Number space to seperat: \n").split(" "))
a, b, c, d = 23.12, 395.3, 100.4617, 564.329

print(f"|{a:7.2f} {b:7.2f}|")
print(f"|{c:7.2f} {d:7.2f}|")
print(f"|{a:<7.2f} {b:<7.2f}|")
print(f"|{c:<7.2f} {d:<7.2f}|")
print(f"|{c:^7.2f} {d:^7.2f}|")
"""
print("|{:7.2f} {:7.2f}|".format(a, b))
print("|{:7.2f} {:7.2f}|".format(c, d))
print("|{:<7.2f} {:<7.2f}|".format(a, b))
print("|{:<7.2f} {:<7.2f}|".format(c, d))

print("|%7.2f %7.2f|" % (a, b))
print("|%7.2f %7.2f|" % (c, d))
print("|%-7.2f %-7.2f|" % (a, b))
print("|%-7.2f %-7.2f|" % (c, d))
"""

print("----------------------------------------", 'Test', "-"*40)
string = "hello"
index = string.index('e')  # 返回 1
str_ = "hello world"
positions = [i for i, char in enumerate(str_) if char == 'o']  # 返回 [4, 7]
"""
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        String s = "hello world";
        char target = 'o';
        ArrayList<Integer> positions = new ArrayList<Integer>();
        int index = s.indexOf(target);  // 首次找到字符的索引
        
        while (index >= 0) {
            positions.add(index);
            index = s.indexOf(target, index + 1);  // 从上一个找到的位置之后开始搜索
        }

        System.out.println(positions);  // 输出所有'o'字符的索引位置
    }
}
"""

print("----------------------------------------", 'Test', "-"*40)
import math
# 0 coordinate
x2, y2 = 0, 0

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
except ValueError:
    print("請輸入有效的數字")
    exit()

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f"({x1}, {y1})")
print(f"({x2}, {y2})")
print(f"Distance = {distance:.4f}")

print("----------------------------------------", 'Test', "-"*40)
x = 345345333424243*15
if x % 15 == 0:
    print("x is multuple of 3 and 5")
elif x % 3 == 0:
    print("x is multuple of 3")
elif  x % 5 == 0:
    print("x is multuple of 5")
else:
    print("x is not multuple of 3 or 5")

print("----------------------------------------", 'Test', "-"*40)
def number_to_hex(num):
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if num <= 9:
        return str(num)
    else:
        return hex_map[num]

num = int(input("輸入數字(0-15): \n"))
print(number_to_hex(num))

# type2
x = int(input("輸入數字(0~15):\n"))
hex_str = hex(x)[2:].upper() # type: str
print(hex_str)

# type3
import re
x = int(input("輸入數字(0~15):\n"))
hex_str = hex(x)

# 使用正規表示法去掉'0x'前綴
hex_str_cleaned = re.sub(r'^0x', '', hex_str).upper()
hex_str_cleaned = hex_str.replace('0x', '', 1).upper() #1表次數
print(hex_str_cleaned)

print("----------------------------------------", 'Test', "-"*40)
number = 777  # 定義一個整數
binary_representation = bin(number)[2:]
print("二進位表示（無前綴）：", binary_representation)
octal_representation = oct(number)[2:]
print("八進位表示（無前綴）：", octal_representation)
hexadecimal_representation = hex(number)[2:]
print("十六進位表示（無前綴）：", hexadecimal_representation)
# decimal_representation = int(str(number), n) # n 表進位方式
"""
x = "0xA"
print(int(x, 16))
"""

print("----------------------------------------", 'Test', "-"*40)
try:
    n = int(input("Enter the Integer:"))
except Exception:
    print("Invalid value:")
    exit()

def drawTriangle(n) -> None:
    for i in range(1, n+1):
        str1 = " " * (n-i)
        str2 = '*' * (2*i-1)
        print(str1+str2)

drawTriangle(n)        

print("----------------------------------------", 'Test', "-"*40)
dict1 = {}
dict2 = {}
print("Create the dict1, input end to stop")
while True:
    key = input('key: ')
    if key == 'end':
        break
    dict1[key] = input('Value: ')

print("Create the dict2, input end to stop")
while True:
    key = input('key: ')
    if key == 'end':
        break
    dict2[key] = input('Value: ')
dict1.update(dict2)
print("----print----")
# sorted_dict = sorted(dict_.items(), key=lambda x: x[1], reverse=True) # 按照值進行排序，返回列表
for i in sorted(dict1.keys()):
    print(i+': '+ dict1[i])

print("----------------------------------------", 'Test-Assignment Expressions(指派運算式[海象運算符])', "-"*40)
import pprint
dict1 = {}
dict2 = {}

print("Create the dict1, input end to stop")
# while (key := input('key: ')) != 'end':
while (key := input('key: ').strip()) != 'end':
    dict1[key] = input('Value: ')

print("Create the dict2, input end to stop")
# while (key := input('key: ')) != 'end':
while (key := input('key: ').strip()) != 'end':
    dict2[key] = input('Value: ')

dict1 |= (dict2)
pprint.pprint(dict1)
print("----------------------------------------", 'Test', "-"*40)
"""
ord()
chr()
"""
x = list(input())
n = 0

for i in x:
    n += ord(i)
    print(f'ASCII code for {i} is {ord(i)}')
print(n)

print("----------------------------------------", 'Test', "-"*40)
f_name = input()
n = int(input())

y = open(f_name, 'r')
z = y.read()
a = z.split()
b = sorted(a)  # 排序後但未去除的字符串
c = sorted(set(b))  # 利用set删除重複字符串

for i in c:
    if b.count(i) == n:
        print(i)

print("----------------------------------------", 'Test', "-"*40)
import math
n = float(input()) # 邊數
s = float(input()) # 邊長

p = n*s
a = (n*(s**2))/(4*math.tan(math.pi/n))
print(f'Perimeter = {p}')
print(f'Area = {a:.4f}')

print("----------------------------------------", 'Test', "-"*40)
side1 = float(input())
side2 = float(input())
side3 = float(input())

x = [side1, side2, side3]
y = sorted(x)

if y[0]+y[1] > y[2]:
    print(sum(y))
else:
    print('Invalid')

print("----------------------------------------", 'Test', "-"*40)
#type:1
import math
num = int(input("輸入數字: "))

def value(n):
    return 1 / (math.sqrt(n - 1) + math.sqrt(n))

values_list = [value(i) for i in range(2, num + 1)]
ans = sum(values_list)
print(f"{ans:.4f}")

#type:2
num = int(input("輸入數字: "))
ans = 0
for i in range(1, num):
    ans += 1 / (math.sqrt(i) + math.sqrt(i + 1))
print(f"{ans:.4f}")

print("----------------------------------------", 'Test', "-"*40)
# a, b = map(int, input("Input two Number(a>b) space to seperat: \n").split(" "))
a, b = 14, 1144

#type: 1
sum_ = sum(n for n in range(a, b+1) if n % 2 == 0)

#type: 2
sum_ = 0
for _ in range(a, b+1):
    sum_ += _ if _ % 2 == 0 else 0

print("Sum:", sum_)

print("----------------------------------------", 'Test', "-"*40)
"""
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())
x10 = int(input())
list_ = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
"""

numbers = [int(input(f"輸入數字 {i+1}: ")) for i in range(10)]

odd_count = 0
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# 輸出奇數和偶數的計數結果
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
"""
# 遍歷列表中的每個數字，使用位元運算判斷是奇數還是偶數並計數
for number in numbers:
    if number & 1 == 0:  # 使用位元運算判斷偶數
        even_count += 1
    else:
        odd_count += 1
"""
print("----------------------------------------", 'Test', "-"*40)
# 定義一個函數來計算a的b次方
def compute(a, b) -> int:
    return a ** b  # 返回a的b次方

# 獲取用戶輸入的兩個數字，並轉換為整數
a = int(input("輸入第一個數字 (a): "))
b = int(input("輸入第二個數字 (b): "))

# 調用compute函數計算結果並打印
print(compute(a, b))

print("----------------------------------------", 'Test', "-"*40)
list_ = []
while True:
    num = int(input("Enter 9999 to stop loop:\n"))
    list_.append(num)
    if num == 9999:
        print("The minimum number: ", min(list_))
        break

"""
list_ = []
while True:
    try:
        num = int(input("Enter 9999 to stop loop:\n"))
        if num == 9999:
            if list_:  # 確保列表中有數據
                print("The minimum number: ", min(list_))
            else:
                print("No numbers were entered.")
            break
        else:
            list_.append(num)
    except ValueError:
        print("Please enter a valid integer.")
"""
# 初始化變量和集合
i = 0
set_ = set()

# 使用while循環不斷接收用戶輸入
while True:
    i = int(input("輸入數字（輸入-1999結束):"))
    if i == -1999:  # 如果輸入-1999，則結束循環
        break
    set_.add(i)  # 將輸入的數字添加到集合中

# 輸出集合的長度、最大值、最小值和總和
print(f"Length: {len(set_)}")
print(f"Max: {max(set_)}")
print(f"Min: {min(set_)}")
print(f"Sum: {sum(set_)}")

print("----------------------------------------", 'Test', "-"*40)
def compute(x, y):
    return x * y
a, b = map(int, input("Enter two number, use space to seperate.\n").split(" "))
print(f"{a}*{b} = {compute(a,b)}")

print("----------------------------------------", 'Test', "-"*40)
"""
a = eval(input("week1:"))
b = eval(input("week1:"))
c = eval(input("week1:"))

d = eval(input("week2:"))
e = eval(input("week2:"))
f = eval(input("week2:"))

g = eval(input("week3:"))
h = eval(input("week3:"))
i = eval(input("week3:"))

j = eval(input("week4:"))
k = eval(input("week4:"))
l = eval(input("week4:"))


list_ = [[a,b,c], [d,e,f], [g,h,i], [i,k,l]]
for i in range(4):
    print(f"Week: {i+1}:")
    print(f"Day 1: {list_[i][0]}")
    print(f"Day 2: {list_[i][1]}")
    print(f"Day 3: {list_[i][2]}")

print(f"Average: {sum(list_)/len(list_):.2f}")
print(f'Highest: {max(list_):.2f}')
print(f'Lowest: {min(list_): .2f}')
"""
# 定義函數來獲取用戶輸入的數據
def get_weekly_data(week_number):
    print(f"Week {week_number}:")
    week_data = [
        float(input("Day 1: ")),
        float(input("Day 2: ")),
        float(input("Day 3: "))
    ]
    return week_data

# 獲取每周的數據
week1 = get_weekly_data(1)
week2 = get_weekly_data(2)
week3 = get_weekly_data(3)
week4 = get_weekly_data(4)

# 組合所有周的數據成一個列表
list_ = [week1, week2, week3, week4]

# 輸出每周的數據
for i in range(4):
    print(f"Week {i + 1}:")
    print(f"Day 1: {list_[i][0]}")
    print(f"Day 2: {list_[i][1]}")
    print(f"Day 3: {list_[i][2]}")

# 計算所有數據的平均值、最高值和最低值
all_data = [item for sublist in list_ for item in sublist]
average = sum(all_data) / len(all_data)
highest = max(all_data)
lowest = min(all_data)

# 輸出結果
print(f"Average: {average:.2f}")
print(f'Highest: {highest:.2f}')
print(f'Lowest: {lowest:.2f}')

print("----------------------------------------", 'Test', "-"*40)
"""
list_ = list(map(str, input("Select five cards of deck(num), use space to seperate.\n").split(" ")))

valid_cards = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'J', 'j', 'Q', 'q', 'K', 'k'}

if not all(card in valid_cards for card in list_):
    print("Invalid input")
else: 
    sum_  = 0
    for i in list_: 
        if i == "A" or i == "a":
            sum_ += 1
        elif i == "J" or i == "j":
            sum_ += 11
        elif i == "Q" or i == "q":
            sum_ += 12
        elif i == "K" or i == "k":
            sum_ += 13
        else:
            sum_ += int(i)
    print(f"Sum of cards is: {sum_}")
"""
input_cards = input("Select five cards of deck (num), use space to separate:\n").strip().upper().split()

valid_cards = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'J', 'Q', 'K'}

try:
    # 驗證輸入的合法性
    if len(input_cards) != 5 or not all(card in valid_cards for card in input_cards):
        raise ValueError("Invalid input: please enter exactly five cards from the valid set.")

    # 卡牌對應數值的字典
    card_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    card_values.update({str(num): num for num in range(1, 10)})  # 增加數字卡牌的映射

    # 計算卡牌總和
    total_sum = sum(card_values[card] for card in input_cards)
    print(f"Sum of cards is: {total_sum}")

except ValueError as e:
    print(e)

print("----------------------------------------", 'Test', "-"*40)
#type1
_str  = list(input())
print(''.join(reversed(_str)))

#type2
"""
23456 % 10 = 2345..6
2345 % 10 = 234..5
234 % 10 = 23..4
23 % 10 = 2..3
"""
x = int(input())
y = x
if x == 0:
    print(0)
else:
    while y != 0:
        z = y % 10
        print(z, end='')
        y = y // 10

print("----------------------------------------", 'Test', "-"*40)
card_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
card_values = sorted(card_values.items(), key=lambda x:x[1], reverse=False)
print(card_values)

print("----------------------------------------", 'Test', "-"*40)
import os
fn = os.path.join(os.path.dirname(__file__), 'number.txt')

with open(fn, 'r', encoding="utf-8") as fobj:
    list_ = [int(word.strip()) for word in fobj.read().split()]
print(sum(list_))

print("----------------------------------------", 'Test', "-"*40)
import os
# Requesting file name and strings for replacement from the user
f_name = input("Enter the file name: ")
str_old = input("Enter the old string to replace: ")
str_new = input("Enter the new string: ")

fn = os.path.join(os.path.dirname(__file__), f_name)
# Reading the content of the file
with open(fn, 'r') as file:
    content = file.read() #type is the string

# Displaying content before replacement
print("==== Before the replacement ====")
print(content)

# Replacing the old string with the new string in the content
updated_content = content.replace(str_old, str_new)

# Writing the updated content back to the file
# with open(fn, 'w') as file: #允許寫入
with open(fn, 'w+') as file: #允許讀加上寫入
    file.write(updated_content)

# Displaying content after replacement
print("==== After the replacement ====")
with open(fn, 'r') as file:
    print(file.read())


print("----------------------------------------", 'Test', "-"*40)
# 讀取文件並計算字數
def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        words = content.split()
        word_count = len(words)
        return word_count
    except FileNotFoundError:
        return "檔案不存在"

# 使用函數
filename = 'example.txt'  # 確保這個文件在你的文件夾中
print(f'文件中的字數為: {count_words_in_file(filename)}')

print("----------------------------------------", 'Test', "-"*40)
# 寫入文件
def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

# 使用函數
content = "這是一段範例文本。"
filename = 'new_example.txt'
write_to_file(filename, content)
print(f'文本已寫入到文件 {filename}')

print("----------------------------------------", 'Test', "-"*40)
# 附加到文件
def append_to_file(filename, content):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content)

# 使用函數
content = "\n這是追加的文本。"
filename = 'example.txt'  # 確保這個文件在你的文件夾中
append_to_file(filename, content)
print(f'文本已附加到文件 {filename}')

print("----------------------------------------", 'Test', "-"*40)
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

print("----------------------------------------", 'Test-assignment expressions(海象算符)', "-"*40)
while text := input('Enter string:'): #empty string regards as False
    print('String:', text)
print("End") #Enter space to break

def run_timing():
    total_time = 0.0
    number_of_runs = 0
    while run_time := input('輸入跑10公里的時間(按Enter結束):'):
        try:
            run_time_value = float(run_time)
            total_time += run_time_value
            number_of_runs += 1
        except Exception as e:
            print('Error: ', e)

    if number_of_runs > 0:
        average_time = (total_time / number_of_runs)
    else:
        average_time = 0.0
    print(f"跑{number_of_runs}次平均時間為{average_time:.3f}分鐘")

run_timing()

print("----------------------------------------", 'Test-reverse String and Number', "-"*40)
#String method1
original_string = "hello"
reversed_string = original_string[::-1]
print(reversed_string)

#String method2
original_string = "hello"
reversed_string = ''.join(reversed(original_string))
print(reversed_string)

#String method3
def reverse_string_loop(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

#Number method1
original_number = 12345
reversed_number = int(str(original_number)[::-1])
print(reversed_number)

#Number method2
original_number = 12345
reversed_number = int(''.join(reversed(str(original_number))))
print(reversed_number)

#Number method3
def reverse_number_math(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

print("----------------------------------------", 'Test-Different char', "-"*40)
seq1 = 'atgtcttcgcaagactcaaaaaata'
seq2 = 'atgtcttcgcaagactaaaaaata'

zip_seqs = zip(seq1, seq2)
# print(list(zip_seqs))

enum_seqs = enumerate(zip_seqs)
# print(list(enum_seqs))

for i, (a, b) in enum_seqs:
    if a != b:
        print(f'index: {i}')

print("----------------------------------------", 'Test', "-"*40)
"""
type 1
"""
matrix = [
    [3, 8, 1],
    [7, 4, 9],
    [5, 6, 2]
]

# 初始化最大值及其索引
max_value = matrix[0][0]
max_index = (0, 0)

# 遍歷整個矩陣來找出最大值及其索引
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_index = (i, j)

print(f"最大值是 {max_value}, 位置在 {max_index}")
"""
type 2
"""
matrix = [
    [3, 8, 1],
    [7, 4, 9],
    [5, 6, 2]
]

# 找出最大值及其索引
max_value = max(max(row) for row in matrix)
max_index = [(i, row.index(max_value)) for i, row in enumerate(matrix) if max_value in row][0]

print(f"最大值是 {max_value}, 位置在 {max_index}")

"""
Output:
最大值是 9, 位置在 (1, 2)
"""

print("----------------------------------------", 'Test', "-"*40)
