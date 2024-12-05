import numpy as np
a = [1,2,3,4]
b = [5,6,7,8]
c = np.c_[a, b] # 合併column
print(c)
d = np.r_[a, b] # 陣列
print(d)
print(a + b)#list
print(np.array(a + b)) # 陣列
