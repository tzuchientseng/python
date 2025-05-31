import sys
# sys.path.append('/Users/GOOD-PC/Coding/python/module')
sys.path.append('module')


# demo 1
print("----------------------------------------", 'demo1-import function(直接import 模組名稱)', "-"*40)
import module.makefood as object
from module.makefood import make_icecream, make_drink
from module.makefood import *
make_icecream("草莓醬")
make_icecream("草莓醬", "葡萄乾", "巧克力碎片")
make_drink("large", "Coke")
object.make_drink("large", "Coke")

# demo 2
print("----------------------------------------", 'demo2-import classes(from 檔名 import 類別名稱)', "-"*40)
from module.bank import *
jamesbank = Banks('James')
print("James's bank = ", jamesbank.bank_title())
jamesbank.save_money(500)
jamesbank.get_balance()

hungbank = Shilin_Banks('Hung')
print("Hung's bank = ", hungbank.bank_title())

# demo 3
print("----------------------------------------", 'demo3-import module name(import 檔名 使用模組名稱.類別名稱)', "-"*40)
import module.bank
jamesbank = module.bank.Banks('James')
print("James's bank = ", jamesbank.bank_title())
jamesbank.save_money(500)
jamesbank.get_balance()
hungbank = module.bank.Shilin_Banks('Hung')
print("Hung's bank = ", hungbank.bank_title())

# demo 4
import random
print("----------------------------------------", 'demo4-Random', "-"*40)
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

print("----------------------------------------", 'demo4-Random(0~1)', "-"*40)
for i in range(5):
    print(random.random())

print("----------------------------------------", 'demo-uniform(Float)', "-"*40)
for i in range(5):
    print("Uniform(1, 10) : ", random.uniform(1, 10))

print("----------------------------------------", 'demo-Choice', "-"*40)
fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print(random.choice(fruits))

print("----------------------------------------", 'demo-Shuffle', "-"*40)
porker = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for i in range(3):
    random.shuffle(porker)
    print(porker)
import random
print("----------------------------------------", 'sample', "-"*40)
lotterys = random.sample(range(1, 50), 7)
specialNum = lotterys.pop()
print("第XX期大樂透號碼:", end=" ")
for lottery in sorted(lotterys):
    print(lottery,end=" ")
print(f"特別號:{specialNum}")

print("----------------------------------------", 'seed', "-"*40)
random.seed(5)
for i in range(5):
    print(random.random())

print("----------------------------------------", 'Time', "-"*40)
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

print("----------------------------------------", 'Time(ASCII time)', "-"*40)
import time
print(time.asctime())
print(time.ctime())
print(time.ctime(1700000))

print("----------------------------------------", 'Process()', "-"*40)
import time 
x = 1000_000
pi = 0
time.process_time()
for i in range(1, x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:
        e_time = time.process_time()
        print(f"當 {i=:7d}, 時 PI={pi:8.7}, 所花的時間={e_time}")

print("----------------------------------------", 'stdin/stdou', "-"*40)
import sys
print("Enter the String(Enter to submit)")
msg = sys.stdin.readline()
print(msg)
sys.stdout.write("I like python.")

print("----------------------------------------", 'Path', "-"*40)
import sys
for dirpath in sys.path:
    print(dirpath)

print("----------------------------------------", 'Get Version', "-"*40)
print("Python --verion: ", sys.version)
print("Python --verion: ", sys.version_info)
print(sys.getwindowsversion)
print(sys.executable)

print("----------------------------------------", 'Keyword', "-"*40)
import keyword
print(keyword.kwlist)

keywordLists = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordLists:
    print(f"{x:>8s} {keyword.iskeyword(x)}")

print("----------------------------------------", 'Calendar', "-"*40)
import calendar
print("2024是否為閏年", calendar.isleap(2024))
print("幾個閏年(2000,2024)", calendar.leapdays(2000, 2024))
print(calendar.month(2024,5))
print(calendar.calendar(2024))

print("----------------------------------------", 'Collections', "-"*40)
from collections import defaultdict
fruits = defaultdict(lambda : 10)
fruits["Apple"] = 20
fruits["Orange"]
print(fruits)

print("----------------------------------------", 'Counter()', "-"*40)
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

print("----------------------------------------", 'Palindrome', "-"*40)
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

# method 2
def is_palindrome(s: str) -> bool:
    # 去除字串中的空白及非字母數字字符，並轉為小寫
    cleaned_s = ''.join(filter(str.isalnum, s)).lower()
    # 比較清理後的字串與其反轉後的字串
    return cleaned_s == cleaned_s[::-1]
test_strings = ["A man, a plan, a canal, Panama", "racecar", "hello"]
for s in test_strings:
    print(f"'{s}' 是回文: {is_palindrome(s)}")
"""
public class PalindromeChecker {
    public static void main(String[] args) {
        String[] testStrings = {"A man, a plan, a canal, Panama", "racecar", "hello"};
        for (String s : testStrings) {
            System.out.println("'" + s + "' 是回文: " + isPalindrome(s));
        }
    }
    public static boolean isPalindrome(String s) {
        // 將字串中的空白及非字母數字字符去除，並轉為小寫
        String cleanedString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
        // 設定兩個指針，一個從字串開頭，一個從字串結尾
        int left = 0;
        int right = cleanedString.length() - 1;
        
        // 檢查字串是否對稱
        while (left < right) {
            if (cleanedString.charAt(left) != cleanedString.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
}
"""
print("----------------------------------------", 'pprint', "-"*40)
import sys
from pprint import pprint
print("print:")
print(sys.path)
print("pprint:")
pprint(sys.path)
print("----------------------------------------", 'itertools', "-"*40)
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

print("----------------------------------------", 'Combinations()', "-"*40)
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

print("----------------------------------------", 'pyperclip', "-"*40)
import pyperclip as clip
clip.copy('SUNNY')
string = clip.paste()
print(string)
