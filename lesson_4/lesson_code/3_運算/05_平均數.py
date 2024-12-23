import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
np.random.seed(1)
a=np.random.randint(1,100,3)
print(a)
print("np.mean : ", np.mean(a))

#底下是實際的運算，確認後，抽像化成 np.mean(a)
sum=0
for x in a:
    sum+=x
print("手動計算平均數 : ", sum/len(a))
