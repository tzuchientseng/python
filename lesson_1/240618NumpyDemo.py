print("----------------------------------------", 'demo-Numpy_Array', "-"*40)
import numpy as np
x = [5,1,8]
y = [5,14,8]
z = [17,34,98]

z1 = np.array([x,y,z])
z2 = np.array([z1, z1])
print(z2)
print(z2[0,0,1])
print(z2[1,2,1])
print(z2[1,0,1])

print("----------------------------------------", 'demo', "-"*40)
import numpy as np

x = np.arange(16).reshape(4, 4)  # reshape設定規模
print(x)

y1, y2 = np.hsplit(x, 2)  # 水平方向分為兩個陣列
#print(y1)
#print(y2)

z1, z2 = np.vsplit(x, 2)  # 垂直方向分為兩個陣列
print(z1)
print(z2)

print("----------------------------------------", 'demo', "-"*40)
import numpy as np

# 練習(1):
x = np.arange(1, 51).reshape(10, 5)
print(x)

# 練習(2):
y = np.ones((2, 4), dtype=int)
z = y * 8
print(z)

# 練習(3):
a = [x for x in range(20)]
a1 = np.array(a)
print(a1)
print(a1[::2])
print(a1[1::2])
b = np.arange(20).reshape(1, 20)
print(b)

print("----------------------------------------", 'demo', "-"*40)