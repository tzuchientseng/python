import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
a=tf.constant(10.8)
print(a)
b=tf.cast(a, tf.int32)#去除尾數
print(b)