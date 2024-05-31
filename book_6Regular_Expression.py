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

print("----------------------------------------", 'demo-group(), groups()', "-"*40)
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

print("----------------------------------------", 'demo-Character classification', "-"*40)
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

print("----------------------------------------", 'demo- ^ in regular expression', "-"*40)
import re
msg = 'John will attend my party tonight.'
pattern = '^John' #at first
print(re.findall(pattern, msg))
msg = 'MY best friend is John.'
pattern = '^John'
print(re.findall(pattern, msg))

print("----------------------------------------", 'demo- $ in regular expression', "-"*40)
