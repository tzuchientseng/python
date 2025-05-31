print("----------------------------------------", 'demo', "-"*40)
import numpy as np
x = np.array([31,27,39,52])
print(x[0])
print(x[1])
print(x[2])
print(x[3])

print(x)
x[2] = 200
print(x)

print("----------------------------------------", 'demo-field', "-"*40)
import numpy as np 
x= np.array([3,4,5,6])
print(x.ndim) #輸出陣列維度
print(x.shape) #輸出陣列外型 output: (4,)
print(x.size) #輸出認列元素個數

print("----------------------------------------", 'demo', "-"*40)
import numpy as np 
x= np.array([3,4,5,6])
print(x + 10)
y = np.array([1,2,3,4])
print("x + y:", x + y)
print("x - y:", x - y)
print("x * y:", x * y)
print("x / y:", x / y)
print("x > y:", x > y)

print("----------------------------------------", 'demo-method', "-"*40)
import numpy as np

x = np.array([31, 27, 39, 52])
y = np.array([1, 42, 13, 52])
z = np.concatenate((x, y))  # 合并数组
print(z)

z1 = np.insert(x, 1, 50)
print(z1)

z2 = np.delete(x, 2)
z3 = np.delete(y, [1, 2])
print(z2)
print(z3)

print("----------------------------------------", 'demo-method', "-"*40)
