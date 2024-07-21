print("----------------------------------------", 'Test-ROT 13', "-"*40)
def rot13(word):
    output = []
    for c in word.lower():
        new_ord = ord(c) +13
        if new_ord > ord('z'):
            new_ord -= 26
        output.append(chr(new_ord))
    return ''.join(output)
print(rot13('python'))

print("----------------------------------------", 'Test-sorted()', "-"*40)
def strsort(s):
    return ''.join(sorted(s, key = str.lower)) #NOT lower()
print(strsort('python'))

print("----------------------------------------", 'Test-Pig Latin Sentence', "-"*40)
def pl_sentence(sentence):
    output = []
    for word in sentence.lower().split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)

print(pl_sentence('This is a test.'))

import string
def pl_sentence(sentence):
    output = []
    for word in sentence.lower().split():
        # 檢查單詞是否在末尾有標點符號
        if word[-1] in string.punctuation:
            punctuation = word[-1]
            word = word[:-1]
        else:
            punctuation = ''
        
        # 將單詞轉換為豬拉丁語
        if word[0] in 'aeiou':
            pig_latin_word = f'{word}way'
        else:
            pig_latin_word = f'{word[1:]}{word[0]}ay'
        
        # 如果有標點符號，則將其添加回去
        output.append(f'{pig_latin_word}{punctuation}')
    
    return ' '.join(output)

print(pl_sentence('This is a test. My name is Sunny!'))

print("----------------------------------------", 'Test-Pig Latin', "-"*40)
def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else: 
        return word[1:] + word[0] + 'ay'
        # return word[1:] + word[:1] + 'ay'
        
print(pig_latin('python'))
"""
public class PigLatin {
    public static String pigLatin(String word) {
        if (word.length() == 0) {
            return word;
        }
        char firstChar = word.charAt(0);
        if ("aeiou".indexOf(firstChar) != -1) {
            return word + "way";
        } else {
            return word.substring(1) + firstChar + "ay";
        }
    }

    public static void main(String[] args) {
        System.out.println(pigLatin("python"));
    }
}
"""

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/10
def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('abc', 'd', 'e'))
print(mysum([10, 20, 30], [40, 50], [60]))

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/11
people = [
    ('Joe', 'Biden', 'president@usa.gov'),
    ('Emmanuel', 'Macron', 'president@france.gov'),
    ('Justin', 'Trudeau', 'primeminister@canada.gov'),
    ('Angela', 'Merkel', 'primeminister@germany.gov'),
    ('Jacinda', 'Ardern', 'primeminister@newzealand.gov')
    ]

for person in sorted(people, key=lambda d: (d[1], d[0])):
    print(f'{person[1]}, {person[0]}: {person[2]}')

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/12
import operator

def sorted_grades(grades):
    grades.sort(key=operator.itemgetter(2), reverse=True)
    output = []
    for first, last, grade in grades:
        output.append(f'{last:12s}{first:10s}{grade:.1f}')
    return '\n'.join(output)

grades = [
    ('Alice', 'Wooding', 89),
    ('Bob', 'Johnson', 86),
    ('Cindy', 'Letterman', 93),
    ('David', 'Moor', 86),
    ('Eddie', 'Williams', 91)
    ]

print(sorted_grades(grades))

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/13
import operator

def most_repeated_letter(word):
    letters = list(set(word))
    letters_count = []
    for letter in letters:
        letters_count.append((letter, word.count(letter)))
    result = sorted(letters_count, key=operator.itemgetter(1))[-1]
    print(f'{result[0]} 重複了 {result[1]} 次')

most_repeated_letter('independence')

print("----------------------------------------", 'Test', "-"*40)
from collections import Counter
s = 'independence'
letter_count = Counter(s)
print(letter_count)
print(letter_count.most_common())
print(letter_count.most_common(2)) # 2表傳回兩筆
"""
Out put:
Counter({'e': 4, 'n': 3, 'd': 2, 'i': 1, 'p': 1, 'c': 1})
[('e', 4), ('n', 3), ('d', 2), ('i', 1), ('p', 1), ('c', 1)]
"""
#改寫後為...
import operator
from collections import Counter

def most_repeated_letter(word):
    result = Counter(word).most_common(1)[0]
    print(f'{result[0]} 重複了 {result[1]} 次')

most_repeated_letter('independence')

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/14
menu = {
    '三明治': 50,
    '咖啡': 40,
    '沙拉': 30
    }

def order_meal():
    total = 0
    while order := input('請點餐: '):
        if order in menu:
            price = menu[order]
            total += price
            print(f'{order} {price} 元, 總金額 {total}')
        else:
            print(f'抱歉! 我們沒有供應{order}')
    print(f'您的帳單為 {total} 元')

order_meal()

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/15
def record_rainfall():
    rainfall = {}
    while True:
        city_name = input('輸入城市: ')
        if not city_name:
            break
        rain_mm = input('輸入雨量 (mm): ')
        if not rain_mm:
            rain_mm = 0
 
        rainfall[city_name] = rainfall.get(city_name, 0) + int(rain_mm)
 
    for city, rain in rainfall.items():
        print(f'{city}: {rain} mm')

record_rainfall()

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/16
def unique_num_len(numbers):
    return len(set(numbers))

