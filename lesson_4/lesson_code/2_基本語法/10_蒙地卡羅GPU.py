import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import time
import numpy as np
batch=100_000_000
epoch=4000
incircle=0
for e in range(epoch):
    t1=time.time()
    #points = [np.random.uniform(0, 1, batch), np.random.uniform(0, 1, batch)]
    points=[tf.random.uniform(shape=[batch]), tf.random.uniform(shape=[batch])]
    #dist = np.sqrt(np.square(points[0]) + np.square(points[1]))
    dist=tf.sqrt(tf.square(points[0])+tf.square(points[1]))
    #incircle+=np.where(dist<=1)[0].shape[0]
    incircle += tf.where(dist <= 1).shape[0]
    t2=time.time()
    print(f'epoch:{e+1} ,花費時間:{t2-t1:.4f}秒, pi={incircle/((e+1)*batch)*4}')