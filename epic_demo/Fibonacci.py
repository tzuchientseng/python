"""
method 1:
"""
num = int(input('Enter the number(n > 2): \n'))
_list = [1, 1]
for i in range(num-2):
    _list.append(_list[-1] + _list[-2])
print(_list)

"""
method 2:
"""
def fib(x):
    if(x <= 1):
        return x
    else:
        return fib(x-2) + fib(x-1)

n = int(input("(fibonacci_1) enter 'n' :\n"))

for i in range(1, n + 1):
    print(fib(i), end=" ")

"""
method 3:
"""
print()
from functools import reduce

def fibonacci_sequence(n):
    if n <= 0:
        return ['none']
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    seq = [1, 1] # initial list with the first two fibonacci numbers

    # define a function to compute the next fibonacci number
    def next_fib(seq):
        return seq + [seq[-1] + seq[-2]]
    
    # use reduce to generate the fibonacci sequence
    return reduce(lambda seq, _ : next_fib(seq), range(n - 2), seq) #reduce(函數(要兩個引數), 迭代(執行n-2次), 初始值)-> reduce(function, iterable, [initializer])
    #or return reduce(lambda seq, _: seq + [seq[-1] + seq[-2]], range(n - 2), seq)

n = int(input("(fibonacci_2) enter 'n' :\n"))

print(fibonacci_sequence(n))

"""
    def reduce_fib(seq, _):
        return seq + [seq[-1] + seq[-2]]
    return reduce(reduce_fib, range(n - 2), seq)
"""
"""
def fibonacci_sequence(n):
    def next_fib(seq):
        return seq + [seq[-1] + seq[-2]]
    def reduce_fib(seq, _):
        return next_fib(seq)
    return reduce(reduce_fib, range(n - 2), seq)
"""