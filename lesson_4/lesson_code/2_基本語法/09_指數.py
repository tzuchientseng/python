import os
import time
import tensorflow as tf
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
#整數無法開根號
a=tf.constant(10.)
print(tf.sqrt(a))
#平方
b=tf.constant(10.)
print(tf.square(b))

batch=100_000_000
a=np.random.uniform(size=batch)
t1=time.time()
b=np.square(a)
t2=time.time()
print(f'numpy 花費 : {t2-t1}秒')

a=tf.random.uniform(shape=[batch])
t1=time.time()
b=tf.square(a)
t2=time.time()
print(f'tf 花費 : {t2-t1}秒')