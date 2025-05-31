import numpy as np
a = [1,2,3,4]
b = [5,6,7,8]
c = np.c_[a, b] # 合併column
print(c)
"""
[[1 5]
 [2 6]
 [3 7]
 [4 8]]
"""
d = np.r_[a, b] # numpy陣列
print(d)
# [1 2 3 4 5 6 7 8]
print(a + b) # list
# [1, 2, 3, 4, 5, 6, 7, 8]
print(np.array(a + b)) # numpy陣列
# [1 2 3 4 5 6 7 8]
