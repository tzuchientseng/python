print("-"*7, 'demo', "-"*7)

import time

def dect(x):
    time.sleep(1)
    print(x, end=" ")
    if x < 1: 
        return 0 #放任和數字都可
    else:
        dect(x-1)
dect(4)

print("\n", "-"*7, 'demo-Fibonacci', "-"*7)

def fib(x):
    if x > 1:
        return fib(x - 1) + fib(x - 2)
    return x 

for n in range(1, 10):
    print(fib(n), end=' ')

print("\n", "-"*7, 'demo', "-"*7)

def add(x, y):
    return x+y

def func(fun, x, y):
    return fun(x, y)

print(func(add, 12, 3))

print("-"*7, 'demo-try_except', "-"*7)

def divid(x, y):
    try:
        n = x/y
    except ZeroDivisionError:
        print("ZeroDivisionError!")
    except TypeError:
        print("TypeError!")
    except: #Catch 所有exception
        print("!!!!!!There is a error!!!!!!")
    else:
        return n

print(divid(20, 4))
print(divid(20, 0)) #return (ZeroDivisionError + null)

print("-"*7, 'demo', "-"*7)

def food(x, y='orange'):
    print('My favorie food is ', x, y)
food(x = 'orange')

def food(x, y='orange'):
    return'My favorie food is ', x, y
print(food(x = 'orange'))

print("-"*7, 'demo-return multiple(exception)', "-"*7)

def fun(x, y):
    if y == 0:
        raise ValueError('y cannot be zero!')
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d
try:
    e, f, g, h = fun(10, 0)
except ValueError as ve:
    print(f"An error occurred: {ve}")


"""
public class Main {
    public static void main(String[] args) {
        try {
            double[] results = fun(10, 0);
            System.out.println("a: " + results[0]);
            System.out.println("b: " + results[1]);
            System.out.println("c: " + results[2]);
            System.out.println("d: " + results[3]);
        } catch (IllegalArgumentException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    public static double[] fun(int x, int y) {
        if (y == 0) {
            throw new IllegalArgumentException("y cannot be zero!");
        }
        double a = x + y;
        double b = x - y;
        double c = x * y;
        double d = (double) x / y; // 類型轉換以避免整數除法

        return new double[]{a, b, c, d};
    }
}

"""

print("-"*7, 'demo-return dict', "-"*7)
def bub(num, name):
    vip = {"NO.": num, "Name:":name}
    return vip
member = bub(5, "Sunny")
print(member)

try:
    # 嘗試進行某些操作
    result = 10 / 0  # 這裡會拋出ZeroDivisionError
except ZeroDivisionError as e:
    # 當捕捉到ZeroDivisionError時，執行這裡的代碼
    print(f"An error occurred: {e}")
finally:
    # 無論是否拋出異常，都會執行這裡的代碼
    print("This will always be executed.")

print("----------------------------------------", 'demo-Defined Exception', "-"*40)
def password(x):
    pwdlen = len(x)
    if pwdlen <=6:
        raise Exception("Pwd too short")
    elif pwdlen >= 12:
        raise Exception("Too long.")
    elif x != x.title():
        raise Exception("Capital letter!")
    else: 
        print("-------Password Valid-------")

pwd = input("Enter the password (6~12):\n")
password(pwd)