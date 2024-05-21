import sys
# sys.path.append('/Users/GOOD-PC/Coding/python/module')
sys.path.append('module')


# demo 1
print("-"*7, 'demo1-import function(直接import 模組名稱)', "-"*7)

import makefood as object
from makefood import make_icecream, make_drink
from makefood import *


make_icecream("草莓醬")
make_icecream("草莓醬", "葡萄乾", "巧克力碎片")
make_drink("large", "Coke")

object.make_drink("large", "Coke")

# demo 2
print("-"*7, 'demo2-import classes(from 檔名 import 類別名稱)', "-"*7)
from bank import *
jamesbank = Banks('James')
print("James's bank = ", jamesbank.bank_title())
jamesbank.save_money(500)
jamesbank.get_balance()

hungbank = Shilin_Banks('Hung')
print("Hung's bank = ", hungbank.bank_title())

# demo 3
print("-"*7, 'demo3-import module name(import 檔名 使用模組名稱.類別名稱)', "-"*7)
import bank
jamesbank = bank.Banks('James')
print("James's bank = ", jamesbank.bank_title())
jamesbank.save_money(500)
jamesbank.get_balance()
hungbank = bank.Shilin_Banks('Hung')
print("Hung's bank = ", hungbank.bank_title())

# demo 4
import random
print("-"*7, 'demo4-Random', "-"*7)
min, max = 1, 10
ans = random.randint(min, max)
while True: 
    yourNum = int(input("猜猜1-10:之間的數字:\n"))
    if yourNum == ans:
        print("Correct!")
        break
    elif yourNum < ans:
        print("Greater~")
    else: 
        print("Smaller~")

print("-"*4, 'Random(0~1)', "-"*4)
for i in range(5):
    print(random.random())

print("-"*4, 'Uniform', "-"*4)
for i in range(5):
    print("Uniform(1, 10) : ", random.uniform(1, 10))

print("-"*4, 'Choice', "-"*4)
fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print(random.choice(fruits))

print("-"*4, 'Shuffle', "-"*4)
porker = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for i in range(3):
    random.shuffle(porker)
    print(porker)
import random
print("-"*4, 'Sample', "-"*4)
lotterys = random.sample(range(1, 50), 7)
specialNum = lotterys.pop()
print("第XX期大樂透號碼:", end=" ")
for lottery in sorted(lotterys):
    print(lottery,end=" ")
print(f"特別號:{specialNum}")

print("-"*4, 'Seed', "-"*4)
random.seed(5)
for i in range(5):
    print(random.random())

print("-"*4, 'Time', "-"*4)
import time
import random
import time, random #不符合PEP8風格 (Python Enhance Proposals)
min , max = 1, 10
ans = random.randint(min, max)
yourNum = int(input("Guess the number between 1 to 10\n"))
starttime = int(time.time())
while True:
    if yourNum == ans:
        endttime = int(time.time())
        print("Correct!")
        print("Spending time: ", endttime - starttime, "secs")
        break
    elif yourNum < ans:
        print("Greater!")
    else:
        print("Smaller!")
    yourNum = int(input("Guess the number between 1 to 10\n"))

print("-"*4, 'Time(ASCII time)', "-"*4)
import time
print(time.asctime())
print(time.ctime())
print(time.ctime(1700000))

print("-"*4, 'Process()', "-"*4)
import time 
x = 1000_000
pi = 0
time.process_time()
for i in range(1, x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:
        e_time = time.process_time()
        print(f"當 {i=:7d}, 時 PI={pi:8.7}, 所花的時間={e_time}")

print("-"*4, 'stdin/stdout', "-"*4)
import sys
print("Enter the String(Enter to submit)")
msg = sys.stdin.readline()
print(msg)
sys.stdout.write("I like python.")

print("-"*4, 'Path', "-"*4)
import sys
for dirpath in sys.path:
    print(dirpath)

print("-"*4, 'Get Version', "-"*4)
print("Python --verion: ", sys.version)
print("Python --verion: ", sys.version_info)
print(sys.getwindowsversion)
print(sys.executable)

print("-"*4, 'Keyword', "-"*4)
import keyword
print(keyword.kwlist)

keywordLists = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordLists:
    print(f"{x:>8s} {keyword.iskeyword(x)}")

print("-"*4, 'Calendar', "-"*4)
import calendar
print("2024是否為閏年", calendar.isleap(2024))
print("幾個閏年(2000,2024))", calendar.leapdays(2000, 2024))
print(calendar.month(2024,5))
print(calendar.calendar(2024))

# print("-"*7, 'Collections', "-"*7)
from collections import defaultdict
fruits = defaultdict(lambda : 10)
fruits["Apple"] = 20
fruits["Orange"]
print(fruits)

# print("-"*7, 'Counter()', "-"*7)
from collections import Counter

fruits = ["Apple", "Orange", "Apple"]
fruitsdic = Counter(fruits)
print(fruitsdic)
print("most_commin()")
print("(0):", fruitsdic.most_common())
print("(1):", fruitsdic.most_common(1))
print("(2):", fruitsdic.most_common(2))

fruits2 = ['grape', 'orange', 'orange', 'grape']
print("+", Counter(fruits) + Counter(fruits2))
print("-", Counter(fruits) - Counter(fruits2))
print("&", Counter(fruits) & Counter(fruits2)) #Don't add the count
print("|", Counter(fruits) | Counter(fruits2))

print("-"*7, 'Palindrome', "-"*7)
from collections import deque
def palindrome(word):
    wd = deque(word)
    while len(wd) > 1:
        if wd.pop() != wd.popleft():
            return False
    return True
print(palindrome("x"))
print(palindrome("abccba"))
print(palindrome("radar"))
print(palindrome("python"))

print("-"*7, "pprint", "-"*7)
import sys
from pprint import pprint
print("print:")
print(sys.path)
print("pprint:")
pprint(sys.path)

print("-"*7, "itertools", "-"*7)
import itertools

from numpy import double
for i in itertools.chain([1,2,3],('a','d')):
    print(i)
# for i in itertools.cycle(('a','b','c')):
#     print(i)

def mul(x, y):
    return (x * y)
for i in itertools.accumulate((1,2,3,4,5)):
    print(i)
for i in itertools.accumulate((1,2,3,4,5),mul):
    print(i)
# Using itertools.accumulate with a lambda for multiplication
for i in itertools.accumulate((1,2,3,4,5), (lambda x, y: x * y)):
    print(i)

print("-"*7, "Combinations", "-"*7)
n = ['a', 'b', 'c']
r = 2
comb = itertools.combinations(n, r)
print(list(comb))
print("-"*14)
single = 0
double = 0
counter = 0
x = ['F','f','F','f']
r = 2

for gene in itertools.combinations(x, r):
    if 'F' in gene:
        double += 1
    else:
        single += 1
    counter += 1
print("單眼皮機率: %5.3f" % (single / counter))
print("雙眼皮機率: %5.3f" % (double / counter))
print("-"*7, 'demo4', 7)
