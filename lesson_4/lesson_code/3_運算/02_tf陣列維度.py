import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
a = tf.ones(shape=[], dtype=tf.int32) # 純量，根本不是陣列
print(a) # 不能帶索引
b = tf.ones(shape=[1], dtype=tf.int32) # 陣列，一維一元素
print(b[0])
c = tf.ones(shape=[10], dtype=tf.int32) # 陣列, 一維多元素
print(c[8])
d = tf.ones(shape=[2,3], dtype=tf.int32)
print(d[0,1]) # d[0][1]亦可，kotlin 好像也是二個都可以，是 java & python 的集合体
print("d.shape : ", d.shape)
print("d.shape[0] : ", d.shape[0])
print("d[0].shape:",d[0].shape) #使用此法比較少
e = tf.ones(shape=(2,5), dtype=tf.int32) # 此法是傳入 tuple
print(e)
print("tf.shape(d) : ", tf.shape(d)) # 此法通常是要傳給 GPU 計算
