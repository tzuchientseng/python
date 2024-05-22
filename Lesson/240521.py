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