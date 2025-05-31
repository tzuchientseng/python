import numpy as np
import time

a = []
t1 = time.time()

for i in range(1000):
    a += ["hello"] * 1000

a = np.array(a)
t2 = time.time()
print(len(a), a)
print(f'list相加:{t2-t1}秒')

a = np.empty(0, dtype=object)
t1 = time.time()
for i in range(1000):
    a = np.r_[a, ["hello"] * 1000]

t2 = time.time()
print(len(a), a)
print(f'np相加:{t2-t1}秒')

# 優化，才是整個專案的重點，細節決定成敗
# 先求有，再求好。結果整個專案需重新來過
