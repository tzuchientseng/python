print("----------------------------------------", 'Test', "-"*40)
import math
print(math.gcd(3,4))
print(math.lcm(3,4))

print("----------------------------------------", 'Test', "-"*40)
def gcd(n1, n2):
    init = 1
    i = 2
    while i <= n1 and i <= n2:
        if n1 % i == 0 and n2 % i == 0:
            init = i
        i += 1 
    return init
x, y = map(int, input("Enter two number: \n").split())
print("The Greatest Common Divisor(窮舉): ", gcd(x, y))

print("----------------------------------------", 'Test', "-"*40)
def gcd2(a, b):
    if a < b:
        a, b = b, a 
        while b != 0:
            temp = a % b
            a = b 
            b = temp
        return a
x, y = map(int, input("Enter two number: \n").split())
print("The Greatest Common Divisor(輾轉): ", gcd(x, y))

print("----------------------------------------", 'Test', "-"*40)
def gcd_recursive(x, y):
    return x if y == 0 else gcd(y, x % y)
def lcm(x, y):
    return x * y // gcd_recursive (x, y)
x, y = map(int, input("Enter two number: \n").split())
print("The Greatest Common Divisor(遞迴): ", gcd_recursive(x, y))
print("The Least Common Multiple: ", lcm(x, y))

print("----------------------------------------", 'Test', "-"*40)
