#標準差(std)絕對是正值
#是一組數字的離散程度
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
np.random.seed(1)
a=np.random.randint(1,100,3)
print(a)
print("mean : ", np.mean(a))
#每個數與平均數差的平方，加總起來，再除數量，最後開根號
#(((38-41.3)^2+(13-41.3)^2+(73-41.3)^2)/3)^0.5
print("np.std : ", np.std(a))

sum=0
mean=np.mean(a)
for x in a:
    sum+=(x-mean)**2
std=(sum/len(a))**0.5
print("手動標準差 : ", std)