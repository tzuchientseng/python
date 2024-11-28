import os
import tensorflow as tf
import pylab as plt
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
a=tf.random.normal(shape=[])#只有一個數，所以不是陣列
print(a)

b=tf.random.normal(shape=[3])#一維，有三個元素
print(b)

c=tf.random.normal([2,3])#二維，2列3行
print(c.shape)

d=np.random.random([2,10])
print(d.shape)

