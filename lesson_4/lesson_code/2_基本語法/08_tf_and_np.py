import os
import time

import tensorflow as tf
import pylab as plt
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
batch=500_000_000
t1=time.time()
a=np.random.uniform(size=batch)
t2=time.time()
print(f'numpy 花費 : {t2-t1}秒')

t1=time.time()
a=tf.random.uniform(shape=[batch])
t2=time.time()
print(f'tf 花費 : {t2-t1}秒')
