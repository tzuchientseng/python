print("----------------------------------------", 'demo-try_exception_else', "-"*40)
def division(x, y):
    try:
        ans = x / y
    # except ZeroDivisionError:
    #     print('Error: Divisor cannot be zero.')
    # except TypeError as e:
    #     print('Error: ', e)
    except (ZeroDivisionError, TypeError) as e:
        print(e)
    else:
        return ans
print(division(10, 0))
print(division('a', 'b'))

print("----------------------------------------", 'demo-FileNotFoundError', "-"*40)
fn = 'XXX.txt'
try: 
    with open(fn) as fObj:
        data = fObj
except FileNotFoundError as e:
    print(e) 
else:
    print(data)

print("----------------------------------------", 'demo-words count', "-"*40)
fn = 'temp\\test.py'
try:
    with open(fn) as fObj:
         data = fObj.read()
except FileNotFoundError as e:
    print(e) 
else:
    wordList = data.split()
    print(f"{fn} words: {len(wordList)}")
    print(data)

print("----------------------------------------", 'demo-Exception', "-"*40)
def division(x, y):
    try:
        ans = x / y
    except Exception as e:
        print(e)
    # except:
    #     print('Error')
    else:
        return ans
print(division(10, 0))
print(division('a', 'b'))

print("----------------------------------------", 'demo-raise Exception(\'XXX\')', "-"*40)
def passWord(pwd):
    pwdlen = len(pwd)
    if pwdlen < 5:
        raise Exception('Too short!!')
    if pwdlen > 8:
        raise Exception('Too long')
    print('Password: valid!')

for pwd in ('ddfdfdfsldjdfksj', 'ddd','kdkdkd'):
    try:
        passWord(pwd)
    except Exception as err:
        print("Password: ", str(err))

print("----------------------------------------", 'demo-Traceback(format_exc())', "-"*40)
import traceback

def passWord(pwd):
    pwdlen = len(pwd)
    if pwdlen < 5:
        raise Exception('Too short!!')
    if pwdlen > 8:
        raise Exception('Too long')
    print('Password: valid!')

for pwd in ('ddfdfdfsldjdfksj', 'ddd','kdkdkd'):
    try:
        passWord(pwd)
    except Exception as err:
        errlog = open('temp/errlog.txt', 'a') # Open error file
        # errlog.write(traceback.format_exc()) # Write traceback to error file
        errlog.close()
        print("New a file!!!(errlog.txt)")
        print("ERROR:", str(err))

print("----------------------------------------", 'demo-finally', "-"*40)
import traceback

def division(x, y):
    try:  # try - except statement
        return x / y
    except:  # Catch all exceptions
        errlog = open('temp/error.txt', 'a')  # Open error file
        # errlog.write(traceback.format_exc())  # Write traceback to error file
        errlog.close()  # Close error file
        print("Writing traceback to error file errch15_17.txt completed")
        print("An exception occurred")
    finally:
        print("Completed")

print(division(10, 2))  # Print 10 / 2
print(division(5, 0))  # Print 5 / 0
print(division('a', 'b'))  # Print 'a' / 'b'
print(division(6, 3))  # Print 6 / 3

print("----------------------------------------", 'demo-assert (optimize)', "-"*40)
class Banks(): # 定義銀行類別
    title = 'Taipei Bank' # 定義屬性
    def __init__(self, uname, money): # 初始化方法
        self.name = uname # 設定存款者名字
        self.balance = money # 設定所有的錢
    
    def save_money(self, money): # 設計存款方法
        assert money > 0, '存款money必須大於0' # 存款檢查
        self.balance += money # 執行存款
        print('存款', money, '完成') # 列印存款完成
    
    def withdraw_money(self, money): # 設計提款方法
        assert money > 0, '提款money必須大於0' # 提款檢查
        assert money <= self.balance, '存款金額不足' # 檢查餘額
        self.balance -= money # 執行提款
        print('提款', money, '完成') # 列印提款完成
    
    def get_balance(self): # 獲得存款餘額
        print(self.name.title(), '目前餘額:', self.balance)
        
sunnybank = Banks('sunny', 100) # 定義物件sunnybank
sunnybank.get_balance() # 獲得存款餘額
sunnybank.save_money(300) # 存款300元
sunnybank.get_balance() # 獲得存款餘額
sunnybank.save_money(-300) # 存款-300元
sunnybank.get_balance() # 獲得存款餘額

print("----------------------------------------", 'demo-logging', "-"*40)
import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, format='')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s : %(message)s')

logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')

print("----------------------------------------", 'demo-debug', "-"*40)
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('--start--')                
for i in range(5):
    logging.debug(f"Current Index: {i}")
logging.debug('--end--')                

print("----------------------------------------", 'demo-debug', "-"*40)
import logging
logging.basicConfig(level=logging.CRITICAL,
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

print("----------------------------------------", 'demo-debug', "-"*40)
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

print("----------------------------------------", 'demo-copy', "-"*40)
logging.disable(logging.CRITICAL) 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')

print("----------------------------------------", 'demo', "-"*40)