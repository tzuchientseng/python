print("-"*7, 'demo-訂單生成', "-"*7)
title = ['商品', '單價', '數量', '小計']
a = []  
b = 0
while True:  
    x1 = input("請輸入商品名稱:")
    x2 = eval(input("請輸入單價:"))
    x3 = eval(input("請輸入數量:"))
    y = input('是否還有商品需要輸入 y/n?')
    a1 = [] 
    a1.append(x1)
    a1.append(x2)
    a1.append(x3)
    a1.append(x2*x3)
    a.append(a1)
    b += x2*x3
    if y == 'n':
        break

print("您的訂單總金額為:")
print(title)
for item in a:
    print(item)
print("總金額:", b)

print("-"*7, 'demo', "-"*7)
# 定義集合 A, B, C
A = {n for n in range(1, 21)}
B = {n for n in range(1, 21) if n % 2 == 0}
C = {n for n in range(1, 21) if n % 3 == 0}

# 計算三個集合的交集
intersection = A & B & C
print(f"三個集合的交集: {sorted(intersection, key=lambda x: x, reverse=False)}")

# 計算三個集合的聯集
union = A | B | C
print(f"三個集合的聯集: {sorted(union)}")

# 計算 A - B - C 的差集
minus = A - B - C
print(f"A - B - C: {sorted(minus)}")

print("-"*7, 'demo2-計算 12, 27, 10 的最小公倍數', "-"*7)
a = 12
b = 27
c = 10

def lcm(x, y):
    from math import gcd
    return x * y // gcd(x, y)

lcm_ab = lcm(a, b)
lcm_abc = lcm(lcm_ab, c)

print(f"12, 27, 10 的最小公倍數為: {lcm_abc}")


print("-"*7, 'demo', "-"*7)
def absolute(x):
    return x if x >= 0 else -x
x = input("Input number: \n")
# print("|x| = ", absolute(x))

def comp(x, y):
    print(x) if x > y else print(y)

a, b = map(int, input("Enter two number:\n"))

print("Bigger Number", end="")
comp(a,b)

comp(x = 3, y = 7)

"""
@author: User
"""

print("-"*7, 'demo', "-"*7)
def comp(x, y):  # 顯示 x 和 y 生成比大小
    z = x - y
    return z  # comp(x, y) = z

a, b = eval(input("請輸入兩個數字："))
print('相減的結果是', comp(a, b))

a, b = map(int, input("Enter two number:\n").split(' '))
# ------------------------------------------
def comp(x, y):  # 顯示 x 和 y 生成比大小
    z = x - y
    print(z)  # 顯示 z 值出 / 並沒有回傳結果comp(x, y)

a, b = eval(input("請輸入兩個數字："))
print('相減的結果是', comp(a, b)) #輸出None

# ------------------------------------------
# ------------------------------------------
print("-"*7, 'demo', "-"*7)

from enum import Enum, auto

class Operation(Enum):
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()

def addi(x, y):
    return x + y

def diff(m, n):
    return m - n

def mult(p, q):
    return p * q

def over(i, j):
    return i / j

def main():
    print("1 加法 / 2 減法 / 3 乘法 / 4 除法")
    
    try:
        num = int(input("請輸入您要運算的代號: "))
        a, b = map(float, input("請輸入兩個數字: ").split())
    except ValueError:
        print("輸入錯誤，請輸入有效的數字")
        return
    
    if num not in range(1, 5):
        print("代號輸入錯誤")
        return

    operation = Operation(num)

    if operation == Operation.ADDITION:
        result = addi(a, b)
        print("兩數相加的結果為:", result)
    elif operation == Operation.SUBTRACTION:
        result = diff(a, b)
        print("兩數相減的結果為:", result)
    elif operation == Operation.MULTIPLICATION:
        result = mult(a, b)
        print("兩數相乘的結果為:", result)
    elif operation == Operation.DIVISION:
        if b == 0:
            print("除數不能為零")
        else:
            result = over(a, b)
            print("兩數相除的結果為:", result)

if __name__ == "__main__":
    main()


print("-"*7, 'demo', "-"*7)

import time
def times(x):
    print(x, end='')
    time.sleep(1)
    return 0 if x == 0 else times(x-1)
times(3)