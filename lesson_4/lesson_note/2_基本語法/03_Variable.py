import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
a=tf.Variable(3)
#b=tf.Tensor(3)穩死的
print(a)
#a = 10#將 a 的 tf物件摧毀掉，然後重建一個 python 的數字
a.assign(10)#此為正確的更改方式
print(a)
print(a.numpy())#純python的格式
print(a.dtype)