print("----------------------------------------", 'demo-phone_number', "-"*40)
def taiwanPhoneNum(string):
    """檢查是否含有手機聯絡資料的台灣手機號碼格式"""
    if len(string) != 12:
        return False

    for i in range(0,4):
        if string[i].isdecimal() == False:
            return False

    if string[4] != '-':
        return False

    for i in range(5, 8):
        if string[i].isdecimal() == False:
            return False

    if string[8] != '-':
        return False

    for i in range(9,12):
        if string[i].isdecimal() == False:
            return False
    return True

def parseString(string):
    """解析字串是否含有電話號碼"""
    notFoundSignal = True
    for i in range(len(string)):
        # 用週遍變數步抽出12個字元做測試
        msg = string[i:i+12]
        if taiwanPhoneNum(msg):
            print(f"電話號碼是: {msg}")
            notFoundSignal = False
    if notFoundSignal:
        print(f"{string}字串不含有電話號碼")

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天7:30和我一起搭小田急巴士到新宿'
msg3 = '請明天7:30和我一起搭小田急巴士到新宿。可打0933-080-080聯絡我!'

parseString(msg1)
parseString(msg2)
parseString(msg3)

print("----------------------------------------", 'demo-regular expression: search()', "-"*40)
import re
"""
rtn_match = re.serch(pattern, string, flags)
'\d\d\d\d-\d\d\d-\d\d\d'
'\\d\\d\\d\\d-\\d\\d\\d-\\d\\d\\d'
r'\d\d\d\d-\d\d\d-\d\d\d'
r'\d\d-\d\d\d\d\d\d\d\d'
r'(\d\d)-(\d\d\d\d\d\d\d\d)'
r'(\d{2})-(\d{8})'
r'(\(\d{2}\))-(\d{8})'
"""
msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天7:30和我一起搭小田急巴士到新宿'
msg3 = '請明天7:30和我一起搭小田急巴士到新宿。可打0933-080-080聯絡我!'
def parseString(string):
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.search(pattern, string) # rtn_match = re.serch(pattern, string, flags)
    # phoneNum = re.findall(pattern, string) 
    if phoneNum != None:
        print(f"Phone number: {phoneNum.group()}")
    else:
        print("-> No phone number in the string!")

parseString(msg1)
parseString(msg2)
parseString(msg3)

print("----------------------------------------", 'demo-regular expression: findall() (return list[])', "-"*40)
import re
msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天7:30和我一起搭小田急巴士到新宿'
msg3 = '請明天7:30和我一起搭小田急巴士到新宿。可打0933-080-080聯絡我!'
def parseString(string):
    pattern = r'\d{4}-\d{3}'
    phoneNum = re.findall(pattern, string) 
    if phoneNum != None:
        print(f"Phone number: {phoneNum}")
    else:
        print("-> No phone number in the string!")

parseString(msg1)
parseString(msg2)
parseString(msg3)

print("----------------------------------------", 'demo-search(), group(), groups()', "-"*40)
import re
msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)
if phoneNum:
    print(f"Phone number: {phoneNum.group()}")
    print(f"Phone number: {phoneNum.group(0)}")
    print(f"Region: {phoneNum.group(1)}")
    print(f"Number: {phoneNum.group(2)}")
else:
    print("No phone number found.")
print("----or----")
phoneNum2 = re.search(pattern, msg)
if phoneNum:
    areaNum, localNUm = phoneNum2.groups()
    print(f"Region: {areaNum}")
    print(f"Number: {localNUm}")

print("----------------------------------------", 'demo-pipe', "-"*40)
import re
msg = 'John and Tom will attend my party tonight. JOHN is by best friend, and he name is John Mayer'
pattern = 'John|Tom'
print(re.findall(pattern, msg))
pattern2 = 'Mary|Tom'
print(re.findall(pattern, msg))
print("Ignore case")
print(re.findall(pattern, msg, re.I))
print(re.findall(pattern, msg, re.IGNORECASE))

print("----------------------------------------", 'demo-string', "-"*40)
import re
def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:  # 搜索失败
        print("--FAIL--", txt)
    else:  # 搜索成功
        print(" ------>", txt.group())