numbers = [1, 2, 3, 1, 2, 3, 4, 1, 2]
print(unique_num_len(numbers))

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/17
def dict_diff(first, second):
    output = {}
    all_keys = sorted(first.keys() | second.keys())
 
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 5}
d2 = {'a': 1, 'b': 2, 'd': 4, 'e': 6}
print('The different: ', dict_diff(d1, d2))

print("----------------------------------------", 'Test', "-"*40)
import os
fn = os.path.join(os.path.dirname(__file__), 'login.log')
f = open(fn, 'r')
try:
    for line in f.readlines():
        print(line)
finally:
    f.close()

print("----------------------------------------", 'Test-last line(type 1)', "-"*40)
import os
fn = os.path.join(os.path.dirname(__file__), 'login.log')
with open (fn, 'r', encoding='utf-8') as fobj:
    list = fobj.readlines()[-1] #會浪費讀取記憶體
    print(list)

print("----------------------------------------", 'Test-last line(type 2)', "-"*40)
import os
fn = os.path.join(os.path.dirname(__file__), 'login.log')
with open (fn, 'r', encoding='utf-8') as fobj:
    while True:
        line = fobj.readline()
        if not line:
            break
        lastline = line
    print(lastline)

print("----------------------------------------", 'Test-last line(type 3:iterator protocol)', "-"*40)
import os
fn = os.path.join(os.path.dirname(__file__), 'login.log')
with open (fn, 'r', encoding='utf-8') as fobj:
    for line in fobj:
        lastline = line
print(lastline)

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/18
s = """192.168.111.13 - frank [10/Oct/2000:13:55:36] "GET /login HTTP/1.1" 200 3217
192.168.100.165 - alan [10/Oct/2000:22:01:17] "GET /user HTTP/1.1" 200 5480
192.168.113.214 - bob [11/Oct/2000:07:45:22] "GET /main HTTP/1.1" 301 1078
192.168.131.21 - lindy [11/Oct/2000:10:23:09] "GET /settings HTTP/1.1" 200 5466
192.168.192.89 - peter [11/Oct/2000:19:56:00] "GET /data HTTP/1.1" 200 4912
192.168.111.13 - frank [12/Oct/2000:11:03:37] "GET /login HTTP/1.1" 200 3226
192.168.114.117 - grace [12/Oct/2000:17:15:54] "GET /main HTTP/1.1" 200 5603"""

from io import StringIO

def open(file, mode='r'):
    return StringIO(s)

# --------------------

def read_final_line(filename):
    f = open(filename, 'r')
    for line in f:
        pass
    f.close()
    return line

print(read_final_line(r'login.log'))

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/19
s = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lerner:x:1000:1000:Reuven Lerner:/home/lerner:/bin/bash"""

from io import StringIO

class open:
    def __init__(self, file, mode='r'):
        self.f = StringIO(s)
    
    def __enter__(self):
        return self.f
    
    def __exit__(self, *args):
        if self.f:
            self.f.close()

# --------------------

def passwd_to_dict(filename):
    users = {}
    with open(filename) as f:
        for line in f:
            user_info = line.split(':')
            users.update({user_info[0]: user_info[2]})
    return users

print(passwd_to_dict(r'passwd.cfg'))

print("----------------------------------------", 'Test-import pprint', "-"*40)
import pprint
pprint.pprint(passwd_to_dict(r'passwd.cfg'))
pprint.pprint(passwd_to_dict(r'passwd.cfg'), sort_dicts=False)

print("----------------------------------------", 'Test', "-"*40)
# https://www.flag.com.tw/Redirect/F1750/20
s = """This is a test file.

It contains 28 words and 20 different words.

It also contains 164 characters.

It also contains 11 lines.

It is also self-referential.

Wow!"""

from io import StringIO

class open:
    def __init__(self, file, mode='r'):
        self.f = StringIO(s)
    
    def __enter__(self):
        return self.f
    
    def __exit__(self, *args):
        if self.f:
            self.f.close()

# --------------------

def wordcount(filename):
    result = {
        'Characters': 0,
        'Words': 0,
        'Unique words': 0,
        'Lines': 0,
        }
    unique_words = set()
 
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            result['Lines'] += 1
            result['Characters'] += len(line)
            result['Words'] += len(words)
            unique_words.update(words)
 
        result['Unique words'] = len(unique_words)
 
    for key, value in result.items():
        print(f'{key}: {value}')

wordcount('text.txt')

print("----------------------------------------", 'Test', "-"*40)
#https://www.flag.com.tw/Redirect/F1750/21
# 這個版本使用假 open() 和 StringIO 來模擬檔案物件,
# 以便在 Python Tutor 執行

# --------------------

s = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts."""

from io import StringIO

class open:
    def __init__(self, file, mode='r'):
        self.f = StringIO(s)
    
    def __enter__(self):
        return self.f
    
    def __exit__(self, *args):
        if self.f:
            self.f.close()

# --------------------

def find_longest_word(filename):
    longest = ''
    with open(filename, 'r') as f:
        for line in f:
            for word in line.replace('.', '').split():
                if len(word) > len(longest):
                    longest = word
    return longest

print(find_longest_word(f'text2.txt'))

print("----------------------------------------", 'Test', "-"*40)
