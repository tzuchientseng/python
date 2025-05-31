#pip install matplotlib
import os
import tensorflow as tf
import pylab as plt
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
batch=10000
# x=np.random.normal(size=batch)
# y=np.random.normal(size=batch)
# x=tf.random.normal(shape=[batch])#標準常態分佈
# y=tf.random.normal([batch])
x=tf.random.uniform(shape=[batch])#平均分佈
y=tf.random.uniform([batch])
print(x)
#matplotlib除了吃 list, numpy陣列，也吃 tf 格式
plt.scatter(x, y, s=0.1)
plt.show()