msg1 = 'son'
msg2 = 'sonson'
msg3 = 'sonsonson'
msg4 = 'sonsonsonson'
msg5 = 'sonsonsonsonson'
pattern = '(son){3,5}' #(son)(son)(son)|(son)(son)(son)(son)|(son)(son)(son)(son)(son)
"""
(son){3,}
(son){,10}
"""
searchStr(pattern, msg1)
searchStr(pattern, msg2)
searchStr(pattern, msg3)
searchStr(pattern, msg4)
searchStr(pattern, msg5)

print("----------------------------------------", 'demo-string_greedy_search', "-"*40)
import re
def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:
        print("--FAIL--")
    else:
        print("---->", txt.group())
msg = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern, msg)
pattern2 = '(son){3,5}?' #ungreedy 
searchStr(pattern2, msg)

print("----------------------------------------", 'demo- +*? ', "-"*40)
import re
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = r'\w+' #['John', 'Johnson', 'Johnnason', 'and', 'Johnnathan', 'will', 'attend', 'my', 'party', 'tonight']
print(re.findall(pattern, msg)) 
pattern2 = r'John\w+' #['Johnson', 'Johnnason', 'Johnnathan']
print(re.findall(pattern2, msg))
pattern3 = r'John\w*' #['John', 'Johnson', 'Johnnason', 'Johnnathan']
print(re.findall(pattern3, msg))
pattern4 = r'John\w?' #['John', 'Johns', 'Johnn', 'Johnn']
print(re.findall(pattern4, msg))

print("----------------------------------------", 'demo- dswDSW', "-"*40)
import re
msg = '1 cat, 2 dog, 3 pigs, 4 swans'
pattern = r'\d+\s\w+' #['1 cat', '2 dog', '3 pigs', '4 swans']
print(re.findall(pattern, msg))

print("----------------------------------------", 'demo-Character Class', "-"*40)
import re
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '[aeiouAEIOU]'
pattern2 = '[^aeiouAEIOU]'
print(re.findall(pattern, msg))
print("-"*17)
print(re.findall(pattern2, msg))
print("-"*17)
msg = '1. cat, 2. dog, 3. pigs, 4. swans'
pattern3 = '[2-5.]'
pattern4 = '[^2-5.]'
print(re.findall(pattern3, msg))
print("-"*17)
print(re.findall(pattern4, msg))
print("-"*17)

print("----------------------------------------", 'demo- ^ $ in regular expression', "-"*40)
import re
msg = 'John will attend my party tonight.'
pattern = r'^John' #at first
print(re.findall(pattern, msg))
msg = 'MY best friend is John.'
pattern = r'^John'
print(re.findall(pattern, msg))

import re
msg = 'John will attend my party 28 tonight.'
pattern = r'\W$'
txt = re.findall(pattern,msg)
print(txt)

msg = 'I am 28'
pattern = r'\W$'
txt = re.findall(pattern,msg)
print(txt)

msg = 'I am 28'
pattern = r'\d$'
txt = re.findall(pattern,msg)
print(txt)

msg = 'I am 28 year old.'
pattern = r'\d$'
txt = re.findall(pattern,msg)
print(txt)

import re
msg = '09282028222'
pattern = r'^\d+$'
txt = re.findall(pattern,msg)
print(txt)

msg = '0928tuyr990'
pattern = r'^\d+$'
txt = re.findall(pattern,msg)
print(txt)

print("----------------------------------------", 'demo- . (wildcard)', "-"*40)
import re
msg = 'Cat hat sat at matter flat'
pattern = r'.at' #['Cat', 'hat', 'sat', ' at', 'mat', 'lat']
txt = re.findall(pattern, msg)
print(txt)

print("----------------------------------------", 'demo- .*', "-"*40)
msg2 = 'Name: Tzu-chien Tseng Address: 2 Taichun, 2A.'
pattern = r'Name:(.*) Address: (.*)'
txt = re.search(pattern, msg2)
Name, Address = txt.groups()
print("Name: ", Name)
print("Address: ", Address)

print("----------------------------------------", 'demo- re.DOTALL(跳過換行字元)', "-"*40)
msg3 = 'Name: Tzu-chien Tseng\n Address: 2 Taichun, 2A.'
pattern = r'.*'
print("Exist \'\\n\': ", re.search(pattern, msg3).group())
txt = re.search(pattern, msg3, re.DOTALL)
print(txt.group())

print("----------------------------------------", 'demo-re.match() (The pattern should at the start!)', "-"*40)
import re 
msg = 'John will attend my party tonight. '
pattern = 'John'
txt = re.match(pattern, msg)
if txt != None:
    print("Out put: ", txt.group())
    print("MatchObject: ", txt)
