"""
第一題:
"""
for i in range(1,10):
    for j in range(1,10):
        if(i >= j):
            print(j, end=" ")
    print()
for i in range(1,10):
    for j in range(1,10):
        if(i < j):
            print(j, end=" ")
    print()

"""
第二題:
x plus to y
"""

x, y = map(int, input("Please enter two numbers separated by a space: \n").split())
try:
    if y < x:
        raise ValueError("y must be greater than or equal to x")
except ValueError as e:
    print(e)
else:
    result = sum(i for i in range(x, y+1))
    print("The sum of integers from", x, "to", y, "is:", result)
