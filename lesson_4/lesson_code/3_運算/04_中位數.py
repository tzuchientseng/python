import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
# 奇數中位數 : 排序後，取得中間的值
np.random.seed(2)
a = np.array([1,80,5,9,20], dtype=np.int32)
print(np.median(a))
b = np.random.randint(1,100,5)
print("排序前 :",b)
print(np.median(b))
c = np.sort(b)
print("排序後 : ", c)
print(np.median(c))

# 偶數中位數 : 排序後，取最中間的二個值，相加後/2
d = np.array([1,2,3,4])
print("偶數中位數 : ",np.median(d))