else:
    print("Out put: None")

msg = 'My best briend is John.'
pattern = 'John'
txt = re.match(pattern, msg)
if txt != None:
    print("Out put: ", txt.group())
    print("MatchObject: ", txt)
else:
    print("Out put: None")

print("----------------------------------------", 'demo-group(), end(), start(), span()', "-"*40)
import re
print("match()")
msg = 'John will attend my party tonight. '
pattern = 'John'
txt = re.match(pattern, msg)
if txt != None:
    print("start() index: ", txt.start())
    print("end() index: ", txt.end())
    print("span() index: ", txt.span())
    print("group() index: ", txt.group())

print("search()")
msg = 'My best friend is John. '
pattern = 'John'
txt = re.search(pattern, msg)
if txt != None:
    print("start() index: ", txt.start())
    print("end() index: ", txt.end())
    print("span() index: ", txt.span())
    print("group() index: ", txt.group())

print("----------------------------------------", 'demo-result = re.sub(pattern, newstr, msg) ', "-"*40)
import re
msg = 'Eli Nan will attend my party tonight. My best friend is Eli Nan.'
pattern = 'Eli Nan'
newstr = 'Sunny Tseng'
txt = re.sub(pattern, newstr, msg)
print(txt) if txt != msg else print("sub() FAIL!")

msg = 'Eli Nan will attend my party tonight. My best friend is Eli Nan.'
pattern = 'Eli Thomson'
newstr = 'Sunny Tseng'
txt = re.sub(pattern, newstr, msg)
print(txt) if txt != msg else print("sub() is FAIL! Origin Txt:", txt)

print("----------------------------------------", 'demo-CIA_sub()', "-"*40)
import re
msg = 'CIA Mark told CIA linda that secret USB had given to CIA Peter.'
pattern = r'CIA (\w)\w*'
newstr = r'\1***' #capture group 1
txt  = re.sub(pattern, newstr, msg)
print(txt)

import re
pattern = r'CIA \w(\w)\w*'
newstr = r'\1***'
text = 'CIA Mark told CIA linda that secret USB had given to CIA Peter.'
result = re.sub(pattern, newstr, text)
print(result)  # 輸出結果將是 "g***"

import re
pattern = r'CIA (\w)(\w)\w*'
newstr = r'\2***' #capture group 2
text = 'CIA Mark told CIA linda that secret USB had given to CIA Peter.'
result = re.sub(pattern, newstr, text)
print(result)  # 輸出結果將是 "g***"

print("----------------------------------------", 'demo-Phone Number (VERBOSE可加註解)', "-"*40)
import re
msg = '''02-88223349,
        (02)-26669999,
        02-29998888 ext 123,
        12345678,
        02 33887766 ext. 12,
        02 33887766 ext. 1234,
        12345,
        123'''

pattern = r'''(
                (\d{2}|\(\d{2}\))?     # 區域號碼
                (\s|-)?                # 區域號碼與電話號碼的分隔符號
                \d{8}                  # 電話號碼
                (\s*(ext|ext.)\s*\d{2,4})? # 2-4位數的分機號碼
            )'''

phoneNum = re.findall(pattern, msg, re.VERBOSE)
print("以下是符合的電話號碼")
for num in phoneNum:
    print(num[0])
"""
02-88223349
(02)-26669999
02-29998888 ext 123
 12345678
02 33887766 ext. 12
02 33887766 ext. 1234
"""
print("----------------------------------------", 'demo-Email address', "-"*40)
import re
msg = '''txt@deepmind.com.tw
        kkk@gmail.com,
        abc@aa
        abcdefg'''

pattern = r'''(
                [a-zA-Z0-9._]+       # 使用者帳號
                @                    # @符號
                [a-zA-Z0-9.-]+       # 主機域名domain
                [\.]                 # .符號
                [a-zA-Z]{2,4}        # 可能是com或edu或其它
                ([\.]?)              # 符號, 也可能無特別是美國
                ([a-zA-Z]{2,4})?     # 國別
            )'''

eMail = re.findall(pattern, msg, re.VERBOSE)
print("以下是符合的電子郵件地址")
for mail in eMail:
    print(mail[0])
"""
txt@deepmind.com.tw
kkk@gmail.com
"""

print("----------------------------------------", 'demo', "-"*